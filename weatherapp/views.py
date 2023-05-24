from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def index(request):
    api_key = "63382a54a7369e8afacc7fe9fb8804c0"

    if(request.method == "POST"):
        city_name = request.POST['city']
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name + "&appid=" + api_key
        json_req = requests.get(url) 
        json_req = json_req.json()
        print(json_req)

        if(json_req['cod'] != "404" and json_req['cod'] != "400"):
            data = {
                'city_name' : json_req['name'],
                'weather' : json_req['weather'][0]['main'],
                'temper' : round(json_req['main']['temp'] - 273.15, 2),
                'icon' : json_req['weather'][0]['icon']
            }

            return render(request, 'weatherapp/home.html', data)
        
        else:
            data = {
                'city_name' : 'Not Found'
            }

            return render(request, 'weatherapp/home.html', data)
    
    else:
        return render(request, 'weatherapp/home.html')
    

        