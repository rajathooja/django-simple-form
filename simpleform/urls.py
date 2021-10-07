from django.urls import path
from .views import homepage

# this is our app specific url pattern to call the main function when loading the index.html page
urlpatterns = [
    path('', homepage, name='home')
]
