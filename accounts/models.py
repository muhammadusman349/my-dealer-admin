from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from .utils import Company_permission_choices,Sales_representative_choices,user_choices
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

class OtpVerify(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()
    
    def __str__(self):
        return str(self.user)     


class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    company_role = models.ForeignKey(CompanyRole,on_delete=models.CASCADE,null=True,blank=True)
    SalesRepresentative_role = models.ForeignKey(SalesRepresentativeRole,on_delete=models.CASCADE,null=True,blank=True)
    member_of = models.CharField(max_length=50, choices=user_choices, default=user_choices)
    is_owner = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

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
           
setup_permission()