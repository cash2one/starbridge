from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import ListView
from myapps.finance.models import  *
from datetime import datetime
from django.db.models import Q
from django.core import serializers
from django.forms.models import model_to_dict   #将单个对象转换成json
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from textwrap import wrap
# Create your views here.
class FinancePageView(ListView):
    #消费记录明细里的时间ajax刷新
    '''消费记录明细里面，根据下拉框里面的值和时间过滤出符合条件的数据'''
    def ajax_f(request):
        datedata = request.GET.get('type','')
        a = datedata[:10]
        b = datedata[-10:]+'/23/59/59'
        c = datetime.strptime(a, '%Y-%m-%d')
        d = datetime.strptime(b,'%Y-%m-%d/%H/%M/%S')
        now_user = request.user
        now_user_count =CustomUser.objects.filter(username=now_user).count()
        if now_user_count != 0:
            throw_data = Expenses.objects.filter(type='B').filter(time__gte=c).filter(time__lte=d).filter(user=now_user)##.values('time','order_id','number','amount','Balance')
            prepaid_data = Expenses.objects.filter(type='A').filter(time__gte=c).filter(time__lte=d).filter(user=now_user)##.values('time','order_id','number','amount','Balance')

        else:
            throw_data = Expenses.objects.filter(type='B').filter(time__gte=c).filter(time__lte=d)##.values('time','order_id','number','amount','Balance')
            prepaid_data = Expenses.objects.filter(type='A').filter(time__gte=c).filter(time__lte=d)##.values('time','order_id','number','amount','Balance')

        jsondata1=[ model_to_dict(i) for i in throw_data]
        jsondata2=[model_to_dict(i) for i in prepaid_data]
        
        context={'throw_data':jsondata1,'prepaid_data':jsondata2}
        return JsonResponse(context)
    '''根据退款记录里下拉框的值，和日期过滤出符合条件的数值，并用json格式返回去'''
    def ajax_chaxun(request):
        now_user = request.user
        query_date= request.GET.get('chaxun-date','')
        operate=request.GET.get('caozuo','')
        a = query_date[:10]
        b = query_date[-10:]+'/23/59/59'
        c = datetime.strptime(a, '%Y-%m-%d')
        d = datetime.strptime(b,'%Y-%m-%d/%H/%M/%S')
        sql_user=CustomUser.objects.filter(username=now_user).count()
        if operate=='0':
            if sql_user == 0:
                refund_data=Refund.objects.filter(type='A').filter(time__gte=c).filter(time__lte=d)
            else:
                refund_data=Refund.objects.filter(type='A').filter(time__gte=c).filter(time__lte=d).filter(user=now_user)
        else:
            if sql_user == 0:
                refund_data=Refund.objects.filter(type='B').filter(time__gte=c).filter(time__lte=d)
            else:
                 refund_data=Refund.objects.filter(type='B').filter(time__gte=c).filter(time__lte=d).filter(user=now_user)
        testdata=[model_to_dict(i) for i in refund_data]
        context={'refund_data':testdata}
        return JsonResponse(context)


    '''这个方法主要是为了展示财务报表页面的余额数据，判断当前登录用户是否在数据库中，如果不在的话，就余额为0，否则取出当前
    用户在数据库中的余额数据。      //// 因为现在已经加上了，如果没有用户登录，会重定向到登录界面，所以，下面的if else其实
    已经不需要进行判断了，直接取出登录用户在数据库里的值就好了'''
    @login_required
    def list_finance(request):
        #获得当前用户
        now_user=request.user
        sql_user=CustomUser.objects.filter(username=now_user).count()
        if sql_user == 0:
            balance_money= 0
            recharge_data=Recharge.objects.filter()
            refund_data = Refund.objects.filter()
        else:
            now_userid = request.user.id
            balance_count = Expenses.objects.filter(user_id=now_userid).count()
            if balance_count == 0:
                balance_money = 0
            else:
            #资金管理中的余额
                balance_object = Expenses.objects.filter(user_id=now_userid).last()
                ''' 下面的for循环主要是为了让显示的余额标准显示'''
                # for key,value in balance_data.items():
                balance_data = balance_object.Balance
                balance_money=",".join(wrap(str(balance_data)[::-1],3))[::-1]
            '''充值汇款数据  充值汇款里的查看汇款记录里面，展示的数据应该是当前登录用户的数据，故，应该判断当前登录用户，
            并获取当前登录用户录入的数据'''
            recharge_data=Recharge.objects.filter(user=now_user)
            refund_data = Refund.objects.filter(user=now_user)
            # #发票信息数据
            # invoice_data = Invoice.objects.values('time','name','amount','application_time','tracking_number','status')
            #财务报表数据
        content = {
            'active_menu': '财务报表',
            'balance_money': balance_money,
            'recharge_data': recharge_data,
            'refund_data': refund_data,
            # 'invoice_data': invoice_data,
        }
        return render(request,'finance/finance.html',content)


'''定义一个充值汇款的类,把用户在页面上输入的数据存放在数据库中'''
class RechargeMoney(ListView):
    #充值汇款信息
    def remitmoney(request):
        now_userid = request.user
        if request.method == 'POST':
            #汇款信息
            recharge_money = Recharge(
                user=now_userid,                                    # 登录账户
                name=request.POST.get('for-name', ''),              # 开户名称
                amount=request.POST.get('for-mon', ''),             # 充值金额
                to_account=request.POST.get('for-pay', ''),         # 支付账号
                # type=request.POST.get('for-way', ''),             # 充值方式
                type='A',
                bank_info=request.POST.get('for-info', ''),         # 银行信息
                branch_info=request.POST.get('for-add',''),         # 支行信息
                time=datetime.now()
            )
            recharge_money.save()
        return redirect("finance")


#申请退款
class RefundMoney(ListView):
    def refundmoney(request):
        now_userid = request.user
        if request.method == 'POST':
            #汇款信息
            refund_money = Refund(
                user=now_userid,                                    # 登录账户
                amount=request.POST.get('for-num', ''),             # 退款金额
                # type=request.POST.get('for-way', ''),               # 退款方式
                type='A',                                           # 退款方式
                name=request.POST.get('for-name', ''),              # 开户名称
                account=request.POST.get('for-mon', ''),            # 银行账号
                bank_info=request.POST.get('for-bank', ''),         # 银行信息
                branch_info=request.POST.get('for-add', ''),        # 支行信息
                info=request.POST.get('for-text', ''),              #退款说明
                time=datetime.now()
            )
            refund_money.save()
        return redirect("finance")


