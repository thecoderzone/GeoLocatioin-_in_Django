from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from .forms import LocationForm


def find_shops(request):
    form = LocationForm()  # Initialize the form

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            srid = form.cleaned_data['srid']
            user_location = Point(longitude, latitude, srid=srid)
            # Find the six nearest shops using GeoDjango's distance lookup
            shops = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[:6]
            return render(request, 'shops.html', {'shops': shops})

    return render(request, 'form.html', {'form': form})