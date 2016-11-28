from django.shortcuts import render, HttpResponse,render_to_response,HttpResponseRedirect
from django.http import JsonResponse
import json
# from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import ListView
from myapps.celebrity.models import *
from django.core import serializers
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.template import RequestContext


class CelebrityPageView(ListView):
    '''红人页面展现处理完成的数据'''
    @login_required
    def list_view(request):
        ## 在红人直播筛选条件 列表
        '''把每一个筛选条件都作为一个字段分别和sid存进去一个表中（因为性别字段只有下面四种情况，故没用单独的表存放），
        最后把这些数据从数据库中以sid正序排列取出来，最后取出来的格式就是和性别存放的格式一样'''
        genderArray = [{'sid':'0','name':'不限'},{'sid':'1','name':'女'},{'sid':'2','name':'男'},{'sid':'3','name':'其他'}]
        categoryArray = CelebrityZhiCategory.objects.values('sid','name').order_by('sid')
        fans_numArray = CelebrityZhiFansNum.objects.values('sid','name').order_by('sid')
        priceArray = CelebrityZhiPrice.objects.values('sid','name').order_by('sid')
        areaArray = CelebrityZhiArea.objects.values('sid','name').order_by('sid')
        platformArray = CelebrityZhiPlatForm.objects.values('sid','name').order_by('sid')
        ## 页面上方的筛选条件
        filters = {
            'gender': genderArray,
            'category': categoryArray,
            'fans_num': fans_numArray,
            'price': priceArray,
            'area': areaArray,
            'platform': platformArray,
        }

        ## 默认的选择项目，获得页面点击点击后得到的值，默认是0，也就是不限
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


        ''''''
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

        ## 页面下方的列表  fans_num
        # 'gt': '> %s',
        # 'gte': '>= %s',
        # 'lt': '< %s',
        # 'lte': '<= %s',
        celebrity_list = CelebrityZhibo.objects.all()
        '''根据前端传过来的值，进行if判断，最后取出符合要求的值'''
        if gender != '0':           ## 性别
            celebrity_list=celebrity_list.filter(celebrity__gender=gender)
        if category != '0':         ## 分类
            celebrity_list=celebrity_list.filter(category__sid=category)

        if fans_num != '0':         ## 粉丝数
            if fans_num == '1':
                celebrity_list = celebrity_list.filter(fans_num__lt='10000')
            elif fans_num == '2':
                celebrity_list = celebrity_list.filter(fans_num__gte='10000').filter(fans_num__lt='50000')
            elif fans_num == '3':
                celebrity_list = celebrity_list.filter(fans_num__gte='50000').filter(fans_num__lt='100000')
            elif fans_num == '4':
                celebrity_list = celebrity_list.filter(fans_num__gte='100000')
            else :
                celebrity_list = celebrity_list.filter(fans_num__gte='100000')

        if fans_num1 == "" and fans_num2 == "":
            if fans_num != '0':         ## 粉丝数
                if fans_num== '1':
                    celebrity_list = celebrity_list.filter(fans_num__lt='10000')
                elif fans_num == '2':
                    celebrity_list = celebrity_list.filter(fans_num__gte='10000').filter(fans_num__lt='50000')
                elif fans_num == '3':
                    celebrity_list = celebrity_list.filter(fans_num__gte='50000').filter(fans_num__lt='100000')
                elif fans_num == '4':
                    celebrity_list = celebrity_list.filter(fans_num__gte='100000')
                else :
                    celebrity_list = celebrity_list.filter(fans_num__gte='100000')
        elif  fans_num1 != ""and  fans_num2 != "":
            celebrity_list =celebrity_list.filter(fans_num__gte=fans_num1).filter(fans_num__lt=fans_num2)

        if price1 == "" and price2 == "":
            if price != '0' :            ## 价格
                if price == '1':
                    celebrity_list = celebrity_list.filter(export_price__lt='1000')
                elif price == '2':
                    celebrity_list = celebrity_list.filter(export_price__gte='1000').filter(export_price__lt='5000')
                elif price == '3':
                    celebrity_list = celebrity_list.filter(export_price__gte='5000').filter(export_price__lt='10000')
                else :
                    celebrity_list = celebrity_list.filter(export_price__gte='10000')
        elif price1 != "" and price2 !="" :
            celebrity_list = celebrity_list.filter(export_price__gte=price1).filter(export_price__lt=price2)

        if price != '0' :            ## 价格
            if price == '1':
                celebrity_list = celebrity_list.filter(export_price__lt='1000')
            elif price == '2':
                celebrity_list = celebrity_list.filter(export_price__gte='1000').filter(export_price__lt='5000')
            elif price == '3':
                celebrity_list = celebrity_list.filter(export_price__gte='5000').filter(export_price__lt='10000')
            else :
                celebrity_list = celebrity_list.filter(export_price__gte='10000')

        if area != '0':             ## 地区
            celebrity_list = celebrity_list.filter(area__sid__contains=area)
        if platform != '0':         ##平台
            celebrity_list = celebrity_list.filter(broadcast_platform__sid=platform)
        if cred != '0':
            celebrity_list = celebrity_list.filter(is_credibility='B')
        if key != '':
            celebrity_list = celebrity_list.filter(celebrity__name__contains=key)




        #分页代码
        display_amount=5
        after_range_num = 3
        bevor_range_num = 2
        paginator = Paginator(celebrity_list, display_amount)
        sum_page = paginator.num_pages
        try:
            page = int(request.GET.get('page'))
        except:
            page = 1
        try:
            celebrity_list = paginator.page(page)
        except PageNotAnInteger:
            celebrity_list = paginator.page(1)  # 页码不是整数,返回第一页
        except EmptyPage:
            celebrity_list = paginator.page(paginator.num_pages)
        if page > after_range_num:
            page_range = paginator.page_range[page - after_range_num:page + bevor_range_num]
            if page > sum_page - bevor_range_num:
                page_range=paginator.page_range[sum_page -after_range_num-bevor_range_num:page + sum_page]
                if sum_page < after_range_num + bevor_range_num:
                    page_range = paginator.page_range[0:sum_page]
        else:
            page_range = paginator.page_range[0:after_range_num + bevor_range_num]

        getValue = '?gender='+gender+'&category='+category+'&fans_num1='+fans_num1+'&fans_num2='+fans_num2+'&fans_num='+fans_num+'&price1='+price1+'&price2='+price2+'&price='+price+'&area='+area+'&platform='+platform+'&key='+key

        '''
        paginator = Paginator(celebrity_list,5)
        page = request.GET.get('page')
        try:
            celebrity_list = paginator.page(page)
        except PageNotAnInteger:
            celebrity_list = paginator.page(1)
        except EmptyPage:
            celebrity_list = paginator.page(paginator.num_pages)

        reqFullPath = request.get_full_path()
        reqPah = request.path
        getValue = reqFullPath[11:]

        if len(getValue)<=20:
            getValue = '?'
        else:
            getValue = getValue+'&'
        '''
        content = {
            'active_menu': '红人库',
            'filters': filters,
            'query_category': getValue,
            'page_range':page_range,
            'selected': selected,
            'celebrityList': celebrity_list,
        }
        return render(request,'celebrity/redMan.html',content)

    '''红人详情展示页，当点击红人头像的时候，取出来表格中所需要的值'''
    def detail_view(request):
        celebrity_id = request.GET.get('id', '')
        celebrity_data = Celebrity.objects.filter(pk=celebrity_id).values('celebrity_zhibo__sid','name','key_words','introduce','celebrity_zhibo__broadcast_platform__name',
                                                                         'celebrity_zhibo__platform_id', 'celebrity_zhibo__average_num','celebrity_zhibo__reads_num',
                                                                          'celebrity_zhibo__platform_id','celebrity_zhibo__export_price',
                                                                          'celebrity_zhibo__ad_implants_price','celebrity_zhibo__brand_exposed_price',
                                                                          'cps')
        a = "http://qs4.datacross.cn/img_head"
        return render(request,'celebrity/introduce.html',locals())




