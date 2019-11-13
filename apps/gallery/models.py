from django.db import models
from django.utils.timezone import now

# Create your models here.


class Gallery(models.Model):
    title = models.CharField(default='项目标题', max_length=100)
    description = models.CharField(default='项目简介', max_length=300)
    image = models.ImageField(default='default.png', upload_to='images/')
    url = models.CharField(default="项目链接", max_length=100)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['last_mod_time']
        verbose_name = '项目名称'  # 指定后台显示模型名称
        verbose_name_plural = '项目列表'  # 指定后台显示模型复数名称
        db_table = "gallery"  # 数据库表名

