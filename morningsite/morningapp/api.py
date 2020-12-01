from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
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
