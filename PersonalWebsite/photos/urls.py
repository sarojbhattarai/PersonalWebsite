from django.urls import path
from photos.views import photo_list
urlpatterns = [
    path('', photo_list, name = 'PhotoList'),
]