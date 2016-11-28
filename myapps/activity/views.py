from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import ListView
from myapps.activity.models import *
from myapps.creative.models import *
from myapps.users.models import *
from myapps.finance.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt ##包装csrf请求，避免django认为其实跨站攻击脚本
import xlwt
from myapps.activity.helpers import *
import re
from datetime import datetime
from myapps.report.paginator import list_page
import random
from myapps.activity.activityshow import activityshow
# Create your views here.

class ActivityPageView(ListView):
    # 活动首页展示
    def activity(request):
        activity_list = Activity.objects.all().order_by('-update_time')
        # 引用activityshow.py文件里的activityshow方法
        activity_order_list=activityshow(request,activity_list)
        # 分页代码
        page_range =list_page(request,list=activity_order_list,display=5,after_range_num=3,bevor_range_num=2)
        content = {
            'active_menu': '活动管理',
            'page_range': page_range,
            }
        return render(request,'activity/activeManagement.html',content)

    # 多条件查询
    def queryactivity(request):
        # 获取搜索的关键字
        if request.method == 'GET':
            actname = request.GET.get('name', '')                       ##活动名称
            start_dates = request.GET.get('start_date', '')            ##活动开始时间
            end_dates = request.GET.get('end_date', '')                ##活动结束时间
            activity_status = request.GET.get('activity_status', '')   ##活动状态
        ##活动时间格式处理
        enddates = end_dates + '/23/59/59'
        start_date = datetime.strptime(start_dates, '%Y-%m-%d')
        end_date = datetime.strptime(enddates, '%Y-%m-%d/%H/%M/%S')
        ##活动信息以修改时间进行排序
        activity_list = Activity.objects.all().order_by('-update_time')
        ##活动名称
        if actname != '':
            activity_list = activity_list.filter(name__contains=actname)
        ##活动状态
        if activity_status != '' and activity_status != '0':
            activity_list = activity_list.filter(activity_status__contains=activity_status)
        ##活动日期
        if start_date != '' and end_date != '':
            activity_list = activity_list.filter(start_date__gte=start_date).filter(end_date__lt=end_date)
        activity_order_list = activityshow(request,activity_list)
        # 分页代码
        getValue='&actname='+actname+'&start_date='+start_dates+'&end_date='+end_dates+'&activity_status='+activity_status
        page_range =list_page(request,list=activity_order_list,display=5,after_range_num=3,bevor_range_num=2)
        content = {
            'active_menu': '活动管理',
            'actname': actname,
            'start_dates': start_dates,
            'end_dates': end_dates,
            'actstatus': activity_status,
            'page_range': page_range,
            'getValue':getValue,
        }
        return render(request, 'activity/activeManagement.html', content)

    # 活动详情
    def acitve_detail(request):
        activity_id = request.GET.get('id', '')
        order_list = Order.objects.filter(activity__id__contains=activity_id) #订单数量
        if activity_id == '':
            return HttpResponseRedirect(reversed("activity"))
        try:
            activity_list = Activity.objects.get(pk=activity_id)
        except Activity.DoesNotExist:
            return HttpResponseRedirect(reversed("activity"))
        content = {
            'activity_list': activity_list,
            'order_list': order_list,
        }
        return render(request, 'activity/activeDetails.html', content)
    # 订单详情
    def order_details(request):
        order_id = request.GET.get('id', '')
        if order_id == '':
            return HttpResponseRedirect(reversed("activity"))
        try:
            activityid = Order.objects.filter(pk=order_id).values('activity_id')[0]['activity_id']
            ordersome = Order.objects.filter(activity_id=activityid).count() # 该活动有几个订单
            activitydatas = Activity.objects.filter(pk=activityid) # 根据活动的ID查询信息
            orderlists = Order.objects.filter(pk=order_id) # 根据订单ID查询信息
            order_addid = Order.objects.filter(pk=order_id).values('order_add_id')[0]['order_add_id']  # 根据订单ID获取中间表的ID
            createzhibo_id = Order_add.objects.filter(pk=order_addid).values('creativezhibo_id')[0]['creativezhibo_id']  # 素材直播ID
            createzhibo_mid= createzhibo_id.split(',')
            createzhiboarray = []
            for i in createzhibo_mid:
                createzhiboarray.append(re.findall(r'(\w*[0-9]+)\w*',i))

            flightingplatform = []
            create_zhibo = []
            for createid in createzhiboarray[0]:
                flightingplatform.append(Flighting.objects.filter(creative_id=createid)[0])  # 投放排期
                create_zhibo.append(CreativeZhibo.objects.filter(pk=createid) ) # 素材信息

            cps = Order_add.objects.filter(pk=order_addid).values('cps')[0]['cps']
            ##已选红人直播信息
            celebrityids = Order_add.objects.filter(pk=order_addid).values('celebrityzhibo_id')[0]['celebrityzhibo_id']
            celebids = celebrityids.split(',')
            ##已选红人id长度个数
            celebritycount = len(celebids)
            ##已选红人ID
            celebrityidarray = []
            ##已选红人查询后的信息
            celebritys = []
            for celid in celebids:
                celebrityidarray.append(re.findall(r'(\w*[0-9]+)\w*',celid))
            ## 已选红人直播信息
            for celeids in celebrityidarray:
                for cids in celeids:
                    celebritys.append(CelebrityZhibo.objects.filter(pk=cids)[0])
            ## 粉丝佣金量
            fanscomms = Order_add.objects.filter(pk=order_addid).values('content')[0]['content']
            comms = []
            commissions = fanscomms.split(',')
            for commission in commissions:
                if commission != '':
                    comms.append(commission.split('-'))
        except Order.DoesNotExist:
            return HttpResponseRedirect(reversed("activity"))
        content = {
            'order_list': orderlists,
            'activitylists': activitydatas,
            'ordersome': ordersome,
            'flightingplatform': flightingplatform,
            'celebritycount': celebritycount,
            'celebritys': celebritys,
            'cps': cps,
            'commission':comms,
            'create_zhibo': create_zhibo,
        }
        return render(request,'activity/activeOrderDetails.html', content)

    # 创建活动订单1
    def create_order1(request):
        # 引用helpers.py中的create_zhibo_order方法
        content = create_zhibo_order(request)
        return render(request, 'activity/creatingOrder.html',content)

    # 创建活动订单2
    def create_order2(request):
        if request.method == 'POST':
            activitysid = request.POST.get("activityid")                            # 活动ID
            activitylists = Activity.objects.get(pk=activitysid)                    # 活动信息
            scheduleids = request.POST.get("nextmaterialid")
            schedule_ids = []
            for i in scheduleids.split(','):
                schedule_ids.append(i)                                              # 截取后的红人ID
            schedulealls = []
            for sch_id in schedule_ids:                                             # 遍历之后的已选红人ID
                schedulealls.append(CelebrityZhibo.objects.filter(pk=sch_id).values('broadcast_platform__name')[0]['broadcast_platform__name']) # 已选红人ID查询外键中的平台名称

            schedulealls = list(set(schedulealls))                                  # 红人投放平台去重



            zhibo_list = CreativeZhibo.objects.filter(is_delete=0)                  # 直播素材全部信息

            # 用户输入的订单信息需要传递到保持页面
            ordername = request.POST.get("ordername")                               # 用户输入的订单名称
            ordertimepre = request.POST.get("ordertimepre")                         # 用户输入的订单投放开始日期
            ordertimenext = request.POST.get("ordertimenext")                       # 用户输入的订单投放结束日期

            content = {
                'activitysid': activitysid,                                         # 活动信息ID
                'scheduleid': scheduleids,                                          # 已选红人ID
                'ordername': ordername,                                             # 用户输入的订单名称
                'ordertimepre': ordertimepre,                                       # 用户输入的订单投放开始日期
                'ordertimenext': ordertimenext,                                     # 用户输入的订单投放结束日期
                'activitylists': activitylists,                                     # 根据活动id获取活动信息
                'zhibo_list':zhibo_list,                                            # 直播素材全部信息
                'schedulealls': schedulealls,                                       # 已选红人平台信息
            }
        return render(request, 'activity/creatingOrder2.html', content)

    ## 创建活动订单3
    def create_order3(request):
        activitysid = request.GET.get("id")                                         # 活动ID
        activitylists = Activity.objects.get(pk=activitysid)                        # 活动信息
        cps = request.POST.get('cps')                                               # cps
        createsflightings = request.POST.get('sucai')                               # 素材排期
        createsflightingsStr = eval(createsflightings)
        if len(createsflightingsStr) > 0:# 弹窗中填写的信息对象
            creative_arr = []   #素材数组初始化
            platform_date = []  # 投放日期数组

            creative_zhibos = []
            creative_ids = []
            creative_id = ''  # 初始化素材ID
            for f in createsflightingsStr:
                sucaiid = f['sucai_content']['id'] #获取素材id
                links = f['sucai_content']['link'] #获取外部链接
                if links == '' or links == None:
                    linksnew = ''
                else:
                    linksnew = links
                numbers = str(random.randrange(0, 9999))
                #素材库选取的素材ID不为空
                if sucaiid != '':
                    goods_urls = CreativeZhibo.objects.filter(pk=sucaiid).values('goods_url')[0]['goods_url'] #查询goods_url状态
                    # A:已上传; B:未上传
                    #如果外部链接(links)为空且植入商品图像的url(goods_urls)为空
                    if goods_urls == '':
                        creativezhibo = CreativeZhibo.objects.filter(pk=sucaiid)[0]
                        creativezhibo.outer_url=linksnew
                        creativezhibo.save()
                        creative_id = creativezhibo.pk
                        creative_ids.append(creative_id)
                        creative_zhibos.append(creativezhibo)
                    elif goods_urls !='': #goods_urls不为空时,把原有的素材id加到初始化素材ID数组里
                        creativezhibo = CreativeZhibo.objects.filter(pk=sucaiid)[0]
                        creativezhibo.outer_url = linksnew
                        creativezhibo.save()
                        creative_id = creativezhibo.pk
                        creative_ids.append(creative_id)
                        creative_zhibos.append(creativezhibo)
                else:
                    if links !='':
                        creativezhibo = CreativeZhibo.objects.create(name='素材'+numbers, outer_url=links)
                        creative_id = creativezhibo.pk
                        creative_ids.append(creative_id)
                        creative_zhibos.append(creativezhibo)
                    else:
                        creativezhibo = CreativeZhibo.objects.create(name='素材'+numbers)
                        creative_id = creativezhibo.pk
                        creative_ids.append(creative_id)
                        creative_zhibos.append(creativezhibo)


                for flightings in f['sucai_content']['paiqi']:
                    custom_times = flightings['data']  #截取|后的选择时间
                    custom_timesave = custom_times.split('|')
                    platform_date.append(custom_timesave)            #把custom_time加到platform_date数组
                    times = flightings['time'].split('-') #截取时间为['11:12','12:21']格式
                    timesfirst = times[0] #取集合第一个值
                    timelast = times[1] #取集合第二个
                    plats = flightings['pingtai']# 投放平台
                    # 排期传递的参数存到表中
                    flightings = Flighting(
                        custom_time=custom_times,                                   # 选择时间
                        start_time=timesfirst,                                      # 自定义排期开始时间
                        end_time=timelast,                                          # 自定义排期结束时间
                        creative_id=creative_id,                                    # 已创建素材ID
                        plat=plats,                                                 # 选择的直播平台
                    )
                    flightings.save()
            creative_arr.append(platform_date)
        #已选红人直播信息
        celebrityreids =request.POST.get("scheduleid")
        celebrityids = celebrityreids.split(',')                     # 已选的红人ID
        celebrityalls = []
        # 截取后的红人ID
        celebrity_ids = []
        for i in celebrityids:
            celebrity_ids.append(i)

        celebritycount = len(celebrity_ids)                                           # 已选红人个数
        for cele_id in celebrity_ids:                                                 # 遍历之后的已选红人ID
            celebrityalls.append(CelebrityZhibo.objects.filter(pk=cele_id))              # 已选红人ID查询的信息

        fansnum = request.POST.get('fansnum')                                       # 粉丝量,佣金总数
        comms = []
        commissions= fansnum.split(',')
        for commission in commissions:
            if commission != '':
                comms.append(commission.split('-'))

        # 用户输入的订单信息
        ordername = request.POST.get("ordername")                                   # 用户输入的订单名称
        ordertimepre = request.POST.get("ordertimepre")                             # 用户输入的订单投放开始日期
        ordertimenext = request.POST.get("ordertimenext")                           # 用户输入的订单投放结束日期

        ##创建迭代器
        creative_idsiter = iter(creative_ids)
        for creatids in creative_idsiter:
            # 创建订单附加的order_add表
            order_add = Order_add(
                cps=cps,                                                                # cps
                content=fansnum,                                                        # 佣金内容,粉丝量
                activity_id=activitysid,                                                # 活动ID
                celebrityzhibo_id=celebrityreids,                                        # 已选红人ID
                creativezhibo_id=creatids,                                              # 已创建素材ID
                # ordername=ordername,                                                    # 用户输入的订单名称
                # ordertimepre=ordertimepre,                                              # 用户输入的订单投放开始日期
                # ordertimenext=ordertimenext,                                            # 用户输入的订单投放结束日期

            )
            order_add.save()
            order_add_id = order_add.pk                                                 # 中间表的ID

        content = {
            'activitylists': activitylists,                                         # 活动信息
            'order_add_id': order_add_id,                                           # 中间表的ID
            'ordername': ordername,                                                 # 用户输入的订单名称
            'ordertimepre': ordertimepre,                                           # 用户输入的订单投放开始日期
            'ordertimenext': ordertimenext,                                         # 用户输入的订单投放结束日期
            'cps': cps,                                                             # cps
            'schedule_ids':celebrity_ids,                                            # 已选红人ID
            'celecount': celebritycount,                                         # 已选红人几个
            'celebrityalls': celebrityalls,                                                 # 已选红人ID查询的信息
            'commission': comms,                                                    # 粉丝量保低佣金
            'creative_arr': creative_arr,                                           # 素材排期
            'sch_id': cele_id,                                                       # 遍历之后的已选红人ID
            'creative_zhibos': creative_zhibos,                                     # 素材信息
        }
        return render(request, 'activity/creatingOrder3.html', content)

    # 保存订单前素材上传
    @csrf_exempt
    def upload_goods_url(request):
        creativeid = request.POST.get('id')  # 上传素材id
        goods_url = request.FILES.get('goods_url', '')  # 植入商品图像的url
        if goods_url != "":
            creative = CreativeZhibo.objects.get(pk=creativeid)
            creative.goods_url = goods_url
            creative.is_upload = 'A'  # 上传状态改为(A:已上传)
            creative.save()
        context = {'creativeid': creativeid}
        return JsonResponse(context)

    # 订单保存
    def save_order(request):
        activitysid = request.GET.get("id")
        order_add_ids = request.POST.get("order_add_id")
        ordernames = request.POST.get("ordername")
        starttime = request.POST.get("ordertimepre")
        endtime = request.POST.get("ordertimenext")
        sch_id = request.POST.get("sch_id")
        orderpays = request.POST.get("hiddentotally")
        new_user = request.user
        # 用户输入的订单信息
        order = Order(
            activity_id=activitysid,
            order_add_id= order_add_ids,                                            # 中间表id
            name= ordernames,                                                       # 用户输入的订单名称
            start_time = starttime,                                                 # 用户输入的订单投放开始日期
            end_time = endtime,                                                     # 用户输入的订单投放结束日期
            order_pay= orderpays,
            create_user= new_user,
        )
        order.save()
        return HttpResponseRedirect('/activity')


    #关闭活动状态
    def acitve_close(request):
        id = request.GET.get('id')
        act = Activity.objects.get(id=id)                                           # 得到该条数据所有字段
        act.activity_status = 'H'
        act.save()
        return HttpResponseRedirect('/activity')

    #只显示已选(创建表单1)-----待完成(zmb)
    def showchecked(request):
        celebritys_list_id = request.POST.get('materialid').split(',')
        print('截取的红人主播ID集合--->', celebritys_list_id)
        for celebritys_id in celebritys_list_id:
            celebritys = CelebrityZhibo.objects.get(pk=int(celebritys_id))
            # 改变红人直播信息显示状态,is_credibility(default='A') CRED_STATUS = (('A', '未认证'),('B', '已认证'),)
            celebritys.is_credibility.CRED_STATUS = 'B'
            celebritys.save()
        return HttpResponseRedirect('/createorder')

    #活动批量导出
    def exportactivity(request):
        actname = request.GET.get('name','')
        start_dates = request.GET.get('start_date','')
        end_dates = request.GET.get('end_date','')
        activity_status = request.GET.get('activity_status', '')

        enddates = end_dates + '/23/59/59'
        start_date = datetime.strptime(start_dates, '%Y-%m-%d')
        end_date = datetime.strptime(enddates, '%Y-%m-%d/%H/%M/%S')

        ##活动信息以修改时间进行排序
        activity_list = Activity.objects.all().order_by('-update_time')

        ##活动名称
        if actname != '':
            activity_list = activity_list.filter(name__contains=actname).values_list('id','name','start_date','end_date',
                                                                                     'advertiser_name','budget','memo',
                                                                                     'activity_status','create_time','create_user',
                                                                                     'update_time','update_user')
        ##活动状态
        if activity_status != '' and activity_status != '0':
            activity_list = activity_list.filter(activity_status__contains=activity_status).values_list('id','name','start_date','end_date',
                                                                                     'advertiser_name','budget','memo',
                                                                                     'activity_status','create_time','create_user',
                                                                                     'update_time','update_user')
        ##活动日期
        if start_date != '' and end_date != '':
            activity_list = activity_list.filter(start_date__gte=start_date).filter(end_date__lt=end_date).values_list('id','name','start_date','end_date',
                                                                                     'advertiser_name','budget','memo',
                                                                                     'activity_status','create_time','create_user',
                                                                                     'update_time','update_user')

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=activity.xls'  # 返回下载文件的名称(activity.xls)
        workbook = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
        mysheet = workbook.add_sheet(u'活动')  # 创建工作页
        rows = activity_list
        cols = 11  # 每行的列
        titlename = ['活动id', '活动名称', '开始时间', '结束时间', '广告主', '总预算', '备注', '活动状态', '创建时间', '创建者', '修改时间', '修改者']  # 表头名
        for cact in range(len(titlename)):
            mysheet.write(0, cact, titlename[cact])
        for ract in range(0, len(rows)):
            for cact in range(cols):
                mysheet.write(ract + 1, cact, str(rows[ract][cact]))
                response = HttpResponse(
                    content_type='application/vnd.ms-excel')  # 这里响应对象获得了一个特殊的mime类型,告诉浏览器这是个excel文件不是html
                response[
                    'Content-Disposition'] = 'attachment; filename=activity.xls'  # 这里响应对象获得了附加的Content-Disposition协议头,它含有excel文件的名称,文件名随意,当浏览器访问它时,会以"另存为"对话框中使用它.
                workbook.save(response)
        return response

    # 订单详情
    def orderdetails(request):
        return render(request, 'activity/activeOrderDetails.html')

class AddActivityView(ListView):
    #添加活动
    def addactivity(request):
        new_user = request.user
        if request.method == 'POST':
            new_activity = Activity(
                name=request.POST.get('name', ''),                      # 活动名称
                start_date=request.POST.get('start_date', ''),          # 开始时间
                end_date=request.POST.get('end_date', ''),              # 结束时间
                advertiser_name=request.POST.get('advertiser_name', ''),# 广告主
                budget=request.POST.get('budget', ''),                  # 总预算
                memo=request.POST.get('memo', ''),                      # 备注
                create_user=new_user,
                update_user=new_user,
            )
            new_activity.save()
            return HttpResponseRedirect('/activity')                    #重定向的活动管理展示页面
        return render(request, 'activity/creatingActivities.html')

    #修改活动
    def updateactivity(request):
        activity_id = request.GET.get('id', '')
        updateactivity = Activity.objects.get(pk=activity_id)
        return render(request, 'activity/activeDetailsChanges.html', {'updateAct': updateactivity})

    # 修改活动ID
    @csrf_exempt
    def updateactivity_ID(request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        advertiser_name = request.POST.get('advertiser_name')
        budget = request.POST.get('budget')
        create_time = request.POST.get('create_time')

        act = Activity.objects.get(pk=id)
        act.name = name
        act.start_date = start_date
        act.end_date = end_date
        act.advertiser_name = advertiser_name
        act.budget = budget
        act.create_time = create_time
        act.save()
        return HttpResponseRedirect('/activity')

    # 选择红人(明星)
    def choiceStar(request):
        activity_id = request.GET.get('id', '')  # 活动ID
        activity_lists = Activity.objects.get(pk=activity_id)

        content = {
            'activitylists': activity_lists,
        }
        return render(request, 'activity/creatingOrderStar.html',content)
    #充值付款
    def pay(request):
        orderid = request.GET.get('id')
        payall = Order.objects.filter(pk=orderid).values('order_pay')[0]['order_pay'] ##平台报价,实收款,支付金额
        now_userid = request.user.id
        try:
            balance_data = Expenses.objects.filter(user_id=now_userid).last()
            balance_money = balance_data.Balance
        except:
            balance_money = 0

        if orderid != '':
            #根据订单id查询出中间表的id
            order_add_id = Order.objects.filter(pk=orderid).values('order_add_id')
            # 直播素材ID
            creativezhibo = Order_add.objects.filter(pk=order_add_id)
            activityid = Order_add.objects.filter(pk=order_add_id).values('activity_id')[0]['activity_id']
            ##已选红人直播信息
            celebrityids = Order_add.objects.filter(pk=order_add_id).values('celebrityzhibo_id')[0]['celebrityzhibo_id']
            celebids = celebrityids.split(',')
            ##已选红人id长度个数
            celebritycount = len(celebids)
            activity_list = Activity.objects.filter(pk=activityid)
            try:
                create_zhibo_id = Order_add.objects.filter(pk=order_add_id).values('creativezhibo_id')[0]['creativezhibo_id']  # 素材直播ID
                create_zhibo_ids = re.findall(r'(\w*[0-9]+)\w*', create_zhibo_id)
                flightingplatform = []
                for createzhiboid in create_zhibo_ids:
                    flightingplatform.append(Flighting.objects.filter(creative_id=createzhiboid)[0])  # 投放排期
            except Flighting.DoesNotExist:
                return HttpResponseRedirect(reversed("activity"))
        content = {
            'activity': activity_list,
            'flightingplatform': flightingplatform,
            'balance_money': balance_money,
            'celebritycount': celebritycount,
            'creativezhibo': creativezhibo,
            'orderid': orderid,
            'payall': payall,
        }

        return render(request, 'activity/activeOrderDetailsPay.html', content)

    #充值成功
    def paysuccess(request):
        orderid = request.GET.get('id')
        if orderid != '':
            # 点击付款之后订单状态改为已付款
            orderstatus = Order.objects.get(pk=int(orderid))
            orderstatus.status = 'D'
            orderstatus.save()
        context = {'orderid': orderid}
        return JsonResponse(context)