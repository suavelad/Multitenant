from django.conf.urls import url

from auth_api import views
from .api import UserDetails, DeactivateUserView,  LoginView, LogoutView, CreateUserView, UsersViewSet, \
    CreateSecureIDView, CreateTellerView, CreateMgtView, CreateSupervisorView, UpdatePassword, ResetPassword, \
    ResetAfterMail, CreateCustomerView,PasswordResetConfirmView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [

    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^deactivate/user/(?P<pk>\d+)/$', DeactivateUserView.as_view()),
    url(r'^supervisor/register/$', CreateSupervisorView.as_view()),
    url(r'^teller/register/$', CreateTellerView.as_view()),
    url(r'^admin/register/$', CreateMgtView.as_view()),
    url(r'^sid/register/$', CreateSecureIDView.as_view()),
    url(r'^customer/register/$', CreateCustomerView.as_view()),
    url(r'^change/p/$', UpdatePassword.as_view()),
    url(r'^reset/p/$', ResetPassword.as_view()),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
    url(r'^reset/after/$', ResetAfterMail.as_view()),
    url(r'^details/$', UserDetails.as_view()),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

   ]
