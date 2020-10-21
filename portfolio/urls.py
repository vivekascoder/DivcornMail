from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('join', views.join, name='join'),
    path('show', views.showmsg, name='show-msg'),
]
