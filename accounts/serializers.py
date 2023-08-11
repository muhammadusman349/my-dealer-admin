from accounts.models import User, OtpVerify,Company,CompanyPermission,CompanyRole,Member
from rest_framework import serializers,status

class CompanyRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= CompanyRole
        fields = (
                'id',
                'company',
                'name',
                'permission',
        )





# class MemberSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Member
#         fields = (
#                'id',
#                'user',
#                'company',
#                'company_role',
#                'is_owner',
#                'is_approved',  
#         )




