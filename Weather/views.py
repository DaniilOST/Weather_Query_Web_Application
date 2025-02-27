from django.shortcuts import render
from pyowm import OWM
from .forms import CityForm
from .models import WeatherRequest

def index(request):
    return render(request, 'Weather/index.html')


def get_weather(city):
    try:
        owm = OWM('87524422688b44a6e0d5475dc12c4939')
        mgr = owm.weather_manager()


        observation = mgr.weather_at_place(f'{city}')
        w = observation.weather

        w.detailed_status         # 'clouds'
        S = w.wind()['speed']                  # {'speed': 4.6, 'deg': 330}
        H = w.humidity                # 87
        T = w.temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        R = w.rain.get('3h', 0)                  # {}
        C = w.clouds                  # 75
        
        weather_request = WeatherRequest(
            city=city,
            temperature=T,
            wind_speed=S,
            humidity=H,
            cloud_coverage=C,
            rain=R
        )
        weather_request.save()
        
        return round(T, 1), round(S, 1), round(R, 1), round(H, 1), round(C, 1)
    
    except Exception as e:
        print(f"Error occurred while fetching weather data: {e}")
        return None, None, None, None, None

def main_page(request):
    current_wind = None
    current_temp = None
    current_rain = None
    current_humidity  = None
    current_clouds  = None
    city = None
    

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            current_temp, current_wind, current_rain, current_humidity, current_clouds = get_weather(city)
    else:
        form = CityForm()

    context = {
        'form': form,
        'current_temp': current_temp,
        'current_wind': current_wind,
        'current_rain': current_rain,
        'current_humidity': current_humidity,
        'current_clouds': current_clouds,
        'city': city,
    }
    return render(request, 'Weather/index.html', context=context)

def weather_history(request):
    
    weather_requests = WeatherRequest.objects.all().order_by('-timestamp')

    context = {
        'weather_requests': weather_requests
    }

    return render(request, 'Weather/weather_history.html', context)