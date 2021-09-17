"""
    Name: geocode_geopy.py
    Author: William A Loring
    Created: 07/10/2021
    Purpose: Geocode using Nominatim from geopy
    pip install geopy
"""

from geopy.geocoders import Nominatim

# For testing
# LAT = 41.8666
# LON = -103.6672


def main():
    # For testing
    geocode()
    # reverse_geocode(LAT, LON)


def geocode():
    try:
        # Create geolocator object with Nominatim geocode service
        # Nominatim is a free geolocater that uses openstreetmaps.org
        geolocator = Nominatim(user_agent="location_practice")

        # Get location input from user
        city = input("Enter city: ")
        state = input("Enter state: ")
        country = input("Enter country: ")

        # Create location dictionary for request
        location = {
            "city": city,
            "state": state,
            "country": country
        }

        geo_location = geolocator.geocode(location)
        # For testing purposes
        # print(geo_location.raw)
        # print(geo_location.address)
        #print((geo_location.latitude, geo_location.longitude))

        # Return geocode location information to calling program
        return (geo_location.latitude, geo_location.longitude, geo_location.address)
    except:
        print("An error occured while geocoding.")


def reverse_geocode(lat, lon):
    try:
        # Create geolocator object
        geolocator = Nominatim(user_agent="location_practice")
        # Create location tuple
        location = (lat, lon)
        # Get address with resolution of town
        address = geolocator.reverse(location, zoom=10)
        # print(address)
        return address
    except:
        print("An error occured while reverse geocoding.")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
