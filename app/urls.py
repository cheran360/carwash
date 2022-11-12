from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('register', views.register, name='register'),
    path('homepage', views.homePage, name='home'),
    path('logout', views.logoutUser, name='logout'),
    path('showservices', views.showServices, name='showServices'),
    path('bookservice/<str:pk>',views.bookService, name='bookService'),
    path('showbookings', views.showBookings, name='showBookings'),
]