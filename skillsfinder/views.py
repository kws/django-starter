from django.shortcuts import render
from skillsfinder.models import Person


def index(request):
    context = {
        'site_name': 'Skillsfinder',
        'people': Person.objects.all(),
    }
    return render(request, 'skillsfinder/index.html', context)
