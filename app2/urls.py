"""second_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import  path

from app2 import views

urlpatterns = [

    #_______________________admin_________________

    path('',views.login,name='login'),
    path('login_code',views.login_code,name='login_code'),
    path('logout',views.logout,name='logout'),
    path('farmer_Registration',views.farmer_Registration,name='farmer_Registration'),
    path('Farmer_registration_post',views.Farmer_registration_post,name='Farmer_registration_post'),
    path('user_registration',views.user_registration,name='user_registration'),
    path('user_registration_post',views.user_registration_post,name='user_registration_post'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('view_user',views.view_user,name='view_user'),
    path('view_complaint',views.view_complaint,name='view_complaint'),
    path('search_date_view_complaint',views.search_date_view_complaint,name='search_date_view_complaint'),
    path('send_reply/<int:id>',views.send_reply,name='send_reply'),
    path('admin_send_reply',views.admin_send_reply,name='admin_send_reply'),
    path('view_accept_farmer',views.view_accept_farmer,name='view_accept_farmer'),
    path('view_farmer_and_verify',views.view_farmer_and_verify,name='view_farmer_and_verify'),
    path('acceptfarm/<int:id>',views.acceptfarm,name='acceptfarm'),
    path('rejectfarm/<int:id>',views.rejectfarm,name='rejectfarm'),

    #__________________________________farmer_________________________

    path('farmer_home', views.farmer_home, name='farmer_home'),
    path('add_new_product', views.add_new_product, name='add_new_product'),
    path('farmer_edit_product/<int:id>', views.farmer_edit_product, name='farmer_edit_product'),
    path('edit_product', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('farmer_manage_product', views.farmer_manage_product, name='farmer_manage_product'),
    path('add_new_product_post', views.add_new_product_post, name='add_new_product_post'),
    path('farmer_view_feedback_and_rating', views.farmer_view_feedback_and_rating, name='farmer_view_feedback_and_rating'),
    path('farmer_view_complaint_and_view_reply', views.farmer_view_complaint_and_view_reply, name='farmer_view_complaint_and_view_reply'),
    path('farmer_reply/<int:id>', views.farmer_reply, name='farmer_reply'),
    path('farmer_send_reply',views.farmer_send_reply, name='farmer_send_reply'),
    path('send_notification', views.send_notification, name='send_notification'),
    path('farmer_send_noti', views.farmer_send_noti, name='farmer_send_noti'),
    path('search_product', views.search_product,name='search_product'),
    path('search_feedback_and_rating', views.search_feedback_and_rating, name='search_feedback_and_rating'),
    path('search_date_complaint_reply', views.search_date_complaint_reply, name='search_date_complaint_reply'),
    path('farmer_view_profile', views.farmer_view_profile, name='farmer_view_profile'),
#______________________________________user________________________________________

    path('user_home', views.user_home, name='user_home'),
    path('view_product', views.view_product, name='view_product'),
    path('search_user_view_product', views.search_user_view_product, name='search_user_view_product'),
    path('send_rating_and_feedback',views.send_rating_and_feedback, name='send_rating_and_feedback'),
    path('user_send_rating_feedback',views.user_send_rating_feedback, name='user_send_rating_feedback'),
    path('send_complaint_user',views.send_complaint_user, name='send_complaint_user'),
    path('send_complaint',views.send_complaint, name='send_complaint'),
    path('search_complaint_product',views.search_complaint_product, name='search_complaint_product'),
    path('search_product_rating_fb',views.search_product_rating_fb, name='search_product_rating_fb'),
    path('view_product_rating_and_feedback',views.view_product_rating_and_feedback, name='view_product_rating_and_feedback'),
    path('user_complaint_to_farmer',views.user_complaint_to_farmer, name='user_complaint_to_farmer'),
    path('view_notification',views.view_notification, name='view_notification'),




]
