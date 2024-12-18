"""
URL configuration for demosite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from .views import home_view, dashboard_view, api_data_view, api_data_view_2, api_data_view_4, api_data_view_5
from users.views import login_view, register_view, logout_view, confirm_email_view

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register_view),
    path('logout/', logout_view, name="logout"),
    path('confirm-email/<uidb64>/<token>/', confirm_email_view, name='confirm_email'),
    path('dashboard', dashboard_view, name="dashboard"),
    path('api-data/', api_data_view, name='api-data'),
    path('api-data2/', api_data_view_2, name='api-data2'),
    path('api-data4/', api_data_view_4, name='api-data4'),
    path('mvoh-result/', api_data_view_5, name='api-data5'),
    path('runs/', include('runs.urls')),
    path('mvoh/', include('mvoh.urls')),
    path('m2/', include('m2.urls')),
    path('m3/', include('m3.urls')),
    path('m4/', include('m4.urls')),
    path('m5/', include('m5.urls')),
    path('m6/', include('m6.urls')),
    path('m7/', include('m7.urls')),
    path('m8/', include('m8.urls')),
    path('rebalancing/', include('rebalancing.urls')),
    path('users/', include('users.urls')),
    path('tickers/', include('tickers.urls')),
    path('admin/', admin.site.urls),
]
