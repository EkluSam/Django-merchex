"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from listings import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    path('hello/', views.hello),
    path('about-us/', views.about_us, name='about-us'),

    # listings
    path('listings/', views.listing_list, name='listing-list'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/add/', views.listing_create, name='listing-create'),
    path('listings/<int:id>/change', views.listing_change, name='listing-change'),
    path('listings/<int:id>/delete', views.listing_delete, name='listing-delete'),
    
    # bands
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create,name='band-create'),
    path('bands/<int:id>/change/', views.band_change, name='band-change'),
    path('bands/<int:id>/delete', views.band_delete, name='band-delete'),

    # contact
    path('contact/', views.contact, name='contact'),    
    path('contact/email-sent/', views.email_sent, name='email-sent'),
]
