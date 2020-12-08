from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from morningapp.models import Article, Profile, Contact, Tag, Tag_Article
from morningapp.model_data import model_data
from method import solve_img
from bs4 import BeautifulSoup
from PIL import Image
import os
import random
import jwt
import time
import datetime
import json
# token密钥
salt = "dyxzdh"

# 注册
@api_view(['POST'])
def morn_register(request):
    # print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username=username)
    if user:
        return Response('repeat')
    userID = random.randint(10000000, 99999999)
    old_user = User.objects.filter(id=userID)
    while old_user:
        userID = random.randint(10000000, 99999999)
        old_user = User.objects.filter(id=userID)
    new_password = make_password(password, username)
    new_user = User(id=userID, username=username, password=new_password)
    new_profile = Profile(belong=new_user, userID=userID)
    new_profile.nickname = '十月札记' + str(userID)
    new_Contact = Contact(belong=new_user, userID=userID)
    # 保存用户表
    new_user.save()
    # 保存用户信息表
    new_profile.save()
    # 保存联系方式表
    new_Contact.save()
    # 生成token
    token = create_token(username)
    data = {
        'token': token,
        'username': username
    }
    return Response(data)

# 登录
@api_view(['POST', 'GET'])
def morn_login(request):
    if request.method == 'GET':
        token = request.GET['token']
        try:
            username = decode_token(token)
            user = User.objects.filter(username=username)
            if user:
                pass
            else:
                return Response('error')
        except Exception as e:
            print(e)
            return Response('error')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if user:
            checkPwd = check_password(password, user[0].password)
            if checkPwd:
                token = create_token(username)
            else:
                return Response('pwderr')
        else:
            return Response('nouser')
    userID = user[0].id
    profile_data = Profile.objects.filter(userID=userID)
    data = {
        'userID':userID,
        'username':username,
        'nickname':profile_data[0].nickname,
        'headimg':profile_data[0].headimg,
        'token':token
    }
    return Response(data)
# 修改密码
@api_view(['POST'])
def change_password(request):
    try:
        token = request.POST['token']
        password = request.POST['password']
        username = decode_token(token)
        user = User.objects.filter(username=username)
        if user:
            user = user[0]
            user.password = password
            user.save()
            return Response('ok')
        else :
            return Response('error')
    except Exception as e:
        return Response('error')

# 获取个人信息
@api_view(['POST'])
def get_message(request):
    try:
        token = request.POST['token']
        username = decode_token(token)
        user = User.objects.get(username=username)
        userID = user.userID
        profile_data = Profile.objects.filter(userID=userID)
        contact_data = Contact.objects.filter(userID=userID)
    except Exception as e:
        return Response('error')

    if profile_data:
        profile = model_data.add_profile(profile_data[0].userID, profile_data[0].nickname, profile_data[0].headimg,
                                         profile_data[0].sex, profile_data[0].birth, profile_data[0].age,
                                         profile_data[0].school, profile_data[0].education, profile_data[0].sign)
    else:
        profile = model_data.add_profile()
    if contact_data:
        contact = model_data.add_contact(contact_data[0].weixin, contact_data[0].qq,
                                         contact_data[0].email, contact_data[0].github, contact_data[0].weibo,)
    else:
        contact = model_data.add_contact()
    data = {
        'username': username,
        'token': token,
        'profile': profile,
        'contact': contact
        
    }
    return Response(data)
# 发布文章
@api_view(['POST'])
def add_article(request):
    # print(cover)
    token = request.POST['token']
    try:
        username = decode_token(token)
        user = User.objects.filter(username=username)
        if user:
            user = user[0]
        else:
            return Response('error')
    except Exception as e:
        print(e)
        return Response('error')
    title = request.POST['title']
    describe = request.POST['desc']
    content = request.POST['content']
    rep_title = Article.objects.filter(title=title)
    if rep_title:
        return Response('repeat')
    # 保存文章
    new_article = Article(title=title)
    new_article.content = content
    new_article.describe = describe
    new_article.belong = user
    new_article.save()
    try:
        cover = request.POST['cover']
    except Exception as e:
        cover = request.FILES.get('cover')
    if cover != None:
        url = solve_img.creat_img(cover,new_article.article_id)
    else :
        url = ''
    if len(url) > 0:
        new_article.cover = url
    new_article.save()
    # 链接标签
    # 去json化 ，获取列表
    tag_list = json.loads(request.POST['tag'])
    for tag_id in tag_list:
        tag = Tag.objects.filter(tagID=tag_id)
        if tag:
            tag = tag[0]
            new_tag_article = Tag_Article(article_id=new_article, tagID=tag)
            new_tag_article.save()
    return Response('ok')


# 删除文章
@api_view(['POST'])
def del_article(request):
    article_id = request.POST['article_id']
    try:
        token = request.POST['token']
        username = decode_token(token)
        article = Article.objects.filter(article_id=article_id)
        if article:
            article = article[0]
            this_username = article.belong.username
            if username == this_username:
                cover  = article.cover
                path = cover.replace('https://api.tian999.top/','')
                os.remove(path)
                article.delete()
                return Response('ok')
            else:
                # 没有权限
                return Response('no perm')
        else:
            return Response('no article')
    except Exception as e:
        return Response('error')


# 获取文章
@api_view(['GET'])
def get_article(request):
    article_id = request.GET['id']
    try:
        article_id = int(article_id)
        article = Article.objects.filter(article_id=article_id)
        if article:
            data = {
                'content': article[0].content
            }
            return Response(data)
        else:
            return Response('no article')
    except Exception as e:
        return Response('error')
# 获取文章列表


@api_view(['GET', 'POST'])
def get_articlelist(request):
    if request.method == 'GET':
        article = Article.objects.all()
    else:
        try:
            token = request.POST['token']
            username = decode_token(token)
            user = User.objects.get(username=username)
            article = Article.objects.filter(belong=user)
        except Exception as e:
            return Response('error')
    article_list = []
    num = 0
    for item in article:
        Ttime = item.createtime
        this_time = Ttime.strftime('%Y-%m-%d %H:%M:%S')
        # 获取文章中的标签
        tag_article = Tag_Article.objects.filter(article_id=item.article_id)
        tag_data = []
        if tag_article:
            for tag in tag_article:
                data = {
                    'tagID':tag.tagID.tagID,
                    'tagname':tag.tagID.tagname,
                }
                tag_data.append(data)
        article_data = {
            'id': item.article_id,
            'title': item.title,
            'cover': item.cover,
            'time': this_time,
            'desc': item.describe,
            'author': item.belong.username,
            'tag_data':tag_data
        }
        num = num + 1
        article_list.append(article_data)
    data = {
        'num': num,
        'article_list': article_list,
    }
    return Response(data)


# 获取标签
@api_view(['GET'])
def get_tag(request):
    tag_list = Tag.objects.all()
    data = []
    for tag in tag_list:
        tagID = tag.tagID
        if tagID == 1:
            sort_data = {
                'sortID': tag.tagID,
                'sortname': tag.tagname,
                'tag_data': []
            }
        elif (tagID-1) % 100 == 0:
            data.append(sort_data)
            sort_data = {
                'sortID': tag.tagID,
                'sortname': tag.tagname,
                'tag_data': []
            }
        else:
            tag_data = {
                'tagID': tag.tagID,
                'tagname': tag.tagname
            }
            sort_data['tag_data'].append(tag_data)
    data.append(sort_data)
    return Response(data)
# 获取标签下的文章
@api_view(['GET'])
def get_taglist(request):
    tagID = request.GET['tagID']
    data = {
        'tagID':tagID,
        'article_data':[]
    }
    tag = Tag.objects.filter(tagID=tagID)
    if tag:
        tag_article = Tag_Article.objects.filter(tagID=tag[0])
        for item in tag_article:
            article_data = {
                'id': item.article_id.article_id,
                'title': item.article_id.title,
                'cover': item.article_id.cover,
                'time': item.article_id.createtime,
                'desc': item.article_id.describe,
                'author': item.article_id.belong.username,
            }
            data['article_data'].append(article_data)
    return Response(data)

# 生成jwtoken
def create_token(username):
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    # 设置headers，即加密算法的配置
    # 随机的salt密钥，只有token生成者（同时也是校验者）自己能有，用于校验生成的token是否合法
    exp = int(time.time() + 60*60)
    # 设置超时时间：当前时间的1s以后超时
    payload = {
        "username": username,
    }
    # 配置主体信息，一般是登录成功的用户之类的，因为jwt的主体信息很容易被解码，所以不要放敏感信息
    # 当然也可以将敏感信息加密后再放进payload
    token = jwt.encode(headers=headers, payload=payload,
                       key=salt, algorithm='HS256').decode('utf-8')
    return token

# token解码
def decode_token(token):
    info = jwt.decode(token, salt, True, algorithm='HS256')
    username = info['username']
    return username



# # 测试接口
# @api_view(['POST'])
# def test(request):
#     src = request.POST['src']
#     article_name = '文章的名称1'
#     url = solve_img.creat_img(src,article_name)
#     return Response(url)