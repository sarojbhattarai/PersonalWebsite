from django.shortcuts import render
from photos.models import Photo
# Create your views here.


def photo_list(request):
    photos = Photo.objects.all().order_by('-published_on')
    template_name = 'photos/photo_list.html'
    context = {
        'photos':photos
    }
    return render(request, template_name, context)
