from django.shortcuts import render, HttpResponse
from newsletter.models import SubscribersEmail
# Create your views here.

def add_to_subscribers_list(request):
    if 'SubscriberEmail' in request.POST:
        email = request.POST['SubscriberEmail']
        SubscribersEmail(email=email).save()
        return render(request, 'newsletter/subscription_success.html', {'email':email})