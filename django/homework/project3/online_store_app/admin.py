from django.contrib import admin
from . models import Client, Product, Order


# @admin.action(description="Добавить скидку 15%")
# def add_discount(modeladmin, request, queryset):
#     queryset.update(price=queryset.price * 0.85)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    ordering = ['-amount']
    list_filter = ['created_at']
    search_fields = ['name']
    search_fields_text = 'Поиск по названию продукта "name"'
    # actions = [add_discount]
    readonly_fields = ['amount', 'created_at']
    fieldsets = [
        (
            'Наименование и количество',
            {
                'classes': ['wide'],
                'fields': ['name', 'amount'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробности для продукта',
                'fields': ['description', 'image'],
            },
        ),
        (
            'Прочее',
            {
                'fields': ['created_at']
            },
        ),
    ]

admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
