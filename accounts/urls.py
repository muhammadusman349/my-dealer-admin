from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (RegistrationApi,
                    LoginApiView,
                    EmailValidate,
                    MemberView,
                    CompanyRoleView,
                    SalesRepresentativeRoleView,
                    DealerView,
                    DealerRoleView
                    )

urlpatterns = [
    path("",                                                  RegistrationApi.as_view(),              name='register'),
    path('login/',                                            LoginApiView.as_view(),                 name='login'),
    path('token-refresh/',                                    jwt_views.TokenRefreshView.as_view(),   name='token_refresh'),
    path('<int:m_id>/email/validate',                         EmailValidate.as_view(),                name='Email-Validate'),
    path('<int:m_id>/company_role/',                          CompanyRoleView.as_view(),              name='CompanyRole-listcreate-view'),
    path('<int:m_id>/company_role/<int:id>/',                 CompanyRoleView.as_view(),              name='CompanyRole-detail-view'),
    path('<int:m_id>/member/',                                MemberView.as_view(),                   name='Member-listcreate-view'),
    path('<int:m_id>/member/<int:id>/',                       MemberView.as_view(),                   name='Member-detail-view'),
    path('<int:m_id>/SalesRepresentativeRole/',               SalesRepresentativeRoleView.as_view(),  name='SalesRepresentativeRole-listcreate-view'),
    path('<int:m_id>/SalesRepresentativeRole/<int:id>/',      SalesRepresentativeRoleView.as_view(),  name='SalesRepresentativeRole-detail-view'),
    path('<int:m_id>/dealer/',                                DealerView.as_view(),                   name='Dealer-listcreate-view'),
    path('<int:m_id>/dealer/<int:id>/',                       DealerView.as_view(),                   name='Dealer-detail-view'),
    path('<int:m_id>/dealer_role/',                           DealerRoleView.as_view(),               name='DealerRole-listcreate-view'),
    path('<int:m_id>/dealer_role/<int:id>/',                  DealerRoleView.as_view(),               name='DealerRole-detail-view'),
]