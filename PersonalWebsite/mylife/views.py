from django.shortcuts import render
from mylife.models import Event
# Create your views here.


def event_list(request):
    events = Event.objects.all().order_by('date')

    template_name = 'mylife/event_list.html'
    context = {
        'events':events
    }
    return render(request, template_name, context)