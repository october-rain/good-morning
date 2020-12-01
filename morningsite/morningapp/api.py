from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from morningapp.models import Article
from bs4 import BeautifulSoup
import jwt
import time

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
    new_user = User(username=username, password=password)
    new_user.save()
    token = create_token(username, password)
    return Response(token)

# 登录
@api_view(['POST', 'GET'])
def morn_login(request):
    if request.method == 'GET':
        token = request.GET['token']
        try:
            info = jwt.decode(token, salt, True, algorithm='HS256')
            username = info['username']
            password = info['password']
            user = User.objects.filter(username=username)
            if user:
                checkPwd = check_password(password, user[0].password)
                if checkPwd:
                    return Response('ok')
            return Response('error')
        except Exception as e:
            print(e)
            
            return Response('error')
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username=username)
    if user:
        checkPwd = check_password(password, user[0].password)
        if checkPwd:
            token = create_token(username, password)
            return Response(token)
        else:
            return Response('pwderr')
    else:
        return Response('nouser')
# 生成jwtoken
def create_token(username, password):
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
        "password": password
    }
    # 配置主体信息，一般是登录成功的用户之类的，因为jwt的主体信息很容易被解码，所以不要放敏感信息
    # 当然也可以将敏感信息加密后再放进payload
    token = jwt.encode(headers=headers, payload=payload,
                       key=salt, algorithm='HS256').decode('utf-8')
    return token

#保存文章
@api_view(['POST'])
def add_article(request):
    title = request.POST['title']
    describe = request.POST['describe']
    cover = request.POST['cover']
    content = request.POST['content']
    rep_title = Article.objects.filter(title=title)
    if rep_title:
        return Response('repeat')
    # 保存文章
    new_article = Article(title=title)
    # 解析富文本html文档
    # soup = BeautifulSoup(content, 'html.parser')
    # # 获取所有img标签 图片
    # imgList = soup.find_all('img')
    # for img in range(0, len(imgList)):
    #     src = imgList[img]['src']
    #     # print(imgList[img]['src'])
    #     # 判断图片是远程还是本地
    #     if 'http://' in src or 'https://' in src:
    #         # 请求远程图片
    #         image = requests.get(src)
    #         # 转化为二进制
    #         image_data = Image.open(BytesIO(image.content))
    #         # print(image_data)
    #         # 设定文件名称
    #         image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-' + \
    #             str(new_article.id) + '-' + str(img)
    #         image_data.save("upload/"+image_name+".png")
    #         new_src = hostURL + 'upload/' + image_name + '.png'
    #         content = content.replace(src, new_src)
    #         # 封面设定
    #         if cover == src:
    #             cover = new_src
    #     else:
    #         image_data = base64.b64decode(src.split(',')[1])
    #         image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-' + str(new_article.id) + \
    #             '-' + str(img) + '.' + \
    #             src.split(',')[0].split('/')[1].split(';')[0]
    #         image_url = os.path.join('upload', image_name).replace('\\', '/')
    #         with open(image_url, 'wb') as f:
    #             f.write(image_data)
    #         new_src = hostURL + image_url
    #         content = content.replace(src, new_src)
    #         # 封面设定
    #         if cover == src:

    #             cover = new_src
    new_article.content = content
    new_article.describe = describe
    new_article.cover = cover
    new_article.save()
    return Response('ok')