import requests

# Enter your OpenWeatherMap API Key here
API_KEY = 'Enter Your Own API Key'

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # For Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()   # Raise error for bad status
        
        data = response.json()
        
        # Extracting required information
        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        
        print("\n Weather Report")
        print("----------------------")
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc}")
        print(f"Wind Speed: {wind_speed} m/s")
        
    except requests.exceptions.HTTPError:
        print(" City not found or API error!")
    except requests.exceptions.ConnectionError:
        print(" Network error. Check your internet connection.")
    except Exception as e:
        print(" Something went wrong:", e)


# Take input from user
city = input("Enter city name: ")
get_weather(city)

