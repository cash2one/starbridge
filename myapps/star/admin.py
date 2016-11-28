from django.contrib import admin
from .models import Star, StarWeixin, StarZhibo, StarWeibo,\
    StarZhiCategory,StarZhiFansNum,StarZhiPrice,StarZhiArea,StarZhiPlatForm
# Register your models here.


class StarZhiCategoryAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class StarZhiFansNumAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class StarZhiPriceAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class StarZhiAreaAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class StarZhiPlatFormAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

admin.site.register(Star)  #注册到管理工具
admin.site.register(StarWeixin)
admin.site.register(StarZhibo)
admin.site.register(StarWeibo)
admin.site.register(StarZhiCategory,StarZhiCategoryAdmin)
admin.site.register(StarZhiFansNum,StarZhiFansNumAdmin)
admin.site.register(StarZhiPrice,StarZhiPriceAdmin)
admin.site.register(StarZhiArea,StarZhiAreaAdmin)
admin.site.register(StarZhiPlatForm,StarZhiPlatFormAdmin)