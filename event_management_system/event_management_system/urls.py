"""
URL configuration for event_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/register/', views.register_event, name='register_event'),
    path('<int:event_id>/schedule/', views.event_schedule, name='event_schedule'),
    path('<int:event_id>/speakers/', views.speakers, name='speakers'),
    path('<int:event_id>/gallery/', views.gallery, name='gallery'),
    path('<int:event_id>/feedback/', views.feedback, name='feedback'),
    path('search/', views.search_event, name='search_event'),
    path('filter/<str:category>/', views.filter_events, name='filter_events'),
]
