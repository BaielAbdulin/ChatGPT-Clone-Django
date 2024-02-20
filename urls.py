from django.urls import path
from . import views

# Define url patterns to the page
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('chatbot', views.chatbot, name='chatbot'),
]