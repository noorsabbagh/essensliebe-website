# Imports required functions from geolocation module
from localisation import (
address_to_geolocation, 
radius_calc, 
bearing_calc, 
centre_point_calc,  
find_restaurants)
import zomato_api

config={
  "user_key":"0af766e8f013b40c87691e93e0dd63a1"
}
# Runs main method
def main():
    zomato  = zomato_api.initialize_app(config)
    # Ask for user input, request two addresses.
    # After input, convert addresses from strings to lat and long.
    address1 = "51 Cuthbert Drive Mill Park Melbourne"
    lat1, lon1 = address_to_geolocation(address1)
    address1_coordinates = (lat1, lon1)
    #print(address1_coordinates)

    address2 = "1 Barmah Street Manor Lakes Melbourne"
    lat2, lon2 = address_to_geolocation(address2)
    address2_coordinates = (lat2, lon2)
    #print(address2_coordinates)

    # Calculates bearing between the two matched users.
    bearing = bearing_calc(lat1,lon1,lat2,lon2)
    #print(bearing)

    # Calculates the radius between the two matched users.
    radius = radius_calc(address1_coordinates,address2_coordinates)

    # Calculates the coordinates of the centre point between the two matched users.
    destination = centre_point_calc(lat1,lon1,bearing,radius)
    d_lat = destination[0]
    d_lon = destination[1]

    # Finds nearby places within specified location coordinates and radius with place_type filter.
    print(zomato.get_nearby_restaurants(d_lat,d_lon))

# Runs main method
main()