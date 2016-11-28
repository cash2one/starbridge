from myapps.activity.models import Activity
from myapps.activity.models import Order
from myapps.activity.models import  Order_add
from myapps.creative.models import  CreativeZhibo
import re
def activityshow(request,activity_list):
    # activity_list = Activity.objects.all().order_by('-update_time')
    ## 初始化  包含有订单的 活动 数组
    activity_order_list=[]
    for act in activity_list:
        orderlist = Order.objects.filter(activity__id=act.id)
        ## 初始化 活动内部 的订单数组
        order_list=[]
        for order in orderlist:
            if order.id > 0:
                ##根据订单ID获取中间表的ID
                order_addid = Order.objects.filter(pk=order.id).values('order_add_id')
                ##粉丝保底佣金量
                fanscomms = Order_add.objects.filter(pk=order_addid).values('content')[0]['content']
                commsfan = []
                commissions = fanscomms.split('-')
                for commission in commissions:
                    if commission != '':
                        commsfan.append(commission)
                commlen = len(commsfan)  # 计算列表长度
                comms = []
                if commlen != 0:
                    comms.append(commsfan[commlen-1])

                # 活动素材直播信息(已上传,未上传)
                createzhibo_id = Order_add.objects.filter(pk=order_addid).values('creativezhibo_id')[0]['creativezhibo_id']
                createzhibo_mid = createzhibo_id.split(',')
                createzhiboarray = []
                for zhibo in createzhibo_mid:
                    createzhiboarray.append(re.findall(r'(\w*[0-9]+)\w*', zhibo))
                create_zhibo = []
                for createid in createzhiboarray[0]:
                    ##素材信息
                    create_zhibo.append(CreativeZhibo.objects.filter(pk=createid))
                ##已选红人个数
                celebrityall = Order_add.objects.filter(pk=order_addid).values('celebrityzhibo_id')[0]['celebrityzhibo_id']
                celebritycount=celebrityall.split(',')
                # celebrityallcount = len(celebritycount)

                ##已选明星个数
                starallcount = Order_add.objects.filter(pk=order_addid).values('starzhibo_id').count()
                order_list.append({'createzhibo': create_zhibo,'comms':comms, 'order_adds': Order_add.objects.filter(pk=order_addid),'order':order,'celebritynum': len(celebritycount),'starnum': starallcount})
            else:
                order_list.append({'createzhibo': '','comms':'', 'order_adds': '','order':'','celebritynum': '','starnum': ''})
        activity_order_list.append({'object':act,'list':order_list})   ## 组成  包含有订单的 活动 数组
    return activity_order_list