from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('registration',views.registration),
    path('appointment',views.appointment),
]
