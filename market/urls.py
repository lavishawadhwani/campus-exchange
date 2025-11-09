 
 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('categories/', views.categories, name='categories'),  # Categories page
    path('add/', views.add_listing, name='add_listing'),  # Add Listing
    path('contact/', views.contact_view, name='contact'),  # Contact page
]
  
 

 
