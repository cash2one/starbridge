from django.db import models
from myapps.activity.models import Order

# Create your models here.
# 报告
class Report(models.Model):
    # agent_id = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(Order,related_name = 'report_order', verbose_name='订单id')
    activity_id = models.IntegerField(blank=True, null=True, verbose_name='活动id')
    weixin_click = models.IntegerField(blank=True, null=True, verbose_name='微信点击量')
    weibo_click = models.IntegerField(blank=True, null=True, verbose_name='微博点击量')
    zhibo_click = models.IntegerField(blank=True, null=True, verbose_name='直播播出量')
    zhibo_read = models.IntegerField(blank=True, null=True, verbose_name='直播订阅量')
    zhibo_call = models.IntegerField(blank=True, null=True, verbose_name='直播访问量')
    click_time = models.DateTimeField(blank=True, null=True, verbose_name='点击时间')
    exposure_num = models.IntegerField(blank=True,null=True,verbose_name='曝光数')
    exposure_rate = models.FloatField(blank=True,null=True,verbose_name='曝光率')
    click_num = models.IntegerField(blank=True,null=True,verbose_name='点击数')
    click_rate = models.FloatField(blank=True,null=True,verbose_name='点击率')

    class Meta:
        db_table = 't_report'
        verbose_name = '报告'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.order_id)