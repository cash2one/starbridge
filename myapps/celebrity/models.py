from django.db import models

# Create your models here.
# 网红
class Celebrity(models.Model):
    GENDER_STATUS  = (
        ('0', '不限'),
        ('1', '女'),
        ('2', '男'),
        ('3', '其他'),
    )

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='网红名')
    key_words = models.CharField(max_length=255, blank=True, null=True, verbose_name='关键字')   ##	逗号分隔
    introduce = models.TextField(max_length=255, blank=True, null=True, verbose_name='介绍')
    avatar_url = models.ImageField(upload_to='img_avatar/%Y-%m-%d', blank=True, null=True, verbose_name='头像的url')
    cps = models.FloatField(blank=True, null=True, verbose_name='CPS')
    is_busy = models.IntegerField(blank=True, null=True, verbose_name='活动状态')
    gender = models.CharField(max_length = 1, choices = GENDER_STATUS, default = '2', verbose_name='性别')
    create_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='创建者')
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='创建时间')

    class Meta:
        db_table = 't_celebrity'
        verbose_name = '网红'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

#########################################################################  红人库 直播平台 个过滤分类
class CelebrityZhiCategory(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')

    class Meta:
        db_table = 't_celebrity_zhicategory'
        verbose_name = '基础数据-网红直播的分类 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class CelebrityZhiFansNum(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')

    class Meta:
        db_table = 't_celebrity_zhifansnum'
        verbose_name = '基础数据-网红直播的粉丝数 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class CelebrityZhiPrice(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')
    class Meta:
        db_table = 't_celebrity_zhiprice'
        verbose_name = '基础数据-网红直播的参考报价 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class CelebrityZhiArea(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')
    class Meta:
        db_table = 't_celebrity_zhiarea'
        verbose_name = '基础数据-网红直播的地域 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class CelebrityZhiPlatForm(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')
    class Meta:
        db_table = 't_celebrity_zhiplatform'
        verbose_name = '基础数据-网红直播的平台 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)
#########################################################################################################################################################

# 网红直播信息
class CelebrityZhibo(models.Model):
    CRED_STATUS = (
        ('A', '未认证'),
        ('B', '已认证'),
    )
    celebrity = models.ForeignKey(Celebrity, related_name = 'celebrity_zhibo', verbose_name='网红')
    broadcast_platform = models.ForeignKey(CelebrityZhiPlatForm,blank=True, null=True, verbose_name='直播平台',limit_choices_to={'sid__gt':0})    ##
    platform_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='网红在某直播平台中的id')
    url = models.URLField(max_length=255, blank=True, null=True, verbose_name='头像url链接')
    nickname = models.CharField(max_length=100, blank=True, null=True, verbose_name='直播平台中的昵称')

    is_credibility = models.CharField(max_length = 1, choices = CRED_STATUS, default = 'A', verbose_name='认证状态')
    area =  models.ForeignKey(CelebrityZhiArea, blank=True, null=True,verbose_name='地域', limit_choices_to={'sid__gt':0} )                         ##
    category =  models.ForeignKey(CelebrityZhiCategory, blank=True, null=True,verbose_name='分类',limit_choices_to={'sid__gt':0})                 ##

    fans_num = models.IntegerField(blank=True, null=True, verbose_name='粉丝数')
    average_num  = models.IntegerField(blank=True, null=True, verbose_name='平均观看数')
    reads_num = models.IntegerField(blank=True, null=True, verbose_name='订阅量')

    export_price = models.FloatField(blank=True, null=True, verbose_name='口头插播价格')
    ad_implants_price = models.FloatField(blank=True, null=True, verbose_name='商品露出价格')
    brand_exposed_price = models.FloatField(blank=True, null=True, verbose_name='品牌植入价格')

    memo = models.TextField(max_length=255, blank=True, null=True, verbose_name='备注')
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='修改时间') #auto_now=True,
    sid = models.IntegerField(verbose_name='红人头像id')

    class Meta:
        db_table = 't_celebrity_zhibo'
        verbose_name = '网红直播信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s -- %s" % (self.broadcast_platform.name, self.platform_id)


# 网红微博信息
class CelebrityWeibo(models.Model):
    celebrity = models.ForeignKey(Celebrity)
    type_id = models.IntegerField(blank=True, null=True, verbose_name='类型')
    nickname = models.CharField(max_length=255, blank=True, null=True, verbose_name='昵称')
    url = models.URLField(max_length=255, blank=True, null=True, verbose_name='url链接')
    fans_num = models.IntegerField(blank=True, null=True, verbose_name='粉丝数')
    is_authentication = models.IntegerField(blank=True, null=True, verbose_name='认证状态')
    forward_place = models.FloatField(blank=True, null=True, verbose_name='转发价格')
    direct_price = models.FloatField(blank=True, null=True, verbose_name='直发价格')
    memo = models.TextField(max_length=255, blank=True, null=True, verbose_name='备注')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        db_table = 't_celebrity_weibo'
        verbose_name = '网红微博信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.nickname)

# 网红微信信息
class CelebrityWeixin(models.Model):
    celebrity = models.ForeignKey(Celebrity)
    type_id = models.IntegerField(blank=True, null=True, verbose_name='微信类型')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='微信号名称')
    weixinid = models.CharField(max_length=100, blank=True, null=True, verbose_name='微信id')
    fans_num = models.IntegerField(verbose_name='粉丝数')
    price = models.FloatField(blank=True, null=True, verbose_name='参考价格')
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='投放位置')
    level = models.IntegerField(blank=True, null=True, verbose_name='推荐指数')
    scan_num = models.IntegerField(blank=True, null=True, verbose_name='阅读量参考')
    is_reserve = models.IntegerField(blank=True, null=True, verbose_name='是否接受预定')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')
    memo = models.TextField(max_length=11, blank=True, null=True, verbose_name='备注')

    class Meta:
        db_table = 't_celebrity_weixin'
        verbose_name = '网红微信信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

