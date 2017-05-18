from django.contrib import admin
from rango.models import Category,Page

#include these fields in the category display in admin
class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')

#allow django to automatically prepopulates the slug field as you type in the category name.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
