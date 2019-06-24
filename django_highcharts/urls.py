"""django_highcharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from titanic_passengers import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sex_view/', views.sex_view, name='sex_view'),
    path('sex_view/2/', views.sex_view_2, name='sex_view_2'),
    path('sex_view/3/', views.sex_view_3, name='sex_view_3'),
    path('ajax/', views.ajax, name='ajax'),
    path('ajax/data/', views.chart_data, name='chart_data'),
    path('admin/', admin.site.urls),
]
