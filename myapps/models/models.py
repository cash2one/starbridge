# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
#
# from django.db import models
########TAdvAgent \   TShare   \  TStore    \     TType
# 账户
# class TAccount(models.Model):
#     name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     type = models.IntegerField()
#     memo = models.CharField(max_length=255, blank=True, null=True)
#     update_user = models.IntegerField()
#     update_time = models.DateTimeField()
#     user_id = models.IntegerField()
#
#     class Meta:
#         db_table = 't_account'

# 账户角色关联表
# class TAccountRole(models.Model):
#     account_id = models.IntegerField()
#     role_id = models.IntegerField()
#
#     class Meta:
#         db_table = 't_account_role'
#         unique_together = (('account_id', 'role_id'),)

# 广告主代理商
# class TAdvAgent(models.Model):
#     company_name = models.CharField(max_length=100)
#     link_man = models.CharField(max_length=50)
#     mobile = models.CharField(max_length=11)
#     web_site = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(max_length=100)
#     register_time = models.DateTimeField()
#     update_user = models.IntegerField()
#     update_time = models.DateTimeField()
#
#     class Meta:
#         db_table = 't_adv_agent'
#
#     def __str__(self):
#         return "%s" % (self.company_name)

# # 活动
# class TCampagin(models.Model):
#     name = models.CharField(max_length=100)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     advertiser_name = models.CharField(max_length=255, blank=True, null=True)
#     budget = models.FloatField()
#     memo = models.CharField(max_length=255, blank=True, null=True)
#     agent_id = models.IntegerField()
#     create_time = models.DateTimeField()
#     create_user = models.IntegerField()
#     update_time = models.DateTimeField()
#     update_user = models.IntegerField()
#
#     class Meta:
#         db_table = 't_campagin'

# # 财务信息
# class TFinancial(models.Model):
#     id = models.IntegerField(primary_key=True)
#
#     class Meta:
#         db_table = 't_financial'

# # 网红
# class TInternetstar(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     key_words = models.CharField(max_length=255, blank=True, null=True)
#     introduce = models.CharField(max_length=255, blank=True, null=True)
#     avatar_url = models.CharField(max_length=255, blank=True, null=True)
#     create_user = models.IntegerField(blank=True, null=True)
#     crate_time = models.DateTimeField(blank=True, null=True)
#     cps = models.FloatField(blank=True, null=True)
#     is_busy = models.IntegerField(blank=True, null=True)
#     credibility = models.IntegerField(blank=True, null=True)
#     gender = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_internetstar'
#
# # 网红微博信息
# class TInternetstarWeibo(models.Model):
#     internetstar_id = models.IntegerField(blank=True, null=True)
#     type_id = models.IntegerField(blank=True, null=True)
#     nickname = models.CharField(max_length=255, blank=True, null=True)
#     url = models.CharField(max_length=255, blank=True, null=True)
#     fans_num = models.IntegerField(blank=True, null=True)
#     is_authentication = models.IntegerField(blank=True, null=True)
#     forward_place = models.FloatField(blank=True, null=True)
#     direct_price = models.FloatField(blank=True, null=True)
#     memo = models.CharField(max_length=255, blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_internetstar_weibo'
#
# # 网红微信
# class TInternetstarWeixin(models.Model):
#     internetstar_id = models.IntegerField(blank=True, null=True)
#     type_id = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     weixinid = models.CharField(max_length=100, blank=True, null=True)
#     fans_num = models.IntegerField()
#     price = models.FloatField(blank=True, null=True)
#     position = models.CharField(max_length=255, blank=True, null=True)
#     level = models.IntegerField(blank=True, null=True)
#     scan_num = models.IntegerField(blank=True, null=True)
#     is_reserve = models.IntegerField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     memo = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         db_table = 't_internetstar_weixin'
#
# # 网红直播
# class TInternetstarZhibo(models.Model):
#     internetstar_id = models.IntegerField(blank=True, null=True)
#     broadcast_platform = models.CharField(max_length=255, blank=True, null=True)
#     fans_num = models.IntegerField(blank=True, null=True)
#     export_price = models.FloatField(blank=True, null=True)
#     ad_implants_price = models.FloatField(blank=True, null=True)
#     brand_exposed_price = models.FloatField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_internetstar_zhibo'

# # 微博素材
# class TMaterialWeibo(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     content = models.CharField(max_length=255, blank=True, null=True)
#     picture = models.CharField(max_length=255, blank=True, null=True)
#     goods_url = models.CharField(max_length=255, blank=True, null=True)
#     memo = models.CharField(max_length=255, blank=True, null=True)
#     create_user = models.IntegerField()
#     create_time = models.DateTimeField()
#
#     class Meta:
#         db_table = 't_material_weibo'
#
# # 微信素材
# class TMaterialWeixin(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     anthor = models.CharField(max_length=100, blank=True, null=True)
#     file_picture_url = models.CharField(max_length=255, blank=True, null=True)
#     create_user = models.IntegerField(blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_material_weixin'
#
# # 直播素材
# class TMaterialZhibo(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     content = models.CharField(max_length=255, blank=True, null=True)
#     goods_name = models.CharField(max_length=255, blank=True, null=True)
#     goods_url = models.CharField(max_length=255, blank=True, null=True)
#     memo = models.CharField(max_length=255, blank=True, null=True)
#     create_user = models.CharField(max_length=255, blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_material_zhibo'

# 菜单
# class TMenu(models.Model):
#     name = models.CharField(max_length=100)
#     url = models.CharField(max_length=255)
#     type = models.IntegerField()
#     level = models.SmallIntegerField()
#     memo = models.CharField(max_length=255)
#     update_user = models.IntegerField()
#     update_time = models.DateTimeField()
#
#     class Meta:
#         db_table = 't_menu'
#
# # 订单
# class TOrder(models.Model):
#     campaign_id = models.IntegerField()
#     name = models.CharField(max_length=255)
#     start_time = models.DateTimeField(blank=True, null=True)
#     end_time = models.DateTimeField(blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#     create_user = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_order'
#
# # 订单红人明星关联表
# class TOrderSuperstarOrInternetstar(models.Model):
#     order_id = models.IntegerField()
#     star_id = models.IntegerField()
#     type = models.IntegerField(blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_order_superstar_or_internetstar'

# # 报告
# class TReport(models.Model):
#     agent_id = models.IntegerField(blank=True, null=True)
#     order_id = models.IntegerField(blank=True, null=True)
#     campagin_id = models.IntegerField(blank=True, null=True)
#     weixin_click = models.IntegerField(blank=True, null=True)
#     weibo_click = models.IntegerField(blank=True, null=True)
#     zhibo_click = models.IntegerField(blank=True, null=True)
#     click_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_report'

# 角色
# class TRole(models.Model):
#     name = models.CharField(max_length=50)
#     memo = models.CharField(max_length=255)
#     update_time = models.DateTimeField()
#     update_user = models.IntegerField()
#     status = models.IntegerField()
#
#     class Meta:
#         db_table = 't_role'

# 角色菜单关联表
# class TRoleMenu(models.Model):
#     role_id = models.IntegerField()
#     menu_id = models.IntegerField()
#
#     class Meta:
#         db_table = 't_role_menu'
#         unique_together = (('role_id', 'menu_id'),)

# 分享
# class TShare(models.Model):
#     account_id = models.IntegerField(blank=True, null=True)
#     url = models.CharField(max_length=255, blank=True, null=True)
#     destination = models.CharField(max_length=255, blank=True, null=True)
#     store_time = models.DateTimeField(blank=True, null=True)
#     memo = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 't_share'

# # 红人素材关联表
# class TStarMaterial(models.Model):
#     # id = models.IntegerField()
#     star_id = models.IntegerField()
#     star_type = models.IntegerField(blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#     material_id = models.IntegerField(blank=True, null=True)
#     material_type = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_star_material'
#         unique_together = (('id', 'star_id'),)

# 收藏
# class TStore(models.Model):
#     account_id = models.IntegerField(blank=True, null=True)
#     url = models.CharField(max_length=255, blank=True, null=True)
#     store_time = models.DateTimeField(blank=True, null=True)
#     source = models.CharField(max_length=255, blank=True, null=True)
#     memo = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 't_store'

# # 明星
# class TSuperstar(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     key_words = models.CharField(max_length=255, blank=True, null=True)
#     introduce = models.CharField(max_length=255, blank=True, null=True)
#     avatar_url = models.CharField(max_length=255, blank=True, null=True)
#     create_user = models.IntegerField(blank=True, null=True)
#     crate_time = models.DateTimeField(blank=True, null=True)
#     cps = models.FloatField(blank=True, null=True)
#     is_busy = models.IntegerField(blank=True, null=True)
#     credibility = models.IntegerField(blank=True, null=True)
#     gender = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_superstar'
#
# # 明星微信信息
# class TSuperstarWeixin(models.Model):
#     superstarr_id = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     weixinid = models.CharField(max_length=100, blank=True, null=True)
#     fans_num = models.IntegerField(blank=True, null=True)
#     price = models.FloatField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     memo = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         db_table = 't_superstar_weixin'
#
# # 明星直播信息
# class TSuperstarZhibo(models.Model):
#     superstar_id = models.IntegerField(blank=True, null=True)
#     broadcast_platform = models.CharField(max_length=255, blank=True, null=True)
#     fans_num = models.IntegerField(blank=True, null=True)
#     export_price = models.FloatField(blank=True, null=True)
#     ad_implants_price = models.FloatField(blank=True, null=True)
#     brand_exposed_price = models.FloatField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_superstar_zhibo'
#
# # 明星微博信息
# class TSuperstarWeibo(models.Model):
#     superstar_id = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     url = models.CharField(max_length=255, blank=True, null=True)
#     fans_num = models.IntegerField(blank=True, null=True)
#     price = models.FloatField(blank=True, null=True)
#     memo = models.CharField(max_length=255, blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_superstar_weibo'

# 类型
# class TType(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     source = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 't_type'
