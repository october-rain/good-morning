from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=80)
    cover = models.CharField(null=True, blank=True, max_length=300)
    describe = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField()
    belong = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='article_user')
    def __int__(self):
        self.id