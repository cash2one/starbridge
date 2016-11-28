from django.contrib import admin
from .models import Activity,Order,Flighting,OrderStarShip, OrderCelebrityShip
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    fields = ('name','start_date','end_date','advertiser_name','budget','memo','activity_status','create_user','update_user')
    readonly_fields = ('name','start_date','end_date','advertiser_name','budget','create_time','update_time','create_user','update_user')
    # fieldsets = (
    #     ['基本信息',{
    #         'fields':('name','start_date','end_date','advertiser_name','budget','memo','activity_status'),
    #     }],
    #     ['扩充信息',{
    #         'classes': ('collapse',), # CSS
    #         'fields':('create_time','update_time','create_user','update_user'),
    #     }]
    # )
    list_display = ('id', 'name','start_date','end_date','advertiser_name','budget','activity_status')
    list_filter = ('activity_status', )
    search_fields = ('name',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return [f for f in self.model._meta.fields]
        return self.readonly_fields

admin.site.register(Activity, ActivityAdmin)  #注册到管理工具
admin.site.register([Order,Flighting, OrderStarShip, OrderCelebrityShip])


