from django.db import models
from myapps.users.models import CustomUser
# Create your models here.

# 资金管理(汇款账号管理)
class Funds(models.Model):  ##OneToOneField  CustomUser CustomUser
    user = models.ForeignKey(CustomUser, verbose_name='财务相关的登录帐户')
    account = models.CharField(max_length=100, verbose_name='账号')
    name = models.CharField(max_length=100, verbose_name='账号名称')
    bank = models.CharField(max_length=100, verbose_name='开户银行')

    class Meta:
        db_table = 't_funds'
        verbose_name = '汇款账号管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

# 消费记录明细
class Expenses(models.Model):
    COST_TYPE = (
        ('A', '充值汇款'),
        ('B', '投放消费'),
        ('C', '退款'),
    )
    user = models.ForeignKey(CustomUser, verbose_name='财务相关的登录帐户')
    time = models.DateTimeField(blank=True, null=True, verbose_name='消费日期')
    order_id = models.IntegerField(verbose_name='订单id')
    number =  models.IntegerField(verbose_name='交易号')
    type = models.CharField(max_length = 1, choices = COST_TYPE, verbose_name='操作类型')
    amount = models.IntegerField(verbose_name='金额')
    Balance = models.IntegerField(verbose_name='余额')
    class Meta:
        db_table = 't_expenses'
        verbose_name = '消费记录'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.order_id)

# 充值汇款
class Recharge(models.Model):
    RECHARGE_TYPE = (
        ('A', "汇款转账"),
        ('B',"支付宝"),
        # ('C', ''),
    )
    user = models.ForeignKey(CustomUser, verbose_name='财务相关的登录帐户')
    time = models.DateTimeField(blank=True, null=True, verbose_name='充值时间')
    name = models.CharField(max_length=100, verbose_name='开户名称')
    # user = models.CharField(max_length=100, verbose_name='登陆账号')
    from_account = models.CharField(max_length=100, verbose_name='汇款账号')
    to_account = models.CharField(max_length=100, verbose_name='支付账号')
    amount = models.IntegerField(verbose_name='充值金额')
    type =  models.CharField(max_length = 1, choices = RECHARGE_TYPE, verbose_name='充值方式')
    bank_info = models.CharField(max_length=100, verbose_name='银行信息')
    branch_info = models.CharField(max_length=100, verbose_name='支行信息')

    class Meta:
        db_table = 't_recharge'
        verbose_name = '充值汇款'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)
    @property
    def type_(self):
        return self.get_type_display()

# 退款记录
class Refund(models.Model):
    REFUND_TYPE = (
        ('A', '汇款转账'),
        ('B', '支付宝'),
    )
    user = models.ForeignKey(CustomUser, verbose_name='财务相关的登录帐户')
    amount = models.IntegerField(verbose_name='退款金额')
    type = models.CharField(max_length = 1, choices = REFUND_TYPE, verbose_name='退款方式')
    name = models.CharField(max_length=100, verbose_name='开户名称')
    account = models.CharField(max_length=100, verbose_name='银行账号')
    bank_info = models.CharField(max_length=100, verbose_name='银行信息')
    branch_info = models.CharField(max_length=100, verbose_name='支行信息')
    info = models.CharField(max_length=100, verbose_name='退款说明')
    time = models.DateTimeField(blank=True, null=True, verbose_name='退款时间')
    class Meta:
        db_table = 't_refund'
        verbose_name = '退款记录'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)
    @property
    def type_(self):
        return self.get_type_display()

################################################################################################################################
# 发票信息
class Invoice(models.Model):
    INVOICE_STATUS = (
        ('A', '未审核'),
        ('B', '待审核'),
        ('C', '待付款'),
        ('D', '已付款'),
    )
    INVOICE_TYPE = (
        ('A', '普通发票'),
        ('B', '增值税发票'),
    )
    user = models.ForeignKey(CustomUser, verbose_name='财务相关的登录帐户')
    time = models.DateTimeField(blank=True, null=True, verbose_name='日期')
    name = models.CharField(max_length=255, verbose_name='发票抬头')
    address = models.CharField(max_length=255, verbose_name='配送地址')
    amount = models.IntegerField(verbose_name='发票金额')
    application_time = models.DateTimeField(blank=True, null=True, verbose_name='申请时间')
    tracking_number = models.CharField(max_length=255, verbose_name='快递单号')
    status = models.CharField(max_length = 1, choices = INVOICE_STATUS, verbose_name='发票状态')
    type = models.CharField(max_length = 1, choices = INVOICE_TYPE, verbose_name='发票类型')
    content = models.CharField(max_length=255, verbose_name='发票内容')

    class Meta:
        db_table = 't_invoice'
        verbose_name = '发票信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.name)

# 财务报表
class Financial(models.Model):
    ACCOUNT_TYPE = (
        ('A', '基本户'),
        ('B', '临时户'),
        ('C', '一般户'),
        ('D', '专用户'),
    )
    user = models.ForeignKey(CustomUser, verbose_name='财务相关的登录帐户')
    name = models.CharField(max_length=100, blank=True, null=True,  verbose_name='财务报表')
    time = models.DateTimeField(blank=True,null=True,verbose_name='日期')
    type = models.CharField(max_length = 1, choices = ACCOUNT_TYPE,default = 'A', verbose_name='账户类型')
    lmonth_balance = models.CharField(max_length=100, blank=True, null=True, verbose_name='上月结余')
    tmonth_recharge = models.CharField(max_length=100, blank=True, null=True, verbose_name='本月充值')
    tmonth_consumption = models.CharField(max_length=100, blank=True, null=True, verbose_name='本月消耗')
    tmonth_balance = models.CharField(max_length=100, blank=True, null=True, verbose_name='本月结余')
    class Meta:
        db_table = 't_financial'
        verbose_name = '财务报表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s" % (self.user.name)