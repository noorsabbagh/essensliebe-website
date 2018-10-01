# Imports required libraries and modules
from geopy.geocoders import Nominatim

# Creates new geolocator object using Nominatim.
geolocator = Nominatim(user_agent='app_demo')

# Method to convert address to geolocation, takes address parameter, returns long and lat.
def address_to_geolocation(address):
    location = geolocator.geocode(str(address))
    lat,lon = location.latitude, location.longitude
    return(lat,lon)