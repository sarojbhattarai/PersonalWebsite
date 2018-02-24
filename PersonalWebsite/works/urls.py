from django.urls import path
from works.views import work_list
urlpatterns = [
    path('', work_list, name = 'WorkList'),
]