from django.contrib import admin
from .models import CreativeWeibo, CreativeWeixin, CreativeZhibo, StarOrCelebrityCreative
# Register your models here.


class CreativeZhiboAdmin(admin.ModelAdmin):
    # readonly_fields = ('is_upload','outer_url','name','content','goods_name','goods_url','archive_url','memo','is_delete','create_time','create_user','update_time','update_user')
    fields = ('is_upload','outer_url','name','content','goods_name','goods_url','archive_url','memo','is_delete','create_time','create_user','update_time','update_user')
    list_display = ('is_upload','outer_url','name','content','goods_name','goods_url','archive_url','memo','is_delete','create_time','create_user','update_time','update_user')
    search_fields = ('name',)

admin.site.register(CreativeWeibo)
admin.site.register(CreativeWeixin)
admin.site.register(CreativeZhibo,CreativeZhiboAdmin)
admin.site.register(StarOrCelebrityCreative)