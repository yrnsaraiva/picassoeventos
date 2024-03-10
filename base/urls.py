from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('events/', views.events, name='events'),
    path('event/<str:pk>/', views.eventDetails, name='event-details'),

    path('about/', views.about, name='about'),

    path('gallery', views.gallery, name='gallery'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('contact/', views.contactPage, name='contact')

    # path('profile/<str:pk>', views.userProfile, name='user-profile'),
    # path('update-user/', views.updateUser, name='update-user'),


]