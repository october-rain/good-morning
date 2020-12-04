from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your models here.
# 文章表
# 用户表
class Userinfo(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
        super(Userinfo, self).save(*args, **kwargs)
    def __str__(self):
        return self.username
# 用户信息表
class Profile(models.Model):
    userID = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=25, blank=True)
    headimg = models.CharField(max_length=200, default='https://api.tian999.top/upload/headDefaultImg.jpeg')
    sex = models.CharField(max_length=4, blank=True)
    birth = models.DateField(blank=True,null=True)
    age = models.CharField(max_length=4, blank=True)
    school = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=10, blank=True)
    sign = models.CharField(max_length=200, blank=True)
    belong = models.OneToOneField(
        Userinfo, on_delete=models.CASCADE, blank=True)
    def __int__(self):
        return self.userID

# 联系方式表
class Contact(models.Model):
    userID = models.AutoField(primary_key=True)
    weixin = models.CharField(max_length=20, blank=True)
    qq = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=20, blank=True)
    github = models.CharField(max_length=20, blank=True)
    weibo = models.CharField(max_length=20, blank=True)
    belong = models.OneToOneField(
        Userinfo, on_delete=models.CASCADE, blank=True)
    def __int__(self):
        return self.userID
# 文章
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(null=True, blank=True, max_length=80)
    cover = models.CharField(null=True, blank=True, max_length=300,default='https://api.tian999.top/upload/pic.png')
    describe = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField()
    createtime = models.DateField(blank=True,null=True)
    belong = models.ForeignKey(
        Userinfo, on_delete=models.CASCADE, null=True,blank=True, related_name='article_user')
    def __str__(self):
        return self.title

# 标签
class Tag(models.Model):
    tagID = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=20)
    article = models.ManyToManyField(to='Article', through='Tag_Article', through_fields=('tagID', 'article_id'))
    belong = models.ForeignKey('self', on_delete=models.SET_NULL,
                               null=True, blank=True, related_name='Tag_children')
    def __str__(self):
        return self.tagname

#文章标签关联表
class Tag_Article(models.Model):
    tagID = models.ForeignKey(to='Tag', on_delete=models.CASCADE)
    article_id = models.ForeignKey(to='Article', on_delete=models.CASCADE,)
    def __int__(self):
        return self.id



