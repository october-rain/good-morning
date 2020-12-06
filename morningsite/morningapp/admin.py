from django.contrib import admin
from morningapp.models import Article,Profile,Contact,Tag,Tag_Article,Mood
# Register your models here.
admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Tag)
admin.site.register(Tag_Article)
admin.site.register(Mood)