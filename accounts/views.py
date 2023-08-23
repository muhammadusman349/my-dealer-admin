# from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import User,Company,CompanyPermission,CompanyRole,Member
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from django.contrib.auth.decorators import permission_required
from .serializers import (      RegistrationSerializer,
                                Loginserializer,
                                CompanyRoleSerializer,
                                MemberSerializer,
                         )

                                #  ChangePasswordSerializer,
                                #  ForgetPasswordSerializer,
                                #  ResetPasswordSerializer,
                                #  UserListSerializer,
class UserValidate(generics.CreateAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        queryset                = User.objects.all()

        def post(self, request, *args, **kwargs):
            email = request.data.get("email",'')
            if email:
                try:
                    user_obj = User.objects.get(email__iexact=email)
                    return Response(
                                    {"name": user_obj.name, 
                                     "phone": user_obj.phone,
                                     "valid": False,}, 
                                     status=status.HTTP_400_BAD_REQUEST)
                
                except User.DoesNotExist:
                    return Response({"valid": True}, status=status.HTTP_200_OK)

class CompanyRoleView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = CompanyRoleSerializer
        queryset                = CompanyRole.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def get_queryset(self,*args,**kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            queryset = self.queryset
            queryset= CompanyRole.objects.filter(company__id=member.company.id)
            return queryset

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = CompanyRoleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

        
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def destroy(self, request, *args, **kwargs):
            return super().destroy(request, *args, **kwargs)

class RegistrationApi(generics.GenericAPIView):
    permission_classes      = [permissions.IsAuthenticated]
    serializer_class        = RegistrationSerializer
    queryset                = User.objects.all()

    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True
            user.save()
            return Response(serializer.data,status=status.HTTP_200_OK)       
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

class LoginApiView(generics.GenericAPIView): 
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = Loginserializer
    queryset    = User.objects.all()
    
    
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": self.request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MemberView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = MemberSerializer
        queryset                = Member.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def get_queryset(self):
            return super().get_queryset()

        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)
             
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def destroy(self, request, *args, **kwargs):
            return super().destroy(request, *args, **kwargs)






# class UserView(generics.ListAPIView):
#     permission_classes      = [permissions.IsAuthenticated]
#     serializer_class        = UserListSerializer
#     queryset                = User.objects.all()
#     lookup_field            = 'id'
  
#     def get(self, request, *args, **kwargs):
#         if 'id' in self.kwargs:
#             return self.retrieve(request, *args, **kwargs)
#         else:
#             return self.list(request, *args, **kwargs)

# class UserApproveView(generics.GenericAPIView):
#     permission_classes      = [permissions.IsAuthenticated]  
#     def post(self,request,*args,**kwargs):
#         try:
#             id=self.request.query_params.get('id',None)
#             user=User.objects.get(id=id)
#             user.is_verified=True
#             user.is_approved = True
#             user.save()
#             return Response({"Message":"User is approve "},status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({"Error":"User is Not Exist "},status=status.HTTP_400_BAD_REQUEST)    


# class ChangePasswordView(generics.GenericAPIView):
#     permission_classes = []
#     serializer_class = ChangePasswordSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data, context={'user': self.request.user})
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'password': ' password changed successfully '}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ForgetPasswordView(generics.GenericAPIView):
#     permission_classes = []
#     serializer_class = ForgetPasswordSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             return Response({'opt': 'successfully send OTP '}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ResetPasswordView(generics.GenericAPIView):
#     permission_classes = []
#     serializer_class = ResetPasswordSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             return Response({'password': 'successfully set New Password '}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
