from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from morningapp.models import Article, Userinfo, Profile, Contact
from morningapp.model_data import model_data
from bs4 import BeautifulSoup
import random
import jwt
import time,datetime
# token密钥
salt = "dyxzdh"

# 注册


@api_view(['POST'])
def morn_register(request):
    # print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = Userinfo.objects.filter(username=username)
    if user:
        return Response('repeat')
    userID = random.randint(10000000, 99999999)
    old_user = Userinfo.objects.filter(userID=userID)
    while old_user:
        userID = random.randint(10000000, 99999999)
        old_user = Userinfo.objects.filter(userID=userID)
    new_user = Userinfo(userID=userID, username=username, password=password)
    new_profile = Profile(belong=new_user, userID=userID)
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
            user = Userinfo.objects.filter(username=username)
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
        user = Userinfo.objects.filter(username=username)
        if user:
            checkPwd = check_password(password, user[0].password)
            if checkPwd:
                token = create_token(username)
            else:
                return Response('pwderr')
        else:
            return Response('nouser')
    userID = user[0].userID
    profile_data = Profile.objects.filter(userID=userID)
    if profile_data:
        profile = model_data.add_profile(profile_data[0].nickname, profile_data[0].headimg,
                                         profile_data[0].sex, profile_data[0].birth,profile_data[0].age,
                                         profile_data[0].school, profile_data[0].education, profile_data[0].sign)
    else:
        profile = model_data.add_profile()
    contact_data = Contact.objects.filter(userID=userID)
    if contact_data:
        contact = model_data.add_contact(contact_data[0].weixin, contact_data[0].qq,
                               contact_data[0].email, contact_data[0].github, contact_data[0].weibo,)
    else:
        contact = model_data.add_contact()
    data = {
        'token': token,
        'profile': profile,
        'contact': contact,
        'username': username
    }
    return Response(data)



# 保存文章
@api_view(['POST'])
def add_article(request):
    token = request.POST['token']
    try:
        username = decode_token(token)
        user = Userinfo.objects.filter(username=username)
        if user:
            user = user[0]
        else :
            return Response('error')
    except Exception as e:
        print(e)
        return Response('error')
    title = request.POST['title']
    describe = request.POST['describe']
    cover = request.POST['cover']
    content = request.POST['content']
    rep_title = Article.objects.filter(title=title)
    if rep_title:
        return Response('repeat')
    # 保存文章
    new_article = Article(title=title)
    new_article.content = content
    new_article.describe = describe
    if len(cover) > 0:
        new_article.cover = cover
    new_article.birth = datetime.date.today()
    new_article.belong = user
    new_article.save()
    return Response('ok')



# 获取文章列表
@api_view(['GET'])
def get_articlelist(request):
    article = Article.objects.all()
    article_list = []
    num = 0
    for item in article:
        article_data = {
            'id':item.article_id,
            'title':item.title,
            'cover':item.cover,
            'time':item.createtime,
            'desc':item.describe,
            'author':item.belong.username
        }
        num = num + 1 
        article_list.append(article_data)
    data = {
        'num':num,
        'article_list':article_list,
    }
    return Response(data)
# 获取文章
@api_view(['GET'])
def get_article(request):
    article_id = request.GET['id']
    try:
        article_id = int(article_id)
        article = Article.objects.filter(article_id = article_id)
        if article:
            data = {
                'content':article[0].content
            }
            return Response(data)
        else :
            return Response('no article')
    except Exception as e:
        return Response('error')

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