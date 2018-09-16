# importing googlemaps module 
import googlemaps 
import math
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyCF7gO3hzQt5A0naY5AcN1nkF4CxgwVAJY') 
# Calculates distance between two points then generates distance used for circumfrence which is 
# then returned in kms
def localisation_calc(input1,input2): 
    my_dist = gmaps.distance_matrix(input1,input2)['rows'][0]['elements'][0]['distance']['value']
    radius = my_dist*math.pi
    radius_in_km = radius/1000
    print(radius_in_km)
# runs main method
def main():
    input1 = input("Please enter suburb/city 1: ")
    input2 = input("Please enter suburb/city 2: ")
    localisation_calc(str(input1),str(input2))
# Run main method
main()