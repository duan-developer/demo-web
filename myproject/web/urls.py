from django.urls import path
from . import views 
urlpatterns = [
    path('', views.Nhap),
    path('login/', views.LOG),
    path('dangky/', views.REG),
]
