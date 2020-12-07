import os
import os.path
import tinify
import requests
from PIL import Image
from io import BytesIO
import io

tinify.key = "4WP5qvWSKm7wl4rj2TvCNtGs7vHHqd2L"
url = "https://api.tian999.top/"
dir_path = 'upload/'

def creat_img(src,article_name):
    if 'http://' in src or 'https://' in src:
        # 请求远程图片
        image = requests.get(src)
        # 转化为二进制
        image_data = Image.open(BytesIO(image.content))
        path = dir_path + article_name + '.png'
        image_data.save(path)
        with open(path,'rb') as f:
            size = len(f.read())
        if(size/1e3 > 1000):
            source = tinify.from_file(path)
            resized = source.resize(method="fit", width=700, height=400)    
        address = url + path
        # resized.to_file(address)
    else :
        pass
    return address