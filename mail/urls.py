from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',views.index,name='index'),
    path('logincheck',views.logincheck,name='home'),
    path('logincheck', views.logincheck, name='loginfail'),
    path('logincheck', views.logincheck, name='logincheck'),
    path('compose',views.compose,name='compose'),
    path('inbox',views.inbox,name='inbox'),
    path('sent',views.sent,name='sent'),
    path('logout',views.logout,name='logout'),
    path('compose1',views.compose1,name='compose1'),
    path('newuser', views.newuser, name='newuser'),
    path('newuser1',views.newuser1,name='index')
]
urlpatterns+=staticfiles_urlpatterns()