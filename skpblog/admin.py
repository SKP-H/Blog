from django.contrib import admin

# Register your models here.
from skpblog.models import *


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('title','category','pub_time')

class Useradmin(admin.ModelAdmin):
    list_display = ('username','email','mobile')

admin.site.register({Category,Comment,Tag})
admin.site.register(UserProfile,Useradmin)