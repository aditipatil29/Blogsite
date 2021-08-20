
#from django.contrib import admin
from . import views
from django.urls import path

#namespace
app_name='home'

urlpatterns = [
    path('posts/author/',views.post_by_user,name='post_by_user'),
    path('posts/archive/monthly/',views.archive_monthly,name='archive_monthly'),
    path('posts/archive/yearly/',views.archive_yearly,name='archive_yearly'),
    path('posts/id/<int:post_id>',views.post_by_id,name='post_by_id'),
    path('index/',views.index,name='index'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.loginuser,name='loginuser'),
    path('post/', views.post,name='post'),
    path('logout/',views.logoutuser,name='logout'),
    path('contactus/',views.contactus,name='contactus'),
    path('',views.home_view,name='home_view'),
    path('overview/',views.overview,name='overview'),
    path('posts/',views.posts,name='posts'),
    path('insights/',views.insights,name='insights'),
    
]
