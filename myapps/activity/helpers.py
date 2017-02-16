from myapps.celebrity.models import *
from myapps.activity.models import Activity,Order,Flighting,OrderCelebrityShip,OrderStarShip
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
# Create your tests here.
def create_zhibo_order(request):

    activity_id = request.GET.get('id', '') #活动ID
    activitylists = Activity.objects.get(pk=activity_id)

            ## 在红人直播筛选条件 列表
    genderArray = [{'sid':'0','name':'不限'},{'sid':'1','name':'女'},{'sid':'2','name':'男'},{'sid':'3','name':'其他'}]
    categoryArray = CelebrityZhiCategory.objects.values('sid','name').order_by('sid')
    fans_numArray = CelebrityZhiFansNum.objects.values('sid','name').order_by('sid')
    priceArray = CelebrityZhiPrice.objects.values('sid','name').order_by('sid')
    areaArray = CelebrityZhiArea.objects.values('sid','name').order_by('sid')
    platformArray = CelebrityZhiPlatForm.objects.values('sid','name').order_by('sid')

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
    celebrity_list = CelebrityZhibo.objects.all()

    if gender != '0':           ## 性别
        celebrity_list=celebrity_list.filter(celebrity__gender=gender)
    if category != '0':         ## 分类
        celebrity_list=celebrity_list.filter(category__sid=category)
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

    if price != '0':            ## 价格
        if price == '1':
            celebrity_list = celebrity_list.filter(export_price__lt='1000')
        elif price == '2':
            celebrity_list = celebrity_list.filter(export_price__gte='1000').filter(export_price__lt='5000')
        elif price == '3':
            celebrity_list = celebrity_list.filter(export_price__gte='5000').filter(export_price__lt='10000')
        else :
            celebrity_list = celebrity_list.filter(export_price__gte='10000')
    if area != '0':             ## 地区
        celebrity_list = celebrity_list.filter(area__sid=area)
    if platform != '0':         ##平台
        celebrity_list = celebrity_list.filter(broadcast_platform__sid=platform)
    if cred != '0':
        celebrity_list = celebrity_list.filter(is_credibility='B')
    if key != '':
        celebrity_list = celebrity_list.filter(nickname=key)

    # 分页代码
    display_amount = 4
    after_range_num = 3
    bevor_range_num = 2
    paginator = Paginator(celebrity_list, display_amount)
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
    else:
        page_range = paginator.page_range[0:page + bevor_range_num]

    reqFullPath = request.get_full_path()
    # reqPah = request.path
    getValue = reqFullPath[24:]

        # if len(getValue)<=20:
        #     getValue = '?'
        # else:
    getValue = getValue+'&'

    content = {
            'filters': filters,
            'query_category': getValue,
            'activity_id':activity_id,
            'selected': selected,
            'celebrityList': celebrity_list,
            'activitylists': activitylists,
            'page_range': page_range,
        }
    return content