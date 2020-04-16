from django.shortcuts import render, redirect
from django.http import HttpResponse
from .api_weather import make_request_name, make_request_lat_long,\
    detect_location, make_request_hourly_city_id
from .models import Image_Theme

def index(request):
    if request.method == 'POST':
        location = make_request_name(city_name= request.POST['city_name_input'])
        try:
            location_hourly = make_request_hourly_city_id(location['id'])
                # fetches the jason file of hourly forecast
        except:
            print('Not available')
        try:
            img_query_set = Image_Theme.objects.filter(image_theme_id=location['weather'][0]['icon'])
            # fetches a particular row of Image_Theme table
        except:
            print('Not available')


        try:
            for i in img_query_set:
                if i.image_theme:
                    img = i.image_theme  # image from the row
        except:
            print('---------error-2------------')

        try:
            return render(request, 'location_result.html',
                          {'location': location,
                           'image_theme': img,
                           'details_hourly': location_hourly})
        except:
            return HttpResponse('Sorry cannot show the.' +
                                '\n Type the city correctly or check your' +
                                'internet connection.')
    else:
        current_location_details = detect_location()
            # fetches location using ip addresss

        current_location = make_request_lat_long(lat = current_location_details[0],
                                             long = current_location_details[1])
            # fetches the json file
        return render(request, 'index.html', {'current_location': current_location})

def location_result(request):
    pass