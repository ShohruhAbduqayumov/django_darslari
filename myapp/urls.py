from django.urls import path
from . import views

urlpatterns = [
    path('', views.sahifa),
    path('goodbye/', views.goodbye),
    path('ism', views.ism),
    path('hello', views.hello)

]
