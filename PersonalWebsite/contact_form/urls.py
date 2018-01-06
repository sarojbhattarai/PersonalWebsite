from django.urls import path
from contact_form.views import contact

urlpatterns = [
    path('', contact, name = "Contact"),
]