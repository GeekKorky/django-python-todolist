from django.contrib import admin
from .models import Accounts


#adding admin columns to model
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    user_info.short_description = 'Info'


admin.site.register(Accounts, AccountsAdmin)
