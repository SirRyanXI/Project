from django.contrib import admin
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','category','available','stock','updated']
    list_editable = ['price','stock','available']
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
# Register your models here.
