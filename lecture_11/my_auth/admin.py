from django.contrib import admin
from my_auth.models import User, ResetPassword
# Register your models here.
admin.site.register(User)


class ResetPasswordAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'created_at',)


admin.site.register(ResetPassword, ResetPasswordAdmin)
