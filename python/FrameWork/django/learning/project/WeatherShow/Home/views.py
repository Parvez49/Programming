from django.shortcuts import render

# Create your views here.

import json
import urllib.request

def index(request):

    if request.method=='POST':
        city=request.POST['city']
        link=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b3a1addd97c8e5edf11b08cd7a30c1ca').read()
        js_data=json.loads(link)
        data={
            "country_code": str(js_data['sys']['country']),
            "coordinate": str(js_data['coord']['lon'])+ ' '+ str(js_data['coord']['lat']),
            "temp": str(js_data['main']['temp'])+'k',
            "pressure": str(js_data['main']['pressure']),
            "humidity": str(js_data['main']['humidity']),
        }
    else:
        data={}
        city=''
    return render(request,'index.html',{'data':data,'city':city})