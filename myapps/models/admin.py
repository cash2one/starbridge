from django.contrib import admin
from starbridge_project import settings


# Register your models here.

# Text to put in each page's <h1>.
admin.site.site_header = settings.ADMIN_SITE_HEADER

# # Text to put at the end of each page's <title>.
admin.site.site_title = settings.ADMIN_SITE_TITLE

# Text to put at the top of the admin index page.
admin.site.index_title = settings.ADMIN_INDEX_TITLE

