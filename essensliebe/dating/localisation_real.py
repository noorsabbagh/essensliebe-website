# Imports required functions from geolocation module
from dating import localisation 
from dating import zomato_api
import json
from django.shortcuts import render


# Runs main method
def main(request):
    config={
  "user_key":"0af766e8f013b40c87691e93e0dd63a1"
}
    location = localisation.initialize_app()
    zomato  = zomato_api.initialize_app(config)
    # Ask for user input, request two addresses.
    # After input, convert addresses from strings to lat and long.
    address1 = request.user.profile.location
    lat1, lon1 = location.address_to_geolocation(address1)
    address1_coordinates = (lat1, lon1)
    #print(address1_coordinates)

    address2 = "1 Barmah Street Manor Lakes Melbourne"
    lat2, lon2 = location.address_to_geolocation(address2)
    address2_coordinates = (lat2, lon2)
    #print(address2_coordinates)

    # Calculates bearing between the two matched users.
    bearing = location.bearing_calc(lat1,lon1,lat2,lon2)
    #print(bearing)

    # Calculates the radius between the two matched users.
    radius = location.radius_calc(address1_coordinates,address2_coordinates)

    # Calculates the coordinates of the centre point between the two matched users.
    destination = location.centre_point_calc(lat1,lon1,bearing,radius)
    d_lat = destination[0]
    d_lon = destination[1]

    # Finds nearby places within specified location coordinates and radius with place_type filter.
    resteraunts = zomato.get_nearby_restaurants(d_lat,d_lon)
    print(type(resteraunts))
    test = resteraunts
    context = {
        'test': test
    }

    
    return render(request, 'dating.html', context)
    