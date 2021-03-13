from django.contrib import admin
from django.urls import path, include, re_path
from django.urls import reverse_lazy
import allauth.account.views as views
from apps.user.views import customPasswordChanged

urlpatterns = [
    path('signup/', views.signup, name="account_signup"),
    path('login/', views.login, name="account_login"),
    path('logout/', views.logout, name="account_logout"),
    path("password/change/", customPasswordChanged, name="account_change_password"),
    path('reset_password', views.password_reset, name="account_reset_password"),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", views.password_reset_from_key,
            name="account_reset_password_from_key"),
    path('reset_password_done', views.password_reset_done, name="account_reset_password_done"),
    path('account_reset_password_from_key_done', views.password_reset_from_key_done,
         name="account_reset_password_from_key_done"),
    path("confirm-email/", views.email_verification_sent, name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email, name="account_confirm_email"),
    path("email/", views.email, name="account_email"),
    path("inactive/", views.account_inactive, name="account_inactive"),
]
