from django.db import models

# Create your models here.
# 数据模块
# 使用ORM框架


class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
    author = models.CharField(max_length=32)

    def __str__(self):
        return '标题： ' + self.title


class UserType(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self):
        return '用户职位：' + self.caption


class UserInfo(models.Model):
    user_name = models.CharField(max_length=32)
    age = models.IntegerField()
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)  # 外键

    def __str__(self):
        return '用户名：' + self.user_name


class Guest(models.Model):
    guest_name = models.CharField(max_length=32)

    def __str__(self):
        return '游客名：' + self.guest_name
