"""
    Name: one_call_class.py
    Author:
    Created:
    Purpose: OOP console app
    Get lat and lon from Openweather map current weather
    Use lat and lon for One Call Weather
"""

import requests
import textwrap
import weather_utils
# import geocode_owm for reverse geocode
import geocode_geopy
from datetime import datetime


class WeatherClass:
    def __init__(self):
        """ Initialize object """
        print(weather_utils.title("Welcome to Bill's NWS Weather App!"))
        self.__decorator_width = 75

#--------------------------------- GET LOCATION -------------------------------------#
    def get_location(self):
        """
            Get weather location and weather information
        """
        # try:
        # Get location input from user
        lat, lng, address = geocode_geopy.geocode()
        print(address)

        # Get the gridpoints from lat and lng
        points_url = weather_utils.NWS_ENDPOINT + "/points/" + \
            str(lat) + "," + str(lng)

        # Get the gridpoints response
        response = requests.get(points_url)

        # Get gridpoints dictionary
        if(response.status_code == 200):
            print("[+] The connection to the National Weather Service was successful.")
            # Get the gridpoints dictionary
            grid_points_dict = response.json()
            # \r return to the beginning of the line before printing
            # , end="" Print on the same line
            print(f"\r[+] [#      ]", end="")

            # Get the forecast url from the gridpoints dictionary
            forecast_url = grid_points_dict.get("properties").get("forecast")

            # station_url = grid_points.get("properties").get("observationStations")
            response = requests.get(forecast_url)
        else:
            print("[-] Did not get NWS Gridpoints")

        # Get 7 day forecast dictionary
        if(response.status_code == 200):
            # Get forecast dictionary
            forecast_dict = response.json()
            print(f"\r[+] [##     ]", end="")
            self.forecast_list = forecast_dict.get("properties").get("periods")

            # Get observation station URL
            forecast_hourly_url = grid_points_dict.get(
                "properties").get("forecastHourly")
            response = requests.get(forecast_hourly_url)
        else:
            print(
                f"[-] Did not get NWS 7 Day Forecast - Response: {response.status_code}")

        # Get hourly forecast
        if(response.status_code == 200):
            # Get forecast dictionary
            forecast_hourly_dict = response.json()
            print(f"\r[+] [###    ]", end="")
            self.forecast_hourly_list = forecast_hourly_dict.get(
                "properties").get("periods")

            # Get observation station URL
            stations_url = grid_points_dict.get(
                "properties").get("observationStations")
            response = requests.get(stations_url)
        else:
            print(
                f"[-] Did not get NWS Hourly Forecast - Response: {response.status_code}")

        # Get observation station ids
        if(response.status_code == 200):
            # Get station dictionary
            self.station_dict = response.json()
            print(f"\r[+] [####   ]", end="")
            # Get first station id in list
            self.station_id = self.station_dict.get("features")[0].get(
                "properties").get("stationIdentifier")

            observations_url = weather_utils.NWS_ENDPOINT + \
                "stations/" + self.station_id + "/observations/latest"
            response = requests.get(observations_url)
        else:
            print(
                f"[-] Did not get Station ID - - Response: {response.status_code}")

        # Get latest observation from station
        if(response.status_code == 200):
            # Get latest observation dictionary
            self.weather_dict = response.json()
            print(f"\r[+] [#####  ]", end="")
        else:
            print(
                f"[-] Did not get NWS latest weather observation - Response: {response.status_code}")

        # Get weather alerts for the area
        if(response.status_code == 200):
            alerts_url = f"https://api.weather.gov/alerts?point={lat},{lng}"
            response = requests.get(alerts_url)
            print(f"\r[+] [###### ]", end="")
            self.alert_dict = response.json()
            active_alerts_url = f"https://api.weather.gov/alerts/active?point={lat},{lng}"
            response = requests.get(active_alerts_url)
            print(f"\r[+] [#######]")
            self.active_alert_dict = response.json()
        else:
            print(
                f"[-] Did not get NWS Weather Alerts - Response: {response.status_code}")

#-------------------------- GET ACTIVE WEATHER ALERTS ----------------------------#
    def get_active_weather_alerts(self):
        """ Get weather alerts  """
        print("="*self.__decorator_width)
        print(f"National Weather Service Active Weather Alerts")
        # print(f"{self.__address}")
        print("="*self.__decorator_width)
        # print(self.alert_dict.get("features")[0].get("properties").get("areaDesc"))
        active_alert_list = self.active_alert_dict.get("features")[:]

        # If active weather alert list is not empty
        if active_alert_list != []:
            for alert in active_alert_list:
                area = alert.get("properties").get("areaDesc")
                headline = alert.get("properties").get("headline")
                description = alert.get("properties").get("description")

                effective = alert.get("properties").get("effective")
                effective = datetime.fromisoformat(effective)
                effective = effective.strftime(
                    "%m/%d/%Y, %I:%M %p")  # , %-I:%M %p

                expires = alert.get("properties").get("expires")
                expires = datetime.fromisoformat(expires)
                expires = expires.strftime("%m/%d/%Y, %I:%M %p")  # , %-I:%M %p

                wrapper = textwrap.TextWrapper(width=70)
                area = wrapper.fill(text=area)
                headline = wrapper.fill(text=headline)
                description = wrapper.fill(text=description)

                print("*" * 70)
                print(f"Effective: {effective}")
                print(f"Expires: {expires}")
                print(f"{area}")
                print(f"{headline}")
                print(f"{description}")
                input("Press the enter key for the next alert")
        else:
            print("There are no weather alerts at this time.")

#-------------------------- GET WEATHER ALERTS ----------------------------#
    def get_weather_alerts(self):
        """ Get weather alerts  """
        print("="*self.__decorator_width)
        print(f"National Weather Service Weather Alerts")
        # print(f"{self.__address}")
        print("="*self.__decorator_width)
        # print(self.alert_dict.get("features")[0].get("properties").get("areaDesc"))
        alert_list = self.alert_dict.get("features")[:]

        # If weather alert list is not empty
        if alert_list != []:
            for alert in alert_list:
                area = alert.get("properties").get("areaDesc")
                headline = alert.get("properties").get("headline")
                description = alert.get("properties").get("description")

                effective = alert.get("properties").get("effective")
                effective = datetime.fromisoformat(effective)
                effective = effective.strftime(
                    "%m/%d/%Y, %I:%M %p")  # , %-I:%M %p

                expires = alert.get("properties").get("expires")
                expires = datetime.fromisoformat(expires)
                expires = expires.strftime("%m/%d/%Y, %I:%M %p")  # , %-I:%M %p

                wrapper = textwrap.TextWrapper(width=70)
                area = wrapper.fill(text=area)
                headline = wrapper.fill(text=headline)
                description = wrapper.fill(text=description)

                print("*" * 70)
                print(f"Effective: {effective}")
                print(f"Expires: {expires}")
                print(f"{area}")
                print(f"{headline}")
                print(f"{description}")
                input("Press the enter key for the next alert")
        else:
            print("There are no weather alerts at this time.")

#-------------------------- GET 12 HOUR FORECAST ----------------------------#
    def get_twelve_hour_forecast(self):
        """ Get hourly forecast """
        print("="*self.__decorator_width)
        print(
            f"National Weather Service 12 Hour Weather Forecast")
        # print(f"{self.__address}")
        print("="*self.__decorator_width)
        # Slice 12 hours out of the hourly forecast list
        hourly_slice = self.forecast_hourly_list[:12]
        # Iterate through each item in the forecast list
        for forecast_item in hourly_slice:
            start_time = forecast_item.get("startTime")
            temperature = forecast_item.get("temperature")
            wind_speed = forecast_item.get("windSpeed")
            wind_direction = forecast_item.get("windDirection")
            short_forecast = forecast_item.get("shortForecast")
            time = datetime.fromisoformat(start_time)
            time = time.strftime('%I:%M %p')
            print(
                f"{time:>8}: {temperature:>5.1f}°F | {wind_speed:>8} | {wind_direction:>5} | {short_forecast}")

#-------------------------- GET LATEST WEATHER OBSERVATION ----------------------------#
    def get_weather(self):
        """ Get latest observation from the closest NWS station """
        # Get nearest stationid
        self.station_name = self.station_dict.get(
            "features")[0].get("properties").get("name")

        # Get latest weather observation from dictionary
        # Shorten up weather observations dictionary code
        weather_obs = self.weather_dict.get("properties")

        self.__description = weather_obs.get("textDescription")

        temperature = weather_obs.get("temperature").get("value")
        self.__temperature = weather_utils.celsius_to_fahrenheit(temperature)

        dewpoint = weather_obs.get("dewpoint").get("value")
        if not (dewpoint is None):
            self.__dewpoint = round(dewpoint, 1)
        else:
            self.__dewpoint = "NA"

        humidity = weather_obs.get("relativeHumidity").get("value")
        if not (humidity is None):
            self.__humidity = round(humidity)
        else:
            self.__humidity = "NA"

        wind_speed = weather_obs.get("windSpeed").get("value")
        if not (wind_speed is None):
            # Convert kph to mph
            self.__wind__speed = round(wind_speed * .62137, 1)
        else:
            self.__wind__speed = "NA"

        wind_direction = weather_obs.get("windDirection").get("value")
        if not (wind_direction is None):
            # Convert kph to mph
            self.__degree = wind_direction
            self.__wind_cardinal = weather_utils.degrees_to_cardinal(
                wind_direction)
        else:
            self.__degree = "NA"
            self.__wind_cardinal = "NA"

        pressure = weather_obs.get("barometricPressure").get("value")
        if not (pressure is None):
            # Convert pascals to inches of mercury inHg
            self.__pressure = round(pressure / 3386, 2)
        else:
            self.__pressure = "NA"

        visibility = weather_obs.get("visibility").get("value")
        if not (visibility is None):
            self.__visibility = round((visibility * 3.28084) / 5280)
        else:
            self.__visibility = "NA"

        windchill = weather_obs.get("windChill").get("value")
        if not (windchill is None):
            # Convert meters to miles
            self.__windchill = weather_utils.celsius_to_fahrenheit(windchill)
        else:
            self.__windchill = "NA"

        heatindex = weather_obs.get("visibility").get("value")
        if not (pressure is None):
            # Convert meters to miles
            self.__heatindex = round(heatindex * 0.000621371)
        else:
            self.__heatindex = "NA"

        elevation = weather_obs.get("elevation").get("value")
        if not (elevation is None):
            # Convert meters to miles
            self.__elevation = round(elevation * 3.28084)
        else:
            self.__elevation = "NA"

#-------------------------- DISPLAY LATEST WEATHER OBSERVATION ----------------------------#
    def display_weather(self):
        WIDTH = 15
        print("="*self.__decorator_width)
        print(f"National Weather Service Latest Weather Observations")
        print(f"Station: {self.station_id} {self.station_name}")
        print("="*self.__decorator_width)
        print(f"{self.__description}")
        print(f"{'Temperature:':{WIDTH}} {self.__temperature}°F")
        print(f"{'Dew Point:':{WIDTH}} {self.__dewpoint}°F")
        print(f"{'Humidity:':{WIDTH}} {self.__humidity}%")
        print(
            f"{'Wind:':{WIDTH}} {self.__wind__speed} mph  {self.__degree}°  {self.__wind_cardinal}")
        print(f"{'Pressure:':{WIDTH}} {self.__pressure} inHg")
        print(f"{'Visibility:':{WIDTH}} {self.__visibility} mi")
        print(
            f"{'WindChill:':{WIDTH}} {self.__windchill}°F         {'Heat Index:'} {self.__heatindex}°F")
        print(f"{'Elevation:':{WIDTH}} {self.__elevation} feet")

#-------------------------- GET 7 DAY FORECAST ----------------------------#
    def get_forecast(self):
        print("="*self.__decorator_width)
        print(
            f"National Weather Service 7 Day Weather Forecast")
        # print(f"{self.__address}")
        print("="*self.__decorator_width)

        # Iterate through each item in the forecast list
        for forecast_item in self.forecast_list:
            # start_time = forecast_item.get("startTime")
            name = forecast_item.get("name")
            temperature = forecast_item.get("temperature")
            wind_speed = forecast_item.get("windSpeed")
            wind_direction = forecast_item.get("windDirection")
            short_forecast = forecast_item.get("shortForecast")
            # detailed_forecast = forecast_item.get("detailedForecast")
            # time = datetime.fromisoformat(start_time)
            # time = time.strftime('%m-%d-%Y')
            # print(f"{name}: {detailed_forecast}")
            print(
                f"{name:<15} {temperature:>4}°F | {wind_speed:12} {wind_direction:5} | {short_forecast}")
            # print(f'{detailed_forecast}')

#-------------------------- GET 7 DAY DETAILED FORECAST ----------------------------#
    def get_detailed_forecast(self):
        print("="*self.__decorator_width)
        print(
            f"National Weather Service 7 Day Weather Forecast")
        # print(f"{self.__address}")
        print("="*self.__decorator_width)

        # Iterate through each item in the forecast list
        for forecast_item in self.forecast_list:
            # start_time = forecast_item.get("startTime")
            name = forecast_item.get("name")
            # temperature = forecast_item.get("temperature")
            # wind_speed = forecast_item.get("windSpeed")
            # wind_direction = forecast_item.get("windDirection")
            # short_forecast = forecast_item.get("shortForecast")
            detailed_forecast = forecast_item.get("detailedForecast")
            wrapper = textwrap.TextWrapper(width=60)
            detailed_forecast = wrapper.fill(text=detailed_forecast)
            # time = datetime.fromisoformat(start_time)
            # time = time.strftime('%m-%d-%Y')
            print(f"* {name}: {detailed_forecast}")
            # print(f"{temperature} °F | {wind_speed:5} {wind_direction}")
            # print(f'{detailed_forecast}')

#------------------------------- AIR QUALITY INDEX -------------------------------------#
    def get_air_quality_index(self):
        """ 
            Get Air Quality Index from OpenWeatherMap
        """
        params = {
            "lat": self.__latitude,
            "lon": self.__longitude
        }
        # Build request with url and parameters
        url = weather_utils.AQI_ENDPOINT
        response = requests.get(url, params)
        # print(response.text)

        # If the status_code is 200, successful connection and data
        if(response.status_code == 200):
            # Load json response into __weather dictionary
            data = response.json()
            # Get Air Quality Index
            self.__aqi = data.get("list")[0].get("main").get("aqi")

            # Convert AQI to text
            if self.__aqi == 1:
                self.__aqi_string = "Good"
            elif self.__aqi == 2:
                self.__aqi_string = "Fair"
            elif self.__aqi == 3:
                self.__aqi_string = "Moderate"
            elif self.__aqi == 4:
                self.__aqi_string = "Poor"
            elif self.__aqi == 5:
                self.__aqi_string = "Very Poor"
            else:
                self.__aqi_string = "No AQI Reading"
