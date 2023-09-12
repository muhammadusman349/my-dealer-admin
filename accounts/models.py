from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from .utils import (Company_permission_choices,
                    Sales_representative_choices,
                    Dealer_choices,
                    Agency_choices,
                    RepairFacility_choices,
                    user_choices,
                    producer_type,
                    claim_review_choices,
                    payment_method_choices,
                    dealer_of,
                    dwolla_receiving_account_choices,
                    )
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email, password=None):
        if email is None:
            raise TypeError('User should have a Email')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(email,password=password)
        
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.is_approved = True
        user.save()
        return user
class Company(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=255,unique=True)
    country = models.CharField(max_length=220)
    city = models.CharField(max_length=220)
    state = models.CharField(max_length=220)
    address = models.CharField(max_length=256)
    postal_address = models.CharField(max_length=256)
    strip_secret_key = models.CharField(max_length=120)
    strip_public_key = models.CharField(max_length=120)
    dwolla_stagging = models.BooleanField(default=True)
    dwolla_secret_key = models.CharField(max_length=120)
    dwolla_public_key = models.CharField(max_length=120)
    phone = models.CharField(max_length=120,null=True)
    logo = models.ImageField(upload_to="Logo/",verbose_name='Logo',null=True,blank=True)
    card_logo = models.ImageField(upload_to="Card_logo/",verbose_name="Card_Logo",null=True,blank=True)
    heading_1 = models.CharField(max_length=120)
    heading_2 = models.CharField(max_length=120)
    message = models.TextField()
    ck_stagging = models.BooleanField(default=True)
    ck_username = models.CharField(max_length=120)
    ck_pass = models.CharField(max_length=120)
    ck_tpaCode = models.CharField(max_length=120)
    motor_stagging = models.BooleanField(default=True)
    motor_public_key = models.CharField(max_length=120)
    motor_private_key = models.CharField(max_length=120)
    wis_inspection_stagging = models.BooleanField(default=True)
    wis_username = models.CharField(max_length=120)
    wis_pass = models.CharField(max_length=120)
    dwolla_limit = models.IntegerField()
   
    def __str__(self):
        return (self.name) 

class CompanyPermission(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return (self.name) 

class CompanyRole(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=120)
    permission = models.ManyToManyField(CompanyPermission)

    def __str__(self):
        return (self.name) 

class SalesRepresentativePermission(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return (self.name)
    
class SalesRepresentativeRole(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    permission = models.ManyToManyField(SalesRepresentativePermission)

    def __str__(self):
        return str(self.name)

class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone = models.CharField(max_length=100,null=True)
    is_approved = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)
    is_verified = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    
    def __str__(self):
        return (self.email)   

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return True    


class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    company_role = models.ForeignKey(CompanyRole,on_delete=models.SET_NULL,null=True,blank=True)
    SalesRepresentative_role = models.ForeignKey(SalesRepresentativeRole,on_delete=models.SET_NULL,null=True,blank=True)
    dealer = models.ForeignKey('accounts.Dealer', on_delete=models.SET_NULL,null=True,blank=True)
    dealer_role = models.ForeignKey('accounts.DealerRole', on_delete=models.SET_NULL,null=True,blank=True)
    agency = models.ForeignKey('accounts.Agency', on_delete=models.SET_NULL,null=True,blank=True)
    agency_role = models.ForeignKey('accounts.AgencyRole', on_delete=models.SET_NULL,null=True,blank=True)
    repair_facility = models.ForeignKey('accounts.RepairFacility', on_delete=models.SET_NULL,null=True,blank=True)
    repair_facility_role = models.ForeignKey('accounts.RepairFacilityRole', on_delete=models.SET_NULL,null=True,blank=True)
    member_of = models.CharField(max_length=50, choices=user_choices, default=user_choices)
    is_owner = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    


class Dealer(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    dealer_of = models.CharField(max_length=50,choices=dealer_of,default=dealer_of)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=255,unique=True)
    country = models.CharField(max_length=220)
    city = models.CharField(max_length=220)
    state = models.CharField(max_length=220)
    zip_code = models.CharField(max_length=120)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=120,null=True)
    fax = models.CharField(max_length=120)
    dealer_prefix = models.CharField(max_length=120)
    billing_cycle = models.IntegerField()
    dealer_number = models.CharField(max_length=120,null=True,blank=True)
    ach_fee = models.IntegerField()
    logo = models.ImageField(upload_to="Logo/",verbose_name='Logo',null=True,blank=True)
    max_claim_for_auto_approval = models.IntegerField()
    cpi_max_claim_for_auto_approval = models.IntegerField()
    approved_labor_rate = models.IntegerField()
    max_loss_ratio_for_auto_approval = models.IntegerField()
    is_part_of_agency = models.BooleanField(default=False)
    sale_representative = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='sr',null=True,blank=True)
    producer_type = models.CharField(max_length=50,choices=producer_type,default=producer_type)
    agent_code = models.CharField(max_length=120)
    agent_name = models.CharField(max_length=120)
    producer_start_date = models.DateField()
    producer_end_date = models.DateField(null=True,blank=True)
    terminated = models.BooleanField(default=False)
    sale_tax_on_part = models.BooleanField(default=False)
    tax_on_parts =models.IntegerField()
    sale_tax_on_labor = models.BooleanField(default=False)
    tax_on_labor = models.IntegerField()
    sale_tax_on_total = models.BooleanField(default=False)
    tax_on_total = models.IntegerField()
    part_number_used_for_claim_review = models.CharField(max_length=50,choices=claim_review_choices,default=claim_review_choices)
    payment_method = models.CharField(max_length=50,choices=payment_method_choices,default=payment_method_choices)
    stripe_customer_id = models.CharField(max_length=156)
    automated_approval = models.BooleanField(default=False)
    requires_customer_approval = models.BooleanField(default=False)
    pay_by_card_only = models.BooleanField(default=False)
    enable_lightspeed = models.BooleanField(default=False)
    lightspeed_username = models.CharField(max_length=156)
    lightspeed_password = models.CharField(max_length=128)
    lightspeed_cmf = models.CharField(max_length=120)
    has_service_department = models.BooleanField(default=False)
    repair_order = models.BooleanField(default=False)
    heading_1 = models.CharField(max_length=120)
    heading_2 = models.CharField(max_length=120)
    message = models.TextField()
    dealer_note = models.TextField()

    def __str__(self):
        return str(self.name)

class DealerPermission(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return (self.name)
    
class DealerRole(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    permission = models.ManyToManyField(DealerPermission)

    def __str__(self):
        return str(self.name)
    
class Agency(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    sales_representative = models.ForeignKey(Member,related_name='Sr',on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=220)
    city = models.CharField(max_length=220)
    state = models.CharField(max_length=220)
    zip_code = models.CharField(max_length=120)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=120,null=True)
    fax = models.CharField(max_length=120) 
    own_logo = models.ImageField(upload_to="Logo/",verbose_name='Logo',null=True,blank=True)
    own_color = models.CharField(max_length=120)
    own_favicon = models.ImageField(upload_to="favicon/",verbose_name='favicon',null=True,blank=True)

    def __str__(self):
        return str(self.name)
    
class AgencyPermission(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return (self.name)
    
class AgencyRole(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    permission = models.ManyToManyField(AgencyPermission)

    def __str__(self):
        return str(self.name)

class RepairFacility(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=220)
    repair_facility_number = models.CharField(max_length=120)
    city = models.CharField(max_length=220)
    state = models.CharField(max_length=220)
    zip_code = models.CharField(max_length=120)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=120,null=True)
    fax = models.CharField(max_length=120)
    is_active = models.BooleanField(default=False)
    logo = models.ImageField(upload_to="Logo/",verbose_name='Logo',null=True,blank=True)
    sale_tax = models.IntegerField()
    tax_on_parts_cost = models.BooleanField(default=False)
    sale_tax_on_part = models.BooleanField(default=False)
    tax_on_parts =models.IntegerField()
    sale_tax_on_labor = models.BooleanField(default=False)
    tax_on_labor = models.IntegerField()
    sale_tax_on_total = models.BooleanField(default=False)
    tax_on_total = models.IntegerField()
    heading_1 = models.CharField(max_length=120)
    heading_2 = models.CharField(max_length=120)
    message = models.TextField()
    automated_approval = models.BooleanField(default=False)

    def __str__(self):
        return (self.name)

class RepairFacilityPermission(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return (self.name)

class RepairFacilityRole(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    permission = models.ManyToManyField(RepairFacilityPermission)

    def __str__(self):
        return str(self.name)

class DwollaSenderSource(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    dwolla_sender_source = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)

class ExternalAdministrator(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=150,unique=True)
    country = models.CharField(max_length=220)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=220)
    zip_code = models.CharField(max_length=120)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=120,null=True)
    fax = models.CharField(max_length=120)
    own_logo = models.ImageField(upload_to="Logo/",verbose_name='Logo',null=True,blank=True)
    own_color = models.CharField(max_length=120)
    own_favicon = models.ImageField(upload_to="favicon/",verbose_name='favicon',null=True,blank=True)
    payable_code = models.CharField(max_length=120)
    dwolla_sending_account_name = models.CharField(max_length=220)
    dwolla_sending_account = models.CharField(max_length=220)
    dwolla_receiving_account_type = models.CharField(max_length=50,choices=dwolla_receiving_account_choices,default=dwolla_receiving_account_choices)
    dwolla_receiving_account_name = models.CharField(max_length=120)
    dwolla_receiving_account = models.CharField(max_length=120)


def setup_permission():
    for i in Company_permission_choices:
        try:
            role,created = CompanyPermission.objects.get_or_create(code=i[0],name=i[1])
        except Exception as e:
            print("Exception",e)

    for i in Sales_representative_choices:
        try:
            role,created =SalesRepresentativePermission.objects.get_or_create(code=i[0],name=i[1])
        except Exception as e:
            print("Exception",e)

    for i in Dealer_choices:
        try:
            role,created =DealerPermission.objects.get_or_create(code=i[0],name=i[1])
        except Exception as e:
            print("Exception",e)    
    
    for i in Agency_choices:
        try:
            role,created =AgencyPermission.objects.get_or_create(code=i[0],name=i[1])
        except Exception as e:
            print("Exception",e) 
    for i in RepairFacility_choices:
        try:
            role,created =RepairFacilityPermission.objects.get_or_create(code=i[0],name=i[1])
        except Exception as e:
            print("Exception",e)
           
setup_permission()