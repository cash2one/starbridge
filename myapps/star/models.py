from django.db import models

# Create your models here.
# 明星
class Star(models.Model):
    GENDER_STATUS  = (
        ('A', '不限'),
        ('B', '女'),
        ('C', '男'),
        ('D', '其他'),
    )
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='明星名称')
    key_words = models.CommaSeparatedIntegerField(max_length=255, blank=True, null=True, verbose_name='关键字')   ##	逗号分隔
    introduce = models.TextField(max_length=255, blank=True, null=True, verbose_name='介绍')
    avatar_url = models.ImageField(upload_to='img_avatar/%Y-%m-%d', blank=True, null=True, verbose_name='头像的url')
    cps = models.FloatField(blank=True, null=True, verbose_name='明星CPS佣金')
    gender = models.CharField(max_length = 1, choices = GENDER_STATUS, default = 'C', verbose_name='性别')
    create_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='创建者')
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='创建时间')

    class Meta:
        db_table = 't_star'
        verbose_name = '明星'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

#########################################################################  明星库 直播平台 个过滤分类
class StarZhiCategory(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')

    class Meta:
        db_table = 't_star_zhicategory'
        verbose_name = '基础数据-明星直播的分类 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class StarZhiFansNum(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')

    class Meta:
        db_table = 't_star_zhifansnum'
        verbose_name = '基础数据-明星直播的粉丝数 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class StarZhiPrice(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')
    class Meta:
        db_table = 't_star_zhiprice'
        verbose_name = '基础数据-明星直播的参考报价 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class StarZhiArea(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')
    class Meta:
        db_table = 't_star_zhiarea'
        verbose_name = '基础数据-明星直播的地域 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

class StarZhiPlatForm(models.Model):
    sid = models.IntegerField(verbose_name='类型id')
    name = models.CharField(max_length=20, verbose_name='类型名称')
    class Meta:
        db_table = 't_star_zhipaltform'
        verbose_name = '基础数据-明星直播的平台 列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)
#########################################################################

# 明星直播信息
class StarZhibo(models.Model):
    CRED_STATUS = (
        ('A', '未认证'),
        ('B', '已认证'),
    )
    star = models.ForeignKey(Star, related_name = 'star_zhibo', verbose_name='明星')
    broadcast_platform = models.ForeignKey(StarZhiPlatForm,blank=True, null=True, verbose_name='直播平台', limit_choices_to={'sid__gt':0})       ##
    platform_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='明星在某直播平台中的id')
    url = models.URLField(max_length=255, blank=True, null=True, verbose_name='头像url链接')
    nickname = models.CharField(max_length=100, blank=True, null=True, verbose_name='直播平台中的昵称')
    is_credibility = models.CharField(max_length = 1, choices = CRED_STATUS, default = 'A', verbose_name='认证状态')
    area =  models.ForeignKey(StarZhiArea,blank=True, null=True, verbose_name='地域',limit_choices_to={'sid__gt':0})     ##
    category =  models.ForeignKey(StarZhiCategory,blank=True, null=True, verbose_name='分类',limit_choices_to={'sid__gt':0})     ##

    fans_num = models.IntegerField(blank=True, null=True, verbose_name='粉丝数')
    average_num  = models.IntegerField(blank=True, null=True, verbose_name='平均观看数')
    reads_num = models.IntegerField(blank=True, null=True, verbose_name='订阅量')

    export_price = models.FloatField(blank=True, null=True, verbose_name='口头播放价格')
    ad_implants_price = models.FloatField(blank=True, null=True, verbose_name='商品植入价格')
    brand_exposed_price = models.FloatField(blank=True, null=True, verbose_name='品牌漏出价格')

    memo = models.TextField(max_length=255, blank=True, null=True, verbose_name='备注')
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='修改时间')

    class Meta:
        db_table = 't_star_zhibo'
        verbose_name = '明星直播信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s -- %s" % (self.broadcast_platform, self.platform_id)


##################################################################################################################################################
# 明星微信信息
class StarWeixin(models.Model):
    star = models.ForeignKey(Star)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='微信名')
    weixinid = models.CharField(max_length=100, blank=True, null=True, verbose_name='微信id')
    fans_num = models.IntegerField(blank=True, null=True, verbose_name='粉丝数')
    price = models.FloatField(blank=True, null=True, verbose_name='价格')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')
    memo = models.CharField(max_length=11, blank=True, null=True, verbose_name='备注')

    class Meta:
        db_table = 't_star_weixin'
        verbose_name = '明星微信信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

# 明星微博信息
class StarWeibo(models.Model):
    star = models.ForeignKey(Star)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='微博名称')
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name='微博地址')
    fans_num = models.IntegerField(blank=True, null=True, verbose_name='粉丝数')
    price = models.FloatField(blank=True, null=True, verbose_name='价格')
    memo = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    class Meta:
        db_table = 't_star_weibo'
        verbose_name = '明星微博信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)