from urllib.error import URLError

from django.contrib.gis.db import models 
from django.contrib.gis import geos
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderQueryError



class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    location = models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save(self, **kwargs):
        if not self.location:
            address = u'%s %s' % (self.city, self.address)
            address = address.encode('utf-8')
            geocoder = Nominatim()
            try:
                _, latlon = geocoder.geocode(address)
            except (URLError, GeocoderQueryError, ValueError):
                pass
            else:
                point = "POINT(%s %s)" % (latlon[1], latlon[0])
                self.location = geos.fromstr(point)
        super(Shop, self).save()
    

