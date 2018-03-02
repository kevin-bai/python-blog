from django.contrib import admin

# Register your models here.
# 该应用的后台管理系统配置
from . import models


admin.site.register(models.Article)
admin.site.register(models.UserInfo)
admin.site.register(models.UserType)
admin.site.register(models.Guest)