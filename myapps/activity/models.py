from django.db import models

from myapps.celebrity.models import Celebrity
from myapps.star.models import Star
from myapps.creative.models import CreativeZhibo
# Create your models here.

# 活动
class Activity(models.Model):
    Activity_STATUS = (
        ('A', '待审核'),
        ('B', '待上传素材'),
        ('C', '已通过审核,待接单'),
        ('D', '已支付'),
        ('E', '投放中'),
        ('F', '投放结束,待接单'),
        ('G', '已结算'),
        ('H', '已关闭'),
    )

    name = models.CharField(max_length=100, verbose_name='活动名称')
    start_date = models.DateTimeField(verbose_name='开始时间')
    end_date = models.DateTimeField(verbose_name='结束时间')
    advertiser_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='广告主')
    budget = models.FloatField(verbose_name='总预算')
    memo = models.TextField(max_length=255, blank=True, null=True, verbose_name='备注')
    # agent_id = models.IntegerField(verbose_name='代理商') ##############################################
    activity_status = models.CharField(max_length = 1, choices = Activity_STATUS, default = 'A', verbose_name='活动状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  ##  auto_now_add=True,为添加时的时间，更新对象时不会有变动。
    create_user = models.CharField(max_length=100, blank=True, null=True,verbose_name='创建者')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')      ##  auto_now=True,无论是你添加还是修改对象，时间为你添加或者修改的时间。
    # update_time.editable=True
    update_user = models.CharField(max_length=100,blank=True, null=True, verbose_name='修改者')

    class Meta:
        db_table = 't_activity'
        verbose_name = '活动'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
    def __str__(self):
        return "%s" % (self.name)

    # 把活动状态字母在html显示为对应汉字
    @property
    def activity_status_(self):
        return self.get_activity_status_display()

# 订单
class Order(models.Model):  #状态
    ORDER_STATUS = (
        ('A', '未审核'),
        ('B', '待审核'),
        ('C', '待付款'),
        ('D', '已付款'),
        ('E', '已关闭'),
    )

    activity = models.ForeignKey(Activity, related_name = 'activity_order', verbose_name='活动名称')   ## many to one 关系
    name = models.CharField(max_length=255, verbose_name='订单名称')
    status = models.CharField(max_length = 1, choices = ORDER_STATUS,  default = 'C', verbose_name='订单状态')
    start_time = models.DateTimeField(blank=True, null=True, verbose_name='订单投放开始时间')
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='订单投放结束时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单创建者')
    order_add_id = models.IntegerField(verbose_name='order_add 的id')
    order_pay = models.CharField(max_length=255, blank=True, null=True, verbose_name='订单报价总价支付金额')
    class RAYManager(models.Manager):   #  创建管理器类，可以更好地进行封装功能和重用代码。
    # 增加一个方法order_count()  增加额外的管理器方法
        def order_count(self):
            return self.filter(status__exact='A').count()
    objects = models.Manager()  # 默认的管理器
    ray_objects = RAYManager()  # 自定义的管理器，用新变量

    class Meta:
        db_table = 't_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)
    #把状态字母在html显示为对应汉字
    @property
    def status_(self):
        return self.get_status_display()

# 排期
class Flighting(models.Model):
    # order = models.ForeignKey(Order, verbose_name='订单')
    custom_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='选择时间')   ##	逗号分隔
    plat =  models.CharField(max_length=255, blank=True, null=True, verbose_name='选择平台')         ##  逗号分割
    start_time = models.CharField(max_length=100, blank=True, null=True, verbose_name='自定义排期开始时间')
    end_time = models.CharField(max_length=100, blank=True, null=True, verbose_name='自定义排期结束时间')
    creative = models.ForeignKey(CreativeZhibo, verbose_name='素材',blank=True, null=True,)   ## many to one 关系

    class Meta:
        db_table = 't_flighting'
        verbose_name = '排期'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % self.creative.name

# 佣金表  最后一个存
# class Commission(models.Model):
#     content = models.CommaSeparatedIntegerField(max_length=255, blank=True, null=True, verbose_name='粉丝量-保底佣金') # 逗号分隔
#     cps = models.CharField(max_length=255,blank=True, null=True, verbose_name='CPS') # cps
#     # order_add_sid = models.CharField(max_length=255,blank=True, null=True, verbose_name='关联的订单附加表的编号')
#     class Meta:
#         db_table = 't_commission'
#         verbose_name = '佣金'
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return "%s" % (self.order_sid)

# 创建订单附加的order_add表
class Order_add(models.Model):
    # order_add_sid = models.IntegerField(verbose_name='order_add 表的sid')
    ordername = models.CharField(max_length=255, blank=True, null=True, verbose_name='订单名称')
    ordertimepre = models.DateTimeField(blank=True, null=True, verbose_name='自定义排期开始时间')
    ordertimenext = models.DateTimeField(blank=True, null=True, verbose_name='自定义排期结束时间')

    content = models.CharField(max_length=255, blank=True, null=True, verbose_name='粉丝量-保底佣金') # 逗号分隔
    cps = models.CharField(max_length=255,blank=True, null=True, verbose_name='CPS') # cps
    # commission = models.ForeignKey(Commission, verbose_name='佣金') #commission
    # flighting = models.ForeignKey(Flighting, verbose_name='排期') # 投放日期,自定义时间,投放平台
    activity_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='活动ID')  # 活动id存入Activity
    celebrityzhibo_id = models.CommaSeparatedIntegerField(max_length=255, blank=True, null=True, verbose_name='网红直播信息')  # 已选红人直播ID
    starzhibo_id = models.CommaSeparatedIntegerField(max_length=255, blank=True, null=True, verbose_name='明星直播信息')  # 已选明星直播ID
    creativezhibo_id = models.CommaSeparatedIntegerField(max_length=255, blank=True, null=True, verbose_name='直播素材的id 集合')
    class Meta:
        db_table = 't_order_add'
        verbose_name = '订单附加表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.id)

################################################################################
# 订单和红人关联表
class OrderCelebrityShip(models.Model):
    order = models.ForeignKey(Order, verbose_name='订单')
    celebrity = models.ForeignKey(Celebrity, verbose_name='红人')
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='记录创建时间')

    class Meta:
        db_table = 't_order_celebrity'
        verbose_name = '订单与 红人的关联'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s -- %s" % (self.order.name, self.celebrity.name)

# 订单和明星关联表
class OrderStarShip(models.Model):
    order = models.ForeignKey(Order, verbose_name='订单')
    star = models.ForeignKey(Star, verbose_name='明星')
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='记录创建时间')

    class Meta:
        db_table = 't_order_star'
        verbose_name = '订单与 明星的关联'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s -- %s" % (self.order.name, self.star.name)


# class Activity(models.Model):
#
#     name = models.CharField(max_length=100, verbose_name="活动名称")  # 活动名称
#      start_date = models.DateTimeField()  # 开始时间
#     end_date = models.DateTimeField()  # 结束时间
#     advertiser_name = models.CharField()  # 广告主
#     budget = models.CharField()  # 总预算
#     memo = models.CharField()  # 备注
#     agent_id = models.IntegerField()  # 代理商
#     create_time = models.DateTimeField()  # 创建时间
#     create_user = models.IntegerField()  # 创建人
#     update_time = models.DateTimeField(auto_now_add=True)  # 修改时间  dateTime.datetime.strftime(‘%d/%m/%Y %H:%M‘)
#     update_user = models.IntegerField()  # 修改人
#
#     #可以直接赋值替换掉默认的objects管理器，也可以定义一个新的管理器变量
#     #调用时，直接使用这个新变量就可以了，一旦定义了新的管理器，默认管理器
#     #需要显示声明出来才可以使用
#     objects = models.Manager()  # 默认的管理器
#     ray_objects = RAYManager()  # 自定义的管理器，用新变量
#
#     def __str__(self):
#         return "%s" % self.name
#
#
# class RAYManager(models.Manager):   #  创建管理器类，可以更好地进行封装功能和重用代码。
#     # 增加一个方法name_count()  增加额外的管理器方法
#     def name_count(self, keyword):
#         return self.filter(name__icontains=keyword).count()
#     # 修改管理器返回的QuerySet
#     # 调用父类的方法 在原来返回的QuerySet的基础上返回新的QuerySet
#
#     def get_query_set(self):
#         return super(RAYManager, self).get_query_set().filter(name__icontains='xxx')
"""
operators = {

        'exact': '= %s',
        'iexact': 'LIKE %s',
        'contains': 'LIKE BINARY %s',
        'icontains': 'LIKE %s',
        'regex': 'REGEXP BINARY %s',
        'iregex': 'REGEXP %s',
        'gt': '> %s',
        'gte': '>= %s',
        'lt': '< %s',
        'lte': '<= %s',
        'startswith': 'LIKE BINARY %s',
        'endswith': 'LIKE BINARY %s',
        'istartswith': 'LIKE %s',
        'iendswith': 'LIKE %s',
    }

"""