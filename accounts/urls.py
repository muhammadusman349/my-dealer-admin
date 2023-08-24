from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ( EmailValidate,
                    MemberView,
                    CompanyRoleView,
                    RegistrationApi,
                    LoginApiView,
                    # ChangePasswordView,
                    # ForgetPasswordView,
                    # ResetPasswordView,
                    # UserView,
                    # UserApproveView,
                    )

urlpatterns = [
    path("",                            RegistrationApi.as_view(),              name='register'),
    path("login/",                      LoginApiView.as_view(),                 name='login'),
    path('token-refresh/',              jwt_views.TokenRefreshView.as_view(),   name='token_refresh'),
    path('<int:m_id>/email/validate',               EmailValidate.as_view(),              name='Email-Validate'),
    path('<int:m_id>/company_role/',               CompanyRoleView.as_view(),              name='CompanyRole-listcreate-view'),
    path('<int:m_id>/company_role/<int:id>/',      CompanyRoleView.as_view(),              name='CompanyRole-detail-view'),

    path('<int:m_id>/member/',               MemberView.as_view(),              name='Member-listcreate-view'),
    path('<int:m_id>/member/<int:id>/',      MemberView.as_view(),              name='Member-detail-view'),
    # path('changepassword/',             ChangePasswordView.as_view(),           name='change-password'),
    # path('forget/password/',            ForgetPasswordView.as_view(),           name='forget-password'),
    # path('reset/password/',             ResetPasswordView.as_view(),            name='reset-password'),
    # path("user/" ,                      UserView.as_view(),                     name ='user-list'),
    # path("userapprove/" ,               UserApproveView.as_view(),              name ='user-approve'),
    
]