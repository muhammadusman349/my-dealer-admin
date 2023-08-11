from django.urls import path
from .views import ( CompanyRoleView )


urlpatterns = [
         path('company_role/',                            CompanyRoleView.as_view(),               name='CompanyRole-listcreate-view'),
         path('company_role/<int:id>/',                   CompanyRoleView.as_view(),               name='CompanyRole-detail-view'),
]