from django.contrib import admin

from core.admins.UserAdmin import UserAdmin
from core.admins.TableAdmin import TableAdmin
from core import models


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Table, TableAdmin)
