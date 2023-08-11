# from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import User,Company,CompanyPermission,CompanyRole,Member
# from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import permissions
from .serializers import CompanyRoleSerializer


class CompanyRoleView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
        permission_classes      = []
        serializer_class        = CompanyRoleSerializer
        queryset                = CompanyRole.objects.all()
        lookup_field            = 'id'

        def get(self, request, *args, **kwargs):
            if 'id' in self.kwargs:
                return self.retrieve(request, *args, **kwargs)
            else:
                return self.list(request, *args, **kwargs)

        def get_queryset(self):
            queryset = self.queryset
            if 'id' not in self.kwargs:
                queryset = CompanyRole.objects.filter(company__id=self.request.user.company.id)
            return queryset


        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)

        def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)

        def destroy(self, request, *args, **kwargs):
            return super().destroy(request, *args, **kwargs)