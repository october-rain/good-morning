from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
import os.path
import tinify
import requests
from PIL import Image
from io import BytesIO
import io
import datetime

tinify.key = "4WP5qvWSKm7wl4rj2TvCNtGs7vHHqd2L"
url = "https://api.tian999.top/"
dir_path = 'upload/'

def compress_img(path):
    with open(path,'rb') as f:
        size = len(f.read())
    if(size/1e3 > 1000):
        source = tinify.from_file(path)
        resized = source.resize(method="fit", width=700, height=400)
    else :
        pass  

def creat_img(src,article_id):
    # print(type(src))
    if isinstance(src,str):
        # 请求远程图片
        image = requests.get(src)
        # 转化为二进制
        image_data = Image.open(BytesIO(image.content))
        path = dir_path + str(article_id) + '-' + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + '.png'
        image_data.save(path)
        compress_img(path)
        # resized.to_file(address)
    else :
        path = str(article_id) + '-' + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + '.png'
        address = default_storage.save(path,ContentFile(src.read()))
        path = dir_path + path
        compress_img(path)
    return url + path