from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import (User,
                     Company,
                     CompanyPermission,
                     CompanyRole,
                     Member,
                     SalesRepresentativeRole,
                     SalesRepresentativePermission,
                     Dealer,
                     DealerRole,
                     DealerPermission
                     )
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

class CompanyAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name','address')

class CompanyPermissionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name')
class CompanyRoleAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name')

class SalesRepresentativePermissionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name')

class SalesRepresentativeRoleAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name')    

class DealerAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name','dealer_number','dealer_of')  
    list_filter = ('dealer_of',) 

class DealerRoleAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name')  

class DealerPermissionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','name')
class MemberAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id','user','company','company_role','member_of','is_owner','is_approved')  
    list_filter = ('id','company','member_of','is_owner')


admin.site.register(User,CustomUserAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(CompanyPermission,CompanyPermissionAdmin)
admin.site.register(CompanyRole,CompanyRoleAdmin)
admin.site.register(SalesRepresentativePermission,SalesRepresentativePermissionAdmin)
admin.site.register(SalesRepresentativeRole,SalesRepresentativeRoleAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Dealer,DealerAdmin)
admin.site.register(DealerRole,DealerRoleAdmin)
admin.site.register(DealerPermission,DealerPermissionAdmin)