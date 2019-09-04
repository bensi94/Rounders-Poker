from django.contrib import admin


class TableAdmin(admin.ModelAdmin):
    ordering = ['created']
    list_display = ['id', 'name', 'created', 'type', 'status']
