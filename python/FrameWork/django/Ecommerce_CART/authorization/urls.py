
from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.user_login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.user_logout,name="logout"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),

]
