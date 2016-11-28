from django.contrib import admin
from .models import Celebrity, CelebrityWeibo, CelebrityWeixin, CelebrityZhibo,\
    CelebrityZhiCategory,CelebrityZhiFansNum,CelebrityZhiPrice,CelebrityZhiArea,CelebrityZhiPlatForm


class CelebrityZhiboAdmin(admin.ModelAdmin):
    list_display = ('broadcast_platform', 'platform_id')

class CelebrityZhiCategoryAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class CelebrityZhiFansNumAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class CelebrityZhiPriceAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class CelebrityZhiAreaAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

class CelebrityZhiPlatFormAdmin(admin.ModelAdmin):
    list_display = ('sid', 'name')

# Register your models here.
admin.site.register(Celebrity)  #注册到管理工具
admin.site.register(CelebrityWeibo)
admin.site.register(CelebrityWeixin)
admin.site.register(CelebrityZhibo,CelebrityZhiboAdmin)
admin.site.register(CelebrityZhiCategory,CelebrityZhiCategoryAdmin)
admin.site.register(CelebrityZhiFansNum,CelebrityZhiFansNumAdmin)
admin.site.register(CelebrityZhiPrice,CelebrityZhiPriceAdmin)
admin.site.register(CelebrityZhiArea,CelebrityZhiAreaAdmin)
admin.site.register(CelebrityZhiPlatForm,CelebrityZhiPlatFormAdmin)



