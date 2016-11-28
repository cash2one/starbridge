from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 使用Abstractuser扩充fields
class CustomUser(AbstractUser):
    company = models.CharField(max_length=30, default='无', verbose_name="公司名称")
    contacts = models.CharField(max_length=30, default='无', verbose_name="联系人")
    phone = models.CharField(max_length=20, default=0, verbose_name="手机号码")
    url = models.URLField(null=True, blank=True, verbose_name="网址")

    def __str__(self):
        return "%s" % (self.username)

    class Meta:
        ordering = ['date_joined']
        verbose_name = '用户'
        db_table = 'custom_user'
        verbose_name_plural = verbose_name

