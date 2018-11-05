
class Resteraunt:

    def __init__(self, id, name, cuisine, url, address ):
        self.id = id
        self.name = name
        self.cuisine = cuisine
        self.url = url
        self.address = address



class Address:

    def __init__(self, address, city, latitude, longitude, zipcode):
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.zipcode = zipcode
