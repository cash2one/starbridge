from django.contrib import admin
from .models import Activity,Order,Flighting,OrderStarShip, OrderCelebrityShip
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    # fields = ('name', 'start_date')
    readonly_fields = ('create_user','update_user','create_time','update_time',)
    fieldsets = (
        ['基本信息',{
            'fields':('name','start_date','end_date','advertiser_name','budget','memo','activity_status'),
        }],
        ['扩充信息',{
            'classes': ('collapse',), # CSS
            'fields':('create_user','update_user','update_time','create_time',),
        }]
    )
    list_display = ('id', 'name','start_date','end_date','advertiser_name','budget','activity_status')
    list_filter = ('activity_status', )
    search_fields = ('name',)

admin.site.register(Activity, ActivityAdmin)  #注册到管理工具
admin.site.register([Order,Flighting, OrderStarShip, OrderCelebrityShip])


