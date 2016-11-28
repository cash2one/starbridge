from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from myapps.activity.models import  *
from myapps.report.models import  Report
from datetime import datetime
import xlwt
from myapps.report.paginator import list_page
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
class ReportPageView(ListView):
    ''' 展现数据报表首页的数据，首先把活动数据取出来完，然后在根据时间，关键字和活动名称为条件过滤出符合条件的数据'''
    @login_required
    def list_view(request):
        activity_list = Activity.objects.all()
        type = request.GET.get("type", "")            # 得到前端的活动名称
        key = request.GET.get("key","")               # 得到前端输入的关键字
        timereport = request.GET.get("time","")       # 得到前端传过来的日期值
        '''对下拉框里的值和关键字以及日期进行判断，并取出相应的值'''
        if timereport != '':
            get_time = request.GET.get('time')
            print(get_time)
            a = timereport[:10]
            # b = timereport[-10:]+'/23/59/59'
            b = timereport[13:23]+'/23/59/59'
            c = datetime.strptime(a, '%Y-%m-%d')
            d = datetime.strptime(b,'%Y-%m-%d/%H/%M/%S')
            '''如果传过来的活动名称是0的话，也就是没有选中固定的活动名称，则现在以时间和输入的关键字进行判断'''
            if type == '0':
                if key != '':
                    activity_list=Activity.objects.filter(start_date__gte=c).filter(start_date__lte=d).filter(name__contains=key)
                else:
                    activity_list=Activity.objects.filter(start_date__gte=c).filter(start_date__lte=d)

            else:
                if key != '':
                    activity_list = Activity.objects.filter(start_date__gte=c).filter(start_date__lte=d).filter(id__contains=key)
                else:
                    activity_list = Activity.objects.filter(start_date__gte=c).filter(start_date__lte=d)
        '''对取出来的数据进行格式化，把数据按照想要的格式取出来'''
        activity_order_list=[]  #初始化包含有订单的活动数组
        for i in activity_list:
            orderlist = Order.objects.filter(activity__id__contains=i.id)
            order_list = []     #初始化活动内部的订单数组
            for o in orderlist:
                if Report.objects.filter(order_id=o.id).count()>0:
                    order_list.append({'order':o,'report':Report.objects.filter(order_id=o.id)[0],'celebritynum':OrderCelebrityShip.objects.filter(order_id=o.id).count(),'starnum':OrderStarShip.objects.filter(order_id=o.id).count()})
                else :
                    order_list.append({'order':o,'report':'','celebritynum':OrderCelebrityShip.objects.filter(order_id=o.id).count(),'starnum':OrderStarShip.objects.filter(order_id=o.id).count()})
            activity_order_list.append({'object':i,'list':order_list})   #组成包含有订单的 活动 数组
        #分页代码
        # pagination = list_page(request,activity_order_list)
        pagination = list_page(request,list=activity_order_list,display=5,after_range_num=3,bevor_range_num=2)
        getValue = '?type='+type+'&key='+key+'&time='+timereport

        content = {
            'active_menu': '数据报表',
            'query_category': getValue,
            # 'sum_data':activity_order_list,
            'type':type,
            'key':key,
            'timereport':timereport,
            'activity_list':pagination,
        }
        return render(request,'report/data_report.html',content)

    #导出excel表格数据
    def datainput(request):
        type = request.GET.get('activity','')
        key = request.GET.get('gjz','')
        timereport =request.GET.get('dateTime','')
        activity_list=Order.objects.all()
        if timereport != '':
            a = timereport[:10]
            b = timereport[-10:]+'/23/59/59'
            c = datetime.strptime(a, '%Y-%m-%d')
            d = datetime.strptime(b,'%Y-%m-%d/%H/%M/%S')
            if type == '0':
                if key != '':
                    activity_list=activity_list.filter(activity_id__start_date__gte=c).filter(activity_id__start_date__lte=d).filter(activity_id__name__contains=key).values_list( 'activity_id__name','name','start_time','end_time',
                                                 'report_order__zhibo_click','report_order__zhibo_read','report_order__zhibo_call',
                                               'activity_id__start_date','activity_id__end_date', 'activity_id__advertiser_name')
                else:
                    activity_list=activity_list.filter(activity_id__start_date__gte=c).filter(activity_id__start_date__lte=d).values_list('activity_id__name','name','start_time','end_time',
                                                 'report_order__zhibo_click','report_order__zhibo_read','report_order__zhibo_call',
                                                 'activity_id__start_date','activity_id__end_date','activity_id__advertiser_name')
            else:
                if key != '':
                    activity_list = activity_list.filter(activity_id__start_date__gte=c).filter(activity_id__start_date__lte=d).filter(activity_id__id__contains=key).values_list( 'activity_id__name','name','start_time','end_time',
                                                 'report_order__zhibo_click','report_order__zhibo_read','report_order__zhibo_call',
                                               'activity_id__start_date','activity_id__end_date', 'activity_id__advertiser_name')
                else:
                    activity_list =activity_list.filter(activity_id__start_date__gte=c).filter(activity_id__start_date__lte=d).values_list( 'activity_id__name','name','start_time','end_time',
                                                 'report_order__zhibo_click','report_order__zhibo_read','report_order__zhibo_call',
                                              'activity_id__start_date','activity_id__end_date',  'activity_id__advertiser_name')

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=reportdata.xls'  # 返回下载文件的名称(activity.xls)
        workbook = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
        mysheet = workbook.add_sheet(u'活动')  # 创建工作页
        rows=activity_list
        cols = 10#每行的列
        aaa = ['活动名称','订单名称','投放日期','结束日期','直播点击数','直播订阅量','直播访问量','开始时间','结束时间','广告主名称']  #表头名
        for c in range(len(aaa)):
            mysheet.write(0,c,aaa[c])
        for r in range(0, len(rows)):      #对行进行遍历
            for c in range(cols):          #对列进行遍历
                mysheet.write(r+1,c,str(rows[r][c]))
                response = HttpResponse(
                    content_type='application/vnd.ms-excel')  # 这里响应对象获得了一个特殊的mime类型,告诉浏览器这是个excel文件不是html
                response[
                    'Content-Disposition'] = 'attachment; filename=reportdata.xls'  # 这里响应对象获得了附加的Content-Disposition协议头,它含有excel文件的名称,文件名随意,当浏览器访问它时,会以"另存为"对话框中使用它.
                workbook.save(response)
        return response




'''
#定义数据报表模块，点击详情进行跳转
    def report_detail(request):
        report_id = request.GET.get('id','')
        #采用多表查询，把活动详情页面所需要的字段全部对应的取出来
        activity_data = Activity.objects.filter(id=report_id).values('name','start_date','end_date','activity_order__name'
                                                                     ,'advertiser_name','budget','create_time','id')

        print(activity_data)
        return render(request, 'report/ReportDetails.html',locals())

#定义数据报表模块进行点击查看进行跳转
    def click_views(request):
        return render(request, 'report/ReportOrderDetails.html')
'''