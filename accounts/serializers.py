from accounts.models import User, OtpVerify,Company,CompanyPermission,CompanyRole,Member
from rest_framework import serializers,status
from rest_framework_simplejwt.tokens import RefreshToken
import pyotp
import base64
import random
import string
import time

class CompanyRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= CompanyRole
        fields = (
                'id',
                'company',
                'name',
                'permission',
        )

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    
    class Meta:
        model = User
        fields=(
            'id',
            'name',
            'email',
            'phone',
            'password',
            'password2',
            'created_at',
            'updated_at',
            )
        read_only_fields=["created_at","updated_at"]
        extra_kwargs = { 
                        'password': {'write_only': True},

                        } 
                        
    def validate(self, obj):
        if obj['password'] != obj['password2']:
            raise serializers.ValidationError({"Password": "Password fields didn't match."})
        return obj
    
    def create(self,validated_data):   
        user_obj = User(
            name      = validated_data.get('name'),
            email     = validated_data.get('email'),
            phone     = validated_data.get('phone'),
            )
                  
        user_obj.set_password(validated_data.get('password'))
        # user_obj.is_owner = True 
        user_obj.save()
        return user_obj
    
    
class Loginserializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password  =serializers.CharField(required=True)
    # member_info = serializers.SerializerMethodField() 

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            # 'member_info',
        ]
    
        
    def validate(self, attr):
        email = attr.get('email', '')
        password = attr.get('password', '')
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"email": "provided credentials are not valid email"}, code=status.HTTP_401_UNAUTHORIZED)

        if user:
            if not user.check_password(password):
                raise serializers.ValidationError(
                    {"password": "provided credentials are not valid password"}, code=status.HTTP_401_UNAUTHORIZED)
                
        token = RefreshToken.for_user(user)
        members = Member.objects.filter(user__email = user.email)
        member_list =[]
        for member in members:
            data_dict = {
                "Member id":member.id,
                "Company Name":member.company.name,
                "Company id":member.company.id,
                "Company Role Name":member.company_role.name,
                "Company Role id":member.company_role.id,
                "Owner":member.is_owner
            }
            member_list.append(data_dict)
        attr['id']            = int(user.id)
        attr['name']          = str(user.name)
        attr['member info']   = member_list
        attr['email']         = str(user.email)
        attr['access_token']  = str(token.access_token)
        attr['refresh_token'] = str(token)
        
        return attr
   
class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = (
               'id',
               'user',
               'company',
               'company_role',
               'is_owner',
               'is_approved',  
        )




# class generateKey:
#     @staticmethod
#     def return_value(user_obj):
#         timestamp = str(int(time.time()))
#         user_id = str(user_obj.id)
#         random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
#         return timestamp + user_id + random_string
    
# class UserListSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    
#     class Meta:
#         model = User
#         fields=(
#             'id',
#             'name',
#             'email',
#             'phone',
#             'password',
#             'password2',
#             'created_at',
#             'updated_at',
#             )
#         read_only_fields=["created_at","updated_at"]
#         extra_kwargs = { 
#                         'password': {'write_only': True},

#                         } 




# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

#     def validate(self, attrs):
#         new_password = attrs.get("new_password", None)
#         old_password = attrs.get("old_password", None)
#         try:
#             user = User.objects.get(email=str(self.context['user']))
#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#                 {"error ": "User not found."})
#         if not user.check_password(old_password):
#             raise serializers.ValidationError(
#                 {"error": "Incorrect Password"})
#         if new_password and len(new_password) > 5:
#             if user.check_password(new_password):
#                 raise serializers.ValidationError(
#                     {"error": "New password should not be same as old_password"})
#         else:
#             raise serializers.ValidationError(
#                 {"error": "Minimum length of new Password should be greater than 5"})
#         return attrs

#     def create(self, validated_data):    
#         user = self.context['user']
#         user.set_password(validated_data.get("new_password"))
#         user.save()
#         return validated_data
    


# class ForgetPasswordSerializer(serializers.Serializer):
#     email = serializers.EmailField(max_length=255)
#     def validate(self, attrs):
#         email = attrs.get("email", None)
#         if email is not None:
#             try:
#                 userObj = User.objects.get(email__iexact=email)
#                 otp_obj = OtpVerify.objects.filter(user__id=userObj.id).first()
#                 if otp_obj:
#                     otp_obj.delete()
#                 key = base64.b32encode(generateKey.return_value(userObj).encode())  
#                 otp_key = pyotp.TOTP(key)  
#                 otp = otp_key.at(6)
#                 otp_obj = OtpVerify()
#                 otp_obj.user = userObj
#                 otp_obj.otp = otp
#                 otp_obj.save()
                
#             except Exception as e:
#                 print("Exception", e) 
#                 raise serializers.ValidationError(
#                     {"email": "Valid email is Required"})
#         else:
#             raise serializers.ValidationError({"email": "email is required"})
#         return attrs

# class ResetPasswordSerializer(serializers.Serializer):
#     otp = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)

#     def validate(self, attrs):
#         otp = attrs.get("otp", None)
#         password = attrs.get("password", None)
#         if otp:
#             try:
#                 otpobj = OtpVerify.objects.filter(otp=otp).first()
#                 if otpobj:
#                     otpobj.user.set_password(password)
#                     otpobj.delete()
#                     otpobj.user.save()
#                 else:
#                     raise OtpVerify.DoesNotExist
#             except OtpVerify.DoesNotExist:
#                 raise serializers.ValidationError(
#                     {"error": "Valid OTP  is Required"})
#         else:
#             raise serializers.ValidationError({"error": "email is required"})
#         return attrs
