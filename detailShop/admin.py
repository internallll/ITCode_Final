from django.contrib import admin

from detailShop import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'generation')

@admin.register(models.Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_start','year_end', 'image')

@admin.register(models.Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','country_prod','storage')

@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('address','capacity')


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number')

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','address_delivery','comment')

@admin.register(models.OrderElement)
class OrderElementAdmin(admin.ModelAdmin):
    list_display = ('detail','count', 'order')