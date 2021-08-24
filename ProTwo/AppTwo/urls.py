from django.urls import path
from AppTwo import views

urlpatterns = [
    
    path('users/',views.user,name='user'),
    path('',views.help,name='help'),
]