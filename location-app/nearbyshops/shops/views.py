# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#moi
from django.views import generic
from django.contrib.gis.geos import fromstr

from django.contrib.gis.geos import Point

from django.contrib.gis.db.models.functions import Distance
from .models import Shop


# Create your views here.

longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)
class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'shops/index.html'
