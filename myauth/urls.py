from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='SignupPage'),
    path('login/', views.login, name='LoginPage'),
    path('logout/', views.logout, name='LogoutPage'),

]
