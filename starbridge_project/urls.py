"""starbridge_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from myapps.users.views import LoginView,RegisterView,ForgetPasswordView,ResetPasswordView,ChangePasswordView,PersonalData
from myapps.home.views import HomePageView
from myapps.activity.views import ActivityPageView,AddActivityView
from myapps.creative.views import CreativePageView
from myapps.report.views import ReportPageView
from myapps.celebrity.views import CelebrityPageView
from myapps.star.views import StarPageView
from myapps.finance.views import FinancePageView,RechargeMoney,RefundMoney

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',LoginView.post, name='login'),

# user 模块# # # # # # # # # # # # # # # # # # # #
    url(r'^login/$', LoginView.post, name='login'), # 登录
    url(r'^register/$', RegisterView.register, name='register'), # 注册
    url(r'^changepassword/$', ChangePasswordView.change_password, name='changepassword'), # 修改密码
    url(r'^forgetpassword/$', ForgetPasswordView.forget_password, name='forgetpassword'), # 忘记密码
    url(r'^resetpassword/(?P<username>\w+)$', ResetPasswordView.reset_password, name='resetpassword'), # 重置密码显示用户
    url(r'^submitpassword/$', ResetPasswordView.subit_newpassword, name='submitpassword'), # 重置密码
    url(r'^changedata/$', PersonalData.personal_data, name='changedata'), # 修改个人信息
    url(r'^logout/$',LoginView.logout,name='logout'),   # 退出登录

# 一 首页模块 home# # # # # # # # # # # # # # # # #
    url(r'^home/$', HomePageView.list_data,name='home'), # 首页
    url(r'^home/ajax__data', HomePageView.ajax_a,name='a_data'),#首页查询数据

# 二 活动模块 activity# # # # # # # # # # # # # # #
    url(r'^activity/$', ActivityPageView.activity, name='activity'),  # 活动
    url(r'^activity/queryactivity/$', ActivityPageView.queryactivity, name='queryactivity'),  # 多条件查询活动
    url(r'^activity/addactivity/$', AddActivityView.addactivity, name='addactivity'),  # 新建活动2
    url(r'^activity/acitve_detail/$', ActivityPageView.acitve_detail, name='acitve_detail'),  # 活动详情
    url(r'^activity/updateactivity/$', AddActivityView.updateactivity, name='updateactivity'),  # 修改活动
    url(r'^activity/acitve_close/$', ActivityPageView.acitve_close, name='acitve_close'),  # 关闭活动
    url(r'^activity/create_order1/$', ActivityPageView.create_order1, name='create_order1'),  # 创建订单1
    url(r'^activity/create_order2/$', ActivityPageView.create_order2, name='create_order2'),  # 创建订单2
    url(r'^activity/create_order3/$', ActivityPageView.create_order3, name='create_order3'),  # 创建订单3
    url(r'^activity/save_order/$', ActivityPageView.save_order, name='save_order'),  # 创建订单保存
    url(r'^activity/order_details/$', ActivityPageView.order_details, name='order_details'),  # 创建订单详情
    url(r'^activity/showchecked/$', ActivityPageView.showchecked, name='showchecked'),  # 只显示已选(创建表单1)
    url(r'^activity/updateactivity_ID/$', AddActivityView.updateactivity_ID, name='updateactivity_ID'),  # 修改活动ID
    url(r'^activity/exportactivity/$', ActivityPageView.exportactivity, name='exportactivity'),  # 活动批量导
    url(r'^activity/choiceStar/$', AddActivityView.choiceStar, name='choiceStar'), #选择红人(明星)

    url(r'^activity/pay/$',AddActivityView.pay,name='pay'), #充值付款
    url(r'^activity/orderdetails/$',ActivityPageView.orderdetails,name='orderdetails'), #订单详情
    url(r'^activity/upload_goods_url/$', ActivityPageView.upload_goods_url,name='upload_goods_url'),  # 保存订单前素材上传和点击查看订单未上传红人

    url(r'^activity/paysuccess/$', AddActivityView.paysuccess, name='paysuccess'),#充值成功

# 三 素材模块 creative# # # # # # # # # # # # # # #
    url(r'^creative/$', CreativePageView.list_view, name='creative'), # 素材中心
    url(r'^creative/edit/$',CreativePageView.edit_view,name='creative_edit'),#编辑素材
    url(r'^creative/add/$', CreativePageView.add_view, name='creative_add'), #新建素材
    url(r'^creative/del/$',CreativePageView.delete_view,name='creative_delete'), #删除素材单个
    url(r'^creative/delmany/$',CreativePageView.delete_many_view,name='creative_many_delete'), #删除素材 多个

# 四 数据报表 模块 report# # # # # # # # # # # # # #
    url(r'^report/$', ReportPageView.list_view, name='report'), # 数据报表
    url(r'^report/datainput/$',ReportPageView.datainput,name='datainput'),
    # url(r'^report/click_views$', ReportPageView.click_views, name='click_views'), # 点击查看
    # url(r'^report/report_deatail$', ReportPageView.report_detail, name='report_detail'), # 详情

# 五 红人库 模块 celebrity# # # # # # # # # # # # # #
    url(r'^celebrity/$', CelebrityPageView.list_view, name='celebrity'), # 红人库
    url(r'^celebrity/detail/$',CelebrityPageView.detail_view, name='celebrity_detail' ),

# 六 明星库 模块 star# # # # # # # # # # # # # # # # #
    url(r'^star/$', StarPageView.list_view, name='star'), # 明星库  login_required(StarPageView.as_view()
    url(r'^star/detail/$',StarPageView.detail_view, name='star_detail'),

# 七 财务报表模块 finance# # # # # # # # # # # # # # #
    url(r'^finance/$', FinancePageView.list_finance, name='finance'), # 财务报表
    url(r'^finance/remitmoney/$',RechargeMoney.remitmoney,name='remitmoney'),#充值汇款
    url(r'^finance/refundmoney/$',RefundMoney.refundmoney,name='refundmoney'),#退款申请

    url(r'^finance/ajax__data', FinancePageView.ajax_f, name='f_data'),
    url(r'^finance/ajax__chaxun', FinancePageView.ajax_chaxun, name='c_data'),
]

import os
from django.conf.urls import *
from starbridge_project.settings import BASE_DIR
urlpatterns += patterns("",
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(BASE_DIR, "media"), 'show_indexes': True }),
                        )