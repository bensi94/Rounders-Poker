from django.contrib import admin

from core.admins.user_admin import UserAdmin
from core.admins.table_admin import TableAdmin
from core.admins.hand_admin import HandAdmin
from core import models


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Table, TableAdmin)
admin.site.register(models.Hand, HandAdmin)
