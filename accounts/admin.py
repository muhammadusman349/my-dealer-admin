from django.contrib import admin
from .models import User,Company,CompanyPermission,CompanyRole,Member,OtpVerify
# Register your models here.


admin.site.register(User)
admin.site.register(Company)
admin.site.register(CompanyPermission)
admin.site.register(CompanyRole)
admin.site.register(Member)
admin.site.register(OtpVerify)


