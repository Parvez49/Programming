
from django.urls import path
from Authentication import views

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("login/",views.handleLogin,name="handleLogin"),
    path("logout",views.handleLogout,name='hangleLogout')
]
