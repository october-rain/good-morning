from django.contrib import admin
from morningapp.models import Article,Userinfo,Profile,Contact,Tag,Tag_Article
# Register your models here.
admin.site.register(Article)
admin.site.register(Userinfo)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Tag)
admin.site.register(Tag_Article)