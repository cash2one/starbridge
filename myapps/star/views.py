from django.shortcuts import render, HttpResponse,render_to_response,HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import ListView
from myapps.star.models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from myapps.report.paginator import list_page
from django.contrib.auth.decorators import login_required
# Create your views here.f

class StarPageView(ListView):
    '''当点击明星名字的时候，会出来相关的详细信息，里面的表格数据都是通过下面的orm方法得到的'''
    def detail_view(request):
        star_id = request.GET.get('id', '')
        star_data = Star.objects.filter(pk=star_id).values('name','key_words','introduce','star_zhibo__broadcast_platform',
                                                           'star_zhibo__platform_id','star_zhibo__average_num','star_zhibo__reads_num',
                                                           'star_zhibo__export_price','star_zhibo__ad_implants_price',
                                                           'star_zhibo__brand_exposed_price','cps')
        return render(request,'star/starintroduce.html',locals())
    @login_required
    def list_view(request):
        ## 在明星 直播筛选条件 列表
        genderArray = [{'sid':'0','name':'不限'},{'sid':'1','name':'女'},{'sid':'2','name':'男'},{'sid':'3','name':'其他'}]
        categoryArray = StarZhiCategory.objects.values('sid','name').order_by('sid')
        fans_numArray = StarZhiFansNum.objects.values('sid','name').order_by('sid')
        priceArray = StarZhiPrice.objects.values('sid','name').order_by('sid')
        areaArray = StarZhiArea.objects.values('sid','name').order_by('sid')
        platformArray = StarZhiPlatForm.objects.values('sid','name').order_by('sid')

        ## 页面上方 的筛选条件
        filters = {
            'gender': genderArray,
            'category': categoryArray,
            'fans_num': fans_numArray,
            'price': priceArray,
            'area': areaArray,
            'platform': platformArray,
        }

        ## 默认的选择项目
        gender  = request.GET.get("gender", "0")
        category= request.GET.get("category", "0")
        fans_num= request.GET.get("fans_num", "0")
        price   = request.GET.get("price", "0")
        area    = request.GET.get("area", "0")
        platform= request.GET.get("platform", "0")
        cred    = request.GET.get('cred','0')
        key     = request.GET.get('key','')
        fans_num1  = request.GET.get('fans_num1','')
        fans_num2 = request.GET.get('fans_num2','')
        price1 = request.GET.get('price1','')
        price2 = request.GET.get('price2','')

        selected ={
            'gender': gender,
            'category': category,
            'fans_num': fans_num,
            'price': price,
            'area': area,
            'platform': platform,
            'cred': cred,
            'key': key,
        }

        ## 页面下方的列表

        star_list = StarZhibo.objects.all()

        if gender != '0':           ## 性别
            star_list=star_list.filter(star__gender=gender)
        if category != '0':         ## 分类
            star_list=star_list.filter(category__sid=category)

        if fans_num != '0':         ## 粉丝数
            if fans_num== '1':
                star_list = star_list.filter(fans_num__lt='10000')
            elif fans_num == '2':
                star_list = star_list.filter(fans_num__gte='10000').filter(fans_num__lt='50000')
            elif fans_num == '3':
                star_list = star_list.filter(fans_num__gte='50000').filter(fans_num__lt='100000')
            elif fans_num == '4':
                star_list = star_list.filter(fans_num__gte='100000')
            else :
                star_list = star_list.filter(fans_num__gte='100000')

        if fans_num1 == "" and fans_num2 == "":
            if fans_num != '0':         ## 粉丝数
                if fans_num== '1':
                    star_list = star_list.filter(fans_num__lt='10000')
                elif fans_num == '2':
                    star_list = star_list.filter(fans_num__gte='10000').filter(fans_num__lt='50000')
                elif fans_num == '3':
                    star_list = star_list.filter(fans_num__gte='50000').filter(fans_num__lt='100000')
                elif fans_num == '4':
                    star_list = star_list.filter(fans_num__gte='100000')
                else :
                    star_list = star_list.filter(fans_num__gte='100000')
        elif  fans_num1 != ""and  fans_num2 != "":
            star_list =star_list.filter(fans_num__gte=fans_num1).filter(fans_num__lt=fans_num2)

        if price != '0':            ## 价格
            if price == '1':
                star_list = star_list.filter(export_price__lt='1000')
            elif price == '2':
                star_list = star_list.filter(export_price__gte='1000').filter(export_price__lt='5000')
            elif price == '3':
                star_list = star_list.filter(export_price__gte='5000').filter(export_price__lt='10000')
            else :
                star_list = star_list.filter(export_price__gte='10000')
        if price1 == "" and price2 == "":
            if price != '0' :            ## 价格
                if price == '1':
                    star_list = star_list.filter(export_price__lt='1000')
                elif price == '2':
                    star_list = star_list.filter(export_price__gte='1000').filter(export_price__lt='5000')
                elif price == '3':
                    star_list = star_list.filter(export_price__gte='5000').filter(export_price__lt='10000')
                else :
                    star_list = star_list.filter(export_price__gte='10000')
        elif price1 != "" and price2 !="" :
            star_list = star_list.filter(export_price__gte=price1).filter(export_price__lt=price2)

        if area != '0':             ## 地区
            star_list = star_list.filter(area__sid=area)
        if platform != '0':         ##平台
            star_list = star_list.filter(broadcast_platform__sid=platform)
        if cred != '0':
            star_list = star_list.filter(is_credibility='B')
        if key != '':
            star_list = star_list.filter(star__name__contains=key)
        #分页代码
        # pagination=list_page(request,star_list)
        pagination = list_page(request,list=star_list,display=10,after_range_num=3,bevor_range_num=2)
        # getValue = '?gender='+gender+'&category='+category+'&fans_num='+fans_num+'&price='+price+'&area='+area+'&platform='+platform+'&key='+key
        getValue = '?gender='+gender+'&category='+category+'&fans_num1='+fans_num1+'&fans_num2='+fans_num2+'&fans_num='+fans_num+'&price1='+price1+'&price2='+price2+'&price='+price+'&area='+area+'&platform='+platform+'&key='+key

        content = {
            'active_menu': '明星库',
            'filters': filters,
            'query_category': getValue,
            'selected': selected,
            # 'star_list': star_list,
            'starvalue':pagination,
        }
        return render(request,'star/mingxingku.html',content)







