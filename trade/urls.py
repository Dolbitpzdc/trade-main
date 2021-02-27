"""trade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
# from django.contrib.auth import views as userViews
admin.autodiscover()

urlpatterns = [
    # path('admin/changeActive/', views.changeActive, name='users_activ_deactiv'),
    # path('admin/changeActive/<id_user>/', views.changeActiveInfo, name='users_activ_deactiv_info'),


    path('admin/', views.moderViews, name='homeAdmin'),
    path('admin/form/', views.moderForms, name='form-common'),
    path('admin/new/person/', views.charts, name='charts'),
    path('admin/tables/', views.tables, name='tables'),
    path('admin/grid/', views.grid, name='grid'),
    path('admin/buttons/', views.buttons, name='buttons'),
    path('admin/interface/', views.interface, name='interface'),
    path('admin/error/', views.error, name='error'),
    path('admin/calendar/', views.calendar, name='calendar'),
    path('admin/activeUser/', views.activeUser),
    path('admin/deactiveUser/', views.deactiveUser),
    path('admin/login/', views.loginAdmin, name='loginAdmin'),
    path('admin/chat/', views.chat, name='chat'),

    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/provider/individ/', views.register_p_ind, name='register_p_ind'),
    path('login/provider/entity/', views.register_p_ent, name='register_p_ent'),
    path('login/buyer/individ/', views.register_z_ind, name='register_z_ind'),
    path('login/buyer/entity/', views.register_z_ent, name='register_z_ent'),

    path('api/log_in/', views.log_in, name='log_in'),
    path('api/registration/<type_reg>/', views.registration, name='registration'),

    path('home/', views.accaunt_home, name='home_accaunt'),
    path('login/home/bay/', views.bay, name='bay'),
    path('rates/', views.rates, name='rates'),
    path('help/', views.help, name='help'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
