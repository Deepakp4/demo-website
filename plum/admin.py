from django.contrib import admin
from plum.models import stform
from .models import products
from .models import category,cart

@admin.register(stform)
class stformAdmin(admin.ModelAdmin):
     list_display=('name','email')
     
@admin.register(products)
class productsAdmin(admin.ModelAdmin):
    list_display=('heading','discription')
    
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display=('name',)
# Register your models here.
@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display=('product','quantity')
    