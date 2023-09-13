from django.urls import path
from . import views

app_name='todo'
urlpatterns=[
    path('', views.intro, name='intro'),
    path('to-do',views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('login', views.loginPage, name='login'),
    path('login_completed', views.loginCompleted, name='login_completed'),
    path('register_completed', views.registerCompleted, name='register_completed'),
    path('register', views.registerUser, name='register'),
    path('logout', views.logouUser, name='logout'),
    path('get', views.TodoApi.as_view(), name='TodoApi'),
    
]