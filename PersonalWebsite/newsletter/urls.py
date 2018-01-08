from django.urls import path
from newsletter.views import add_to_subscribers_list

urlpatterns = [
    path('subscribe/', add_to_subscribers_list, name = 'AddToSubscribersList'),
]
