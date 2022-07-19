"""
    Name: nws_console.py
    Author:
    Created:
    Purpose: OOP console app
    Get weather data from the National Weather Service
"""
# Openweather map url, api key, and other weather utilities
import nws_class

#-------------------------------- MENU -------------------------------------#


def menu():
    """
        Print menu for user, return menu choice
    """
    print("-"*75)
    print(f"[1] Get latest weather observation")
    print(f"[2] Get 12 hour forecast")
    print(f"[3] Get 7 day forecast")
    print(f"[4] Get 7 day detailed forecast")
    print(f"[5] Get active weather alerts")
    print(f"[6] Get weather alerts")
    print(f"[9] Get new location")
    menu_choice = input(f"[Enter] to quit. Enter your choice: ")
    return menu_choice


#-------------------------- MAIN PROGRAM ----------------------------#
def main():
    # Create weather object
    weather = nws_class.WeatherClass()
    # Get the location from the user
    weather.get_location()
    # Menu loop
    while True:
        # Display menu choices
        menu_choice = menu()

        # If the user presses the enter key, exit program
        if menu_choice == "":
            # Exit loop
            break

        # Get current weather and air quality
        elif menu_choice == "1":
            weather.clear_console()
            weather.get_latest_weather_observation()
            weather.process_latest_weather_observation()
            weather.display_latest_weather_observation()

        # Get 12 hour forecast
        elif menu_choice == "2":
            weather.clear_console()
            weather.get_hourly_forecast()
            weather.display_twelve_hour_forecast()

        # Get 7 day forecast
        elif menu_choice == "3":
            weather.clear_console()
            weather.get_7_day_forecast()
            weather.display_7_day_forecast()

        # Get and display 7 day detailed forecast
        elif menu_choice == "4":
            weather.clear_console()
            weather.get_7_day_forecast()
            weather.display_7_day_detailed_forecast()

        # Get and display active weather alerts
        elif menu_choice == "5":
            weather.clear_console()
            weather.get_active_weather_alerts()
            weather.display_active_weather_alerts()

        # Get and display weather alerts
        elif menu_choice == "6":
            weather.clear_console()
            weather.get_weather_alerts()
            weather.display_weather_alerts()

        # Make API call for a new location
        elif menu_choice == "9":
            weather.clear_console()
            weather.get_location()

    # Say goodbye to the user as the program exits
    weather.goodbye()


main()
