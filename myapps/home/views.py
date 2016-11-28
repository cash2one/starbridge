from django.shortcuts import render, HttpResponse,render_to_response
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from myapps.activity.models import Activity, Order
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from django.forms.models import model_to_dict
from django.core import serializers
from myapps.report.models import Report
from myapps.finance.models import  Expenses
from myapps.users.models import *
from textwrap import wrap
from django.contrib.auth.decorators import login_required

# Create your views here.
'''
class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
'''

'''当首页活动名称和时间都传递到后端，后端根据名称和时间进行过滤查询。如果没有选择具体的活动名称，而是按照默认的“活动名称”
这四个字，则只按照时间进行查询,最后把查询出来的数据以json格式传递给前端进行处理'''
class HomePageView(ListView):
    def ajax_a(request):
        homedate = request.GET.get("choose-date",'')   # 获得前端传过来的时间，是字符串格式
        btnName = request.GET.get("btn-name",'')       # 获得前端传过来的活动名称
        a = homedate[:10]                              # 把前端穿够了的时间进行切片，例如，传过来的2016-08-18 - 2016-08-18
        b = homedate[-10:]+'/23/59/59'                 # 则实际查询的是2016年8月18日凌晨到8月18日23时59分59秒的数据
        c = datetime.strptime(a, '%Y-%m-%d')           # 把字符串转换为时间格式
        d = datetime.strptime(b,'%Y-%m-%d/%H/%M/%S')

        '''定义一个公共的，可以被引用的函数，这样，if，else里面重复的while循环函数就可以直接调用这个函数解决。*arg
        表示任意多个无名参数，类型为tuple'''
        def konlist_append(*args):
            i = 0
            while i < lennum:
                konglist.append(activity_list[i])
                i = i + 1

        if btnName ==  '活动名称':
            '''根据时间把相关的数据用django的orm语句取出来'''
            lennum = Activity.objects.all().filter(create_time__gte=c).filter(create_time__lte=d).values().count()
            activity_list= Activity.objects.all().filter(create_time__gte=c).filter(create_time__lte=d).values()
            '''下面这个while循环，是为了把activity_list这个列表里面的数据追加到一个konglist里面,因为上面的activity_list是
            queryset类型，不能直接变成json类型，所以用下面while循环转成列表'''
            konglist=[]
            konlist_append(lennum,activity_list)
            # i = 0
            # while i < lennum:
            #     konglist.append(activity_list[i])
            #     i = i + 1

        else:
            lennum = Activity.objects.all().filter(name=btnName).filter(create_time__gte=c).filter(create_time__lte=d).values().count()
            activity_list = Activity.objects.all().filter(name=btnName).filter(create_time__gte=c).filter(create_time__lte=d).values()
            konglist=[]
            konlist_append(lennum,activity_list)
            # i = 0
            # while i < lennum:
            #     konglist.append(activity_list[i])
            #     i = i + 1
        context={'jsondata':konglist}
        return JsonResponse(context)

    '''展示首页显示的数据'''
    '''@login_required 装饰器是防止如果用户没有登陆而直接访问，加上该装饰器的话，如果没有登录，就会跳转到登陆界面'''
    @login_required
    def list_data(request):
        #好像用到了django管理器，查询到未审核的所有订单总和
        order_counts = Order.ray_objects.order_count()
        '''获取当前登录用户，并判断当前登录用户是否在数据库里面，如果不在数据库里面，则显示余额为0，否则，取得
        当前登录用户的id，然后取出登录用户余额'''
        now_user = request.user
        sql_user = CustomUser.objects.filter(username=now_user).count()
        if sql_user == 0:
            balance_money = 0
        else:
            now_userid = request.user.id
            '''处理金钱格式，让金钱格式以5,000,000这种格式显示，用了python自带的textwrap模块，把取得的金额转为字符串，然后
            把字符串进行反转，每三个插入一个逗号，然后在反转回去'''
            balance_count = Expenses.objects.filter(user_id=now_userid).count()
            if balance_count == 0:
                balance_money = 0
            else:
                balance_object = Expenses.objects.filter(user_id=now_userid).last()
                balance_data = balance_object.Balance
                # for key,value in balance_data.items():
                balance_money=",".join(wrap(str(balance_data)[::-1],3))[::-1]
        '''把这个数据传递给前端页面，然后前端页面处理，显示活动名称'''
        activity_list = Activity.objects.all()

        '''
        这个是为了让首页图形模式显示的数据变成从数据库动态取得数据，但此功能第一版不用

        #定义一个空的曝光数列表，并循环取出所有曝光数的值放在列表中
        exposure_list = []
        #定义一个新的点击数列表
        click_list = []
        #定义一个新的点击率列表
        clickrate_list = []
        # for a in exposure_data:
        #     exposure_list.append(int(a['memo']))
        #     click_list.append(int(a['create_user']))
        #     clickrate_list.append(float(a['update_user']))
        # exposure_list = json.dumps(exposure_list)
        # exposure_list=json.dumps({'exposure_list':exposure_list})
        '''

        content = {
            'active_menu': '首页',
            'order_count': order_counts,
            'activity_list': activity_list,
            # 'exposure_list': json.dumps(exposure_list),
            # 'click_list': json.dumps(click_list),
            # 'clickrate_list': json.dumps(clickrate_list),
            'balance_money': balance_money,
        }
        return render(request,'home/index.html',content)
