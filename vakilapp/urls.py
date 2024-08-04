
from django.contrib import admin
from django.urls import path,include
from. import views
urlpatterns = [
    path('',views.index,name='index'),
    path('send_msg',views.send_msg,name='send_msg'),

    #admin urls
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_register',views.admin_register,name='admin_register'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_msg',views.admin_msg,name='admin_msg'),
    path('admin_team',views.admin_team,name='admin_team'),
    path('admin_alert',views.admin_alert,name='admin_alert'),
    path('admin_update',views.admin_update,name='admin_update'),
    path('logout_admin',views.logout_admin,name='logout_admine'),
    path("delete_msg",views.delete_msg,name='delete_msg'),
    path("add_team",views.add_team,name='add_team'),
    path("delete_team",views.delete_team,name='delete_team'),
    path("update_team/<id>/",views.update_team,name='update_team'),
]
