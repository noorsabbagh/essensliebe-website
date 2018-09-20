from django.shortcuts import render
from geopy.geocoders import Nominatim
import json

def date_view(request):
geolocator = Nominatim(user_agent="Essenslibe")
user_location = request.user.profile.location
location = geolocator.geocode(user_location)
print(location.address)

print((location.latitude, location.longitude))
(40.7410861, -73.9896297241625)
print(location.raw)

return render(request, 'dating.html', context)