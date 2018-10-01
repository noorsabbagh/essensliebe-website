# Imports required libraries and modules
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from geographiclib.geodesic import Geodesic
from diblogeo import Geo

# Creates new geolocator object using Nominatim.
geolocator = Nominatim(user_agent='app_demo')

# Method to convert address to geolocation, takes address parameter, returns long and lat.
def address_to_geolocation(address):
    location = geolocator.geocode(str(address))
    lat,lon = location.latitude, location.longitude
    return(lat,lon)

# Calculates the radius between the two matched users by halving the distance.
def radius_calc(address1,address2): 
    my_dist = distance_calc(address1,address2)
    radius = int(my_dist/2)
    return(radius)

# Calculates distance between two points then generates distance used for circumfrence which is
# then returned in kms.
def distance_calc(address1,address2): 
    my_dist = great_circle(address1,address2).kilometers
    return(my_dist)

# Calculates the bearing degree from start coordinates towards end coordinates 
def bearing_calc(lat1,lon1,lat2,lon2):
    geo_calc = Geodesic.WGS84.Inverse(lat1,lon1,lat2,lon2)
    bearing = geo_calc['azi1']
    return(bearing)

# Calculates the coordinates of the centre point using bearing and distance
def centre_point_calc(lt1,ln1,b,d):
    point = Geo((lt1, ln1))
    destination = point.destination(bearing=b, kilometers=d)
    return(destination)
