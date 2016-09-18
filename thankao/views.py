from django.shortcuts import render_to_response
from apps.locations.models import City


def homepage(request):
    cities = City.objects.filter(visible=True)
    return render_to_response('index.html', {
        'cities': cities
    })
