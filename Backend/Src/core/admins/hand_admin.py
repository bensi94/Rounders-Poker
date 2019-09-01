from django.contrib import admin


class HandAdmin(admin.ModelAdmin):
    list_display = ['id', 'table', 'created']
