
from django.urls import path, include
from . import views


urlpatterns = [
    path("",views.index ,name=""),
    path("contact/",views.contact,name="contact"),
    path('checkout/', views.checkout, name="Checkout"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
]


