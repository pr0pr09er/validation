from django.contrib import admin
from django.urls import path
from regApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.reg, name='reg'),
    path('enter/', views.enter),
]
