from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('about/', views.about_page, name='about'),
    path('booking/', views.booking_page, name='booking'),
    path('contact/', views.contact_page, name='contact'),
    path('index/', views.index_page, name='index'),
    path('room/', views.room_page, name='room'),
    path('service/', views.service_page, name='service'),
    path('team/', views.team_page, name='team'),
    path('testimonial/', views.testimonial_page, name='testimonial'),
]
