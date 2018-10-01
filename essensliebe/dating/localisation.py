# Imports required libraries and modules
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from geographiclib.geodesic import Geodesic
from diblogeo import Geo
import requests, json
from googleplaces import GooglePlaces, types

# Creates new geolocator object using Nominatim.
geolocator = Nominatim(user_agent='app_demo')
# google places api key
api_key = 'AIzaSyCXmfyVfwPypP1HwUnVE1LMKbqqz6heipk'
google_places = GooglePlaces(api_key)

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

# Finds nearby restaurants by using location, radius and types parameters.
# Location: lat and long of the centre point between the matched users.
# Radius: the radius is half of the distance between the matched users.
# Types: the type of etablishment to be searched, such as 'restaurant'.
def find_nearby_places(lat, lon, radius):
    AUTH_KEY = api_key
    LOCATION = str(lat) + "," + str(lon)
    RADIUS = radius
    TYPES = 'restaurant'
    MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
            '?location=%s'
            '&radius=%s'
            '&type=%s'
            '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
    # Grabs the JSON result
    print(MyUrl)
    response = requests.get(MyUrl)
    json_data = json.loads(response.text)
    return(json_data)

# Same method as above, but uses a wrapped version of the google places API.
# Takes 3 perameters: lat and long of the centre point, and radius of search.
def find_restaurants(lat, lon, rad):
    print(lat,lon,rad,types.TYPE_RESTAURANT)
    query_result = google_places.nearby_search(
        lat_lng={'lat':lat,'lng':lon},
        radius=rad, types=[types.TYPE_RESTAURANT])
    # If query has results then print.
    if query_result.has_attributions:
        print(query_result.places)