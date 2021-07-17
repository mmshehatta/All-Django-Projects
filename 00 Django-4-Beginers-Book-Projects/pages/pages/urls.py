
from django.urls import path #new 
from .views import HomePageView , AboutPageView #new


urlpatterns = [
    path('',HomePageView.as_view() , name='home'),
    path('about',AboutPageView.as_view(),name='about')
]
