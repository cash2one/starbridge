from django.contrib import admin
from .models import Financial, Funds, Expenses, Recharge, Refund, Invoice
from datetime import datetime
# Register your models here.
##充值汇款
class RechargeAdmin(admin.ModelAdmin):
    old_status = Recharge.objects.values('status')
    for i in old_status:
        if i.get('status') == 'B':
             readonly_fields = ('user', 'time', 'name', 'from_account','amount','to_account', 'type', 'bank_info', 'branch_info', 'status')

        else:
            readonly_fields = ('user', 'time', 'name', 'from_account', 'amount','to_account', 'type', 'bank_info', 'branch_info')
    # fieldsets = (
    #     [None, {
    #         'fields': ('user','time','name','from_account','to_account','amount','type','bank_info','branch_info')
    #     }],
    # )
    list_display=('user','time','name','from_account','to_account','amount','type','bank_info','branch_info')
    search_fields = ('name',)


    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields
        else:
            return [f for f in self.model._meta.fields]

    # 点击保存后执行该方法
    def save_model(self, request, obj, form, change):
       obj_original = self.model.objects.get(pk=obj.pk)   # 获得编辑的那一条信息数据，这是个对象
       old_status = obj_original.status                   # 获得编辑前的旧状态
       amount_money = obj_original.amount                 # 获得编辑的充值金额
       edit_userid = obj_original.user_id                 # 获得编辑的用户id
       try:
            edit_balace = Expenses.objects.filter(user_id=edit_userid).last()  # 获得符合条件的最后一条数据
            balance_money = edit_balace.Balance
       except Exception:
            balance_money = 0
       if request.method == 'POST':
           new_status = request.POST.get('status')    # 获得表单传过来的新状态
           if old_status != new_status and old_status == 'A':
                sum_balance = balance_money + amount_money
                Expense_money = Expenses(
                    user_id=edit_userid,
                    Balance=sum_balance,
                    time=datetime.now(),
                    order_id='0',
                    number='0',
                    amount='0'
                )
                Expense_money.save()
           obj.save()



admin.site.register(Financial)  #注册到管理工具
admin.site.register(Funds)
admin.site.register(Expenses)
admin.site.register(Recharge,RechargeAdmin)
admin.site.register(Refund)
admin.site.register(Invoice)