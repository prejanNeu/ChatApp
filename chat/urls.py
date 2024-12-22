from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("login/",views.login_page,name="login_page"),
    path("register/",views.register_page,name="register_page"),
    path('get_info/',views.get_info,name='get_info'),
    path('send_otp/',views.send_otp,name='send_otp'),
    path("verify_mail/",views.veryfy_mail,name='verify_mail'),
    ]