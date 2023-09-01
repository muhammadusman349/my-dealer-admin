from accounts.models import (User,
                             Company,
                             CompanyPermission,
                             CompanyRole,
                             Member,
                             SalesRepresentativeRole,
                             SalesRepresentativePermission,
                             Dealer,
                             DealerRole,
                             DealerPermission,
                             Agency,
                             AgencyRole
                            )
from rest_framework import serializers,status
from rest_framework_simplejwt.tokens import RefreshToken


class CompanyRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= CompanyRole
        fields = (
                'id',
                'company',
                'name',
                'permission',
        )

class SalesRepresentativeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRepresentativeRole
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

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
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
                "SR Role Name":member.SalesRepresentative_role.name,
                "SR Role id":member.SalesRepresentative_role.id,
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
    name= serializers.CharField(required = False, allow_blank= True)
    email= serializers.EmailField(required = False, allow_blank= True)
    phone= serializers.CharField(required = False, allow_blank= True)
    password= serializers.CharField(required = False, allow_blank= True)
    class Meta:
        model = Member
        fields = (
               'id',
               'user',
               'company',
               'company_role',
               'SalesRepresentative_role',
               'dealer',
               'dealer_role',
               'agency',
               'agency_role',
               'member_of',
               'name',
               'email',
               'phone',
               'password',
               'is_owner',
               'is_approved',  
        )
    def create(self,validated_data):
        print("validate",validated_data)
        name = validated_data.pop('name',"")
        email = validated_data.pop('email',"")
        phone = validated_data.pop('phone',"")
        password = validated_data.pop('password',"")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user=None
        if user is None:
            user = User(
                name=name,
                email=email,
                phone=phone,
                )        
            user.set_password(password)
            user.is_active = True 
            user.save()
        
        queryset = Member()
        queryset.user = user
        queryset.company= validated_data.get('company')
        queryset.member_of =validated_data.get("member_of")
        queryset.company_role = validated_data.get("company_role")
        queryset.SalesRepresentative_role = validated_data.get("SalesRepresentative_role")
        queryset.dealer = validated_data.get("dealer")
        queryset.dealer_role = validated_data.get("dealer_role")
        queryset.agency = validated_data.get("agency")
        queryset.agency_role = validated_data.get("agency_role")
        queryset.is_owner= validated_data.get('is_owner')
        queryset.is_approved= validated_data.get('is_approved')
        queryset.save()
        return queryset 

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = (
               'id',
               'company',
               'name',
               'email',
               'country',
               'city',
               'state',
               'zip_code',
               'address',
               'phone',
               'fax',
               'dealer_prefix',
               'billing_cycle',
               'dealer_number',
               'ach_fee',
               'logo',
               'max_claim_for_auto_approval',
               'cpi_max_claim_for_auto_approval',
               'approved_labor_rate',
               'max_loss_ratio_for_auto_approval',
               'is_part_of_agency',
               'sale_representative',
               'producer_type',
               'agent_code',
               'agent_name',
               'producer_start_date',
               'terminated',
               'sale_tax_on_part',
               'tax_on_parts',
               'sale_tax_on_labor',
               'tax_on_labor',
               'sale_tax_on_total',
               'tax_on_total',
               'part_number_used_for_claim_review',
               'payment_method',
               'stripe_customer_id',
               'automated_approval',
               'requires_customer_approval',
               'pay_by_card_only',
               'enable_lightspeed',
               'lightspeed_username',
               'lightspeed_password',
               'lightspeed_cmf',
               'has_service_department',
               'repair_order',
               'heading_1',
               'heading_2',
               'message',
               'dealer_note',  
        )

class DealerRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= DealerRole
        fields = (
                'id',
                'company',
                'name',
                'permission',
                )

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = (
            'id',
            'company',
            'sales_representative',
            'name',
            'country',
            'city',
            'state',
            'zip_code',
            'address',
            'phone',
            'fax',
            'own_logo',
            'own_color',
            'own_favicon'
        )

class AgencyRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyRole
        fields = (
               'id',
               'company',
               'name',
               'permission'
        )