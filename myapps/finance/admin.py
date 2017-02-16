from django.contrib import admin
from .models import Financial, Funds, Expenses, Recharge, Refund, Invoice
# Register your models here.
admin.site.register(Financial)  #注册到管理工具
admin.site.register(Funds)
admin.site.register(Expenses)
admin.site.register(Recharge)
admin.site.register(Refund)
admin.site.register(Invoice)