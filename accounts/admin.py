from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User,Company,CompanyPermission,CompanyRole,Member,SalesRepresentativeRole,SalesRepresentativePermission,Dealer
# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = ((None, {'fields': ('email', 'password')}),('Personal info', {'fields': ('name','groups')}),('Permissions', {'fields': ('is_approved','is_verified','is_active','is_staff')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email', 'password1', 'password2'),
        }),
    )
    list_display =['id','name','email']
    ordering = ('id',)
    
admin.site.register(User,CustomUserAdmin)
admin.site.register(Company)
admin.site.register(CompanyPermission)
admin.site.register(CompanyRole)
admin.site.register(SalesRepresentativePermission)
admin.site.register(SalesRepresentativeRole)
admin.site.register(Member)
admin.site.register(Dealer)


