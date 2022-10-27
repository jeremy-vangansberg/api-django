from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page),
    path('contact/', views.contact_page),
    path('about/', views.about_page, name='about'),
    path('special/', views.special_view, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
]
