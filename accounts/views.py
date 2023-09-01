# from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import (User,
                     CompanyRole,
                     Member,
                     SalesRepresentativeRole,
                     Dealer,
                     DealerRole,
                     Agency,
                     AgencyRole,
                     RepairFacility,
                     RepairFacilityRole
                    )
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from django.contrib.auth.decorators import permission_required
from .serializers import (      RegistrationSerializer,
                                Loginserializer,
                                CompanyRoleSerializer,
                                MemberSerializer,
                                SalesRepresentativeRoleSerializer,
                                DealerSerializer,
                                DealerRoleSerializer,
                                AgencySerializer,
                                AgencyRoleSerializer,
                                RepairFacilitySerializer,
                                RepairFacilityRoleSerializer
                         )

                               
class EmailValidate(generics.CreateAPIView):
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
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class CompanyMemberView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = MemberSerializer
        queryset                = Member.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class SalesRepresentativeRoleView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = SalesRepresentativeRoleSerializer
        queryset                = SalesRepresentativeRole.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)
        

        def get_queryset(self,*args,**kwargs):
            member_id = self.kwargs.get("m_id","")
            print("member_id",member_id)
            member = Member.objects.get(id=member_id)
            print("member",member)
            # queryset = self.queryset
            queryset= SalesRepresentativeRole.objects.filter(company__id=member.company.id)
            print("whar the response",queryset)
            return queryset

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            print("member",member)
            serializer = SalesRepresentativeRoleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        

        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        

        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)


class SalesRepresentativeMemberView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = MemberSerializer
        queryset                = Member.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)
    
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

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = MemberSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

           
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class DealerView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = DealerSerializer
        queryset                = Dealer.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = DealerSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class DealerMemberView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = MemberSerializer
        queryset                = Member.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)


class DealerRoleView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = DealerRoleSerializer
        queryset                = DealerRole.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def get_queryset(self,*args,**kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            queryset= DealerRole.objects.filter(company__id=member.company.id)
            return queryset

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = DealerRoleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

        
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class AgencyView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = AgencySerializer
        queryset                = Agency.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = AgencySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class AgencyRoleView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = AgencyRoleSerializer
        queryset                = AgencyRole.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def get_queryset(self,*args,**kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            queryset= AgencyRole.objects.filter(company__id=member.company.id)
            return queryset

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = AgencyRoleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

        
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class AgencyMemberView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = MemberSerializer
        queryset                = Member.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)


class RepairFacilityView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = RepairFacilitySerializer
        queryset                = RepairFacility.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = RepairFacilitySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class RepairFacilityRoleView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = RepairFacilityRoleSerializer
        queryset                = RepairFacilityRole.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def get_queryset(self,*args,**kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            queryset= RepairFacilityRole.objects.filter(company__id=member.company.id)
            return queryset

        def post(self, request, *args, **kwargs):
            member_id = self.kwargs.get("m_id","")
            member = Member.objects.get(id=member_id)
            serializer = RepairFacilityRoleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(company= member.company) 
                return Response(serializer.data,status=status.HTTP_200_OK) 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

        
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

class RepairFacilityMemberView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = [permissions.IsAuthenticated]
        serializer_class        = MemberSerializer
        queryset                = Member.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)