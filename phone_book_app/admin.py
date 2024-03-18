from django.contrib import admin
from django.contrib.admin import register

from .models import Province, City, PhoneBookRow


# Register your models here.


@admin.action(description="Activate selected items")
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Deactivate selected items")
def deactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


@register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'is_active',
                    'created_date',
                    'updated_date')
    list_display_links = ('id', 'name')
    list_filter = ('is_active',
                   'created_date',
                   'updated_date',
                   )
    list_editable = ('is_active',)
    search_fields = ('name',)

    actions = (
        activate_selected_items,
        deactivate_selected_items,

    )


@register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'province',
                    'is_active',
                    'created_date',
                    'updated_date')
    list_display_links = ('id', 'name', 'province')
    list_filter = ('is_active',
                   'created_date',
                   'updated_date',
                   )
    list_editable = ('is_active',)
    search_fields = ('name', 'province')

    actions = (
        activate_selected_items,
        deactivate_selected_items,

    )


@register(PhoneBookRow)
class PhoneBookRowAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'city',
                    'phone_number',
                    'author',
                    'is_active',
                    'created_date',
                    'updated_date')
    list_display_links = ('id',
                          'first_name',
                          'last_name',
                          'city',
                          'phone_number',
                          'author')
    list_filter = ('is_active',
                   'created_date',
                   'updated_date',
                   'author',)
    list_editable = ('is_active',)
    search_fields = ('first_name',
                     'last_name',
                     'city',
                     'phone_number',
                     'author')

    actions = (
        activate_selected_items,
        deactivate_selected_items,

    )
