from django.urls import path
from basic_app import views

#DEFINE THE app_name for template

app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login')
]