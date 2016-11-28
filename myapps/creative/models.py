from django.db import models

# Create your models here.

# 直播素材
class CreativeZhibo(models.Model):
    CREATIVE_STATUS = (
        ('A', '已上传'),
        ('B', '未上传'),

    )
    is_upload = models.CharField(max_length = 1, choices = CREATIVE_STATUS, default = 'B',verbose_name='素材上传状态')
    outer_url = models.URLField(max_length=255, blank=True, null=True, verbose_name='外链url')

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='直播名称')
    content = models.CharField(max_length=255, blank=True, null=True, verbose_name='口播广告内容')
    goods_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='植入商品名称')
    ##height_field='url_height', width_field='url_width'
    # 两个参数height_field和width_field指定的是两个字段，它们的作用是自动填充字段
    # 也就是说当上传图片后，它就会自动获取图片的高和宽，并存入url_height和url_width字段
    # url_height = models.PositiveIntegerField(default=75)
    # url_width = models.PositiveIntegerField(default=75)   ##height_field='url_height', width_field='url_width'
    goods_url = models.ImageField(upload_to='img_goods/%Y-%m-%d/%H-%M-%S/', verbose_name='植入商品图像的url',)  ##%H-%i-%s
    archive_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='压缩包url')
    memo = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    is_delete = models.IntegerField(default=0 ,blank=True, null=True, verbose_name='素材的删除状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间') ##  auto_now_add=True,为添加时的时间，更新对象时不会有变动。
    create_user = models.CharField(max_length=100, verbose_name='创建者')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间') ## auto_now=True,无论是你添加还是修改对象，时间为你添加或者修改的时间。
    update_user = models.CharField(max_length=100, verbose_name='修改者')
    class Meta:
        db_table = 't_creative_zhibo'
        verbose_name = '直播素材'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

    # 把状态字母在html显示为对应汉字
    @property
    def is_upload_(self):
        return self.get_is_upload_display()

# 红人or明星 素材关联表 <没用>
class StarOrCelebrityCreative(models.Model):
    RELATED_TYPE = (
        ('S', '明星'),
        ('C', '红人'),
    )
    creative_type = models.IntegerField(blank=True, null=True, verbose_name='素材类型')
    relate_type = models.CharField(max_length = 1, choices = RELATED_TYPE, verbose_name='类型--明星或者红人')
    star_or_celebrity_id = models.IntegerField(verbose_name='明星或者红人id')
    creative_id = models.IntegerField(blank=True, null=True, verbose_name='素材id')
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='创建时间')

    class Meta:
        db_table = 't_star_or_celebrity_creative'
        verbose_name = '红人或者明星 与素材的关联'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

################################################################################
# 微博素材
class CreativeWeibo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='微博素材名称')
    content = models.TextField(max_length=255, blank=True, null=True, verbose_name='微博文字内容')
    picture = models.CharField(max_length=255, blank=True, null=True, verbose_name='微博图片路径')
    goods_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品链接url')
    memo = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    create_user = models.CharField(max_length=100, verbose_name='创建者')
    create_time = models.DateTimeField(verbose_name='创建时间')

    class Meta:
        db_table = 't_creative_weibo'
        verbose_name = '微博素材'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

# 微信素材
class CreativeWeixin(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='微信标题')
    anthor = models.CharField(max_length=100, blank=True, null=True, verbose_name='微信作者')
    file_picture_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='封面图的url')
    content = models.TextField(max_length=255, blank=True, null=True, verbose_name='文字素材内容')
    create_user = models.IntegerField(blank=True, null=True, verbose_name='创建者')
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='创建时间')

    class Meta:
        db_table = 't_creative_weixin'
        verbose_name = '微信素材'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.title)
