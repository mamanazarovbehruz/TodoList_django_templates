from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('update_account/', views.update_account, name='update_account'),
    path('password_change/', views.password_change, name='password_change'),
]
