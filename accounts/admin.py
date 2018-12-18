from django.contrib import admin
from .models import Accounts


#adding admin columns to model
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('userprofile', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(AccountsAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'userprofile')
        return queryset

    user_info.short_description = 'Info'


admin.site.register(Accounts, AccountsAdmin)
