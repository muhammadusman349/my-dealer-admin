from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (RegistrationApi,
                    LoginApiView,
                    EmailValidate,
                    MemberView,
                    CompanyRoleView,
                    CompanyMemberView,
                    SalesRepresentativeRoleView,
                    SalesRepresentativeMemberView,
                    DealerView,
                    DealerRoleView,
                    DealerMemberView,
                    AgencyView,
                    AgencyRoleView,
                    AgencyMemberView
                    )

urlpatterns = [
    path("",                                                  RegistrationApi.as_view(),              name='register'),
    path('login/',                                            LoginApiView.as_view(),                 name='login'),
    path('token-refresh/',                                    jwt_views.TokenRefreshView.as_view(),   name='token_refresh'),
    path('<int:m_id>/email/validate',                         EmailValidate.as_view(),                name='Email-Validate'),

    path('<int:m_id>/company_role/',                          CompanyRoleView.as_view(),              name='CompanyRole-listcreate-view'),
    path('<int:m_id>/company_role/<int:id>/',                 CompanyRoleView.as_view(),              name='CompanyRole-detail-view'),
    path('<int:m_id>/company/member/',                        CompanyMemberView.as_view(),            name='Company-Member-listcreate-view'),
    path('<int:m_id>/company/member/<int:id>/',               CompanyMemberView.as_view(),            name='Company-Member-detail-view'),

    path('<int:m_id>/member/',                                MemberView.as_view(),                   name='Member-listcreate-view'),
    path('<int:m_id>/member/<int:id>/',                       MemberView.as_view(),                   name='Member-detail-view'),

    path('<int:m_id>/SalesRepresentativeRole/',               SalesRepresentativeRoleView.as_view(),  name='SalesRepresentativeRole-listcreate-view'),
    path('<int:m_id>/SalesRepresentativeRole/<int:id>/',      SalesRepresentativeRoleView.as_view(),  name='SalesRepresentativeRole-detail-view'),
    path('<int:m_id>/SalesRepresentative/member/',            SalesRepresentativeMemberView.as_view(),name='SalesRepresentative-Member-listcreate-view'),
    path('<int:m_id>/SalesRepresentative/member/<int:id>/',   SalesRepresentativeMemberView.as_view(),name='SalesRepresentative-Member-detail-view'),

    path('<int:m_id>/dealer/',                                DealerView.as_view(),                   name='Dealer-listcreate-view'),
    path('<int:m_id>/dealer/<int:id>/',                       DealerView.as_view(),                   name='Dealer-detail-view'),
    path('<int:m_id>/dealer_role/',                           DealerRoleView.as_view(),               name='DealerRole-listcreate-view'),
    path('<int:m_id>/dealer_role/<int:id>/',                  DealerRoleView.as_view(),               name='DealerRole-detail-view'),
    path('<int:m_id>/dealer/member/',                         DealerMemberView.as_view(),             name='Dealer-Member-listcreate-view'),
    path('<int:m_id>/dealer/member/<int:id>/',                DealerMemberView.as_view(),             name='Dealer-Member-detail-view'),

    path('<int:m_id>/agency/',                                AgencyView.as_view(),                   name='Agency-listcreate-view'),
    path('<int:m_id>/agency/<int:id>/',                       AgencyView.as_view(),                   name='Agency-detail-view'),
    path('<int:m_id>/agency_role/',                           AgencyRoleView.as_view(),               name='AgencyRole-listcreate-view'),
    path('<int:m_id>/agency_role/<int:id>/',                  AgencyRoleView.as_view(),               name='AgencyRole-detail-view'),
    path('<int:m_id>/agency/member/',                         AgencyMemberView.as_view(),             name='Agency-Member-listcreate-view'),
    path('<int:m_id>/agency/member/<int:id>/',                AgencyMemberView.as_view(),             name='Agency-Member-detail-view'),

    
]