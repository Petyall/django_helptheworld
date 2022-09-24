from django.contrib import admin
from .models import Help, Instance, Org, Status, Type, OrgForm

admin.site.register(Type)
admin.site.register(OrgForm)
admin.site.register(Status)
admin.site.register(Help)

class OrgInstanceInline(admin.TabularInline):
    model = Instance

# Фильтрация
@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ('name','TypeOrg',)
    list_filter = ('TypeOrg',)
    inlines = [OrgInstanceInline]

# Фильтрация
@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('org','status',)
    list_filter = ('status',)
    fieldsets = (
        ('Название организации/страны, имя человека', {
            'fields': ('org',)
        }),
        ('Статус пожертвований', {
            'fields': ('status',)
        }),
    )

