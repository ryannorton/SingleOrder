from django.contrib import admin
from django.contrib.auth.models import User
from app.models import Meal, Order, Item

class OrderInline(admin.TabularInline):
    model = Order
    extra = 1

class ItemInline(admin.TabularInline):
	model = Item

class MealAdmin(admin.ModelAdmin):
    fieldsets = [
    	(None, 				 {'fields': ['host', 'group', 'restaurant']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [OrderInline]

class OrderAdmin(admin.ModelAdmin):
 	inlines = [ItemInline]

admin.site.register(Meal, MealAdmin)
admin.site.register(Order, OrderAdmin)
