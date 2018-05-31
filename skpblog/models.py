from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.



#用户
class UserProfile(AbstractUser):
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"/static/image/ico.png",
        max_length=100,
        verbose_name=u"头像"
    )
    class Meta:
        verbose_name_plural = verbose_name = '我的信息'

    def __str__(self):
        return self.username



#文章类别
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='类别',max_length=20,unique=True)


    class Meta:
        verbose_name_plural = verbose_name = '类别'

    def __str__(self):
        return self.name


#文章标签
class Tag(models.Model):
    name = models.CharField(verbose_name='标签',max_length=20,unique=True)


    class Meta:
        verbose_name_plural = verbose_name = '标签'


    def __str__(self):
        return self.name


#文章
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(UserProfile,on_delete=models.DO_NOTHING,verbose_name='作者')
    title = models.CharField(verbose_name='标题',max_length=50)
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateField(verbose_name='日期',auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default=1,verbose_name='类别')
    tag = models.ManyToManyField(Tag,verbose_name='标签')


    class Meta:
        verbose_name_plural = verbose_name = '文章'

    def __str__(self):
        return self.title


#评论
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='昵称', max_length=20)
    email = models.EmailField(verbose_name='邮箱')
    content = models.TextField(verbose_name='内容')
    publish = models.DateField(verbose_name='时间', auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    reply = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='回复')

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return self.content