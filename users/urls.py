from django.urls import path
from .views import signup_view,login_view,change_password
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path("signup/",signup_view,name="signup"),
    path("register/", signup_view, name="register"),
    path("login/",login_view,name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("change-password/",change_password,name="change_password"),
  ]