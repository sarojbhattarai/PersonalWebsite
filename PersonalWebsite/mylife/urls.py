from django.urls import path
from mylife.views import event_list

urlpatterns = [
    path('', event_list, name='EventList'),
]