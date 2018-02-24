from django.shortcuts import render
from works.models import Work
# Create your views here.


def work_list(request):
    all_works = Work.objects.all()
    template_name = 'works/work_list.html'
    context = {
        'works' : all_works
    }

    return render(request, template_name, context)