from django.urls import path
from . import views

urlpatterns = [
    path('login_1/', views.login_1,name='login_1'),
    path('register_1/', views.register_1,name='register_1'),
    path('about/', views.about,name='about_1'),
    path('dashboard_1/', views.dashboard_1,name='dashboard_1'),
    path('adddetails/', views.adddetails,name='add'),
    path('bookingrequest/', views.booking_requests, name='bookingrequest'),
    path('managedetails/', views.managedetails,name='manage'),
    path('edit_property/<int:id>', views.edit_property, name='edit-property'),
    path('update_property/<int:id>', views.update_property, name='update_property'),
    path('delete_property/<int:id>/', views.delete_property, name='delete_property')
    ,
    path('showdetails/<int:id>', views.showdetails, name='showdetails'),
    path('property-list/', views.property_list, name='property_list'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
