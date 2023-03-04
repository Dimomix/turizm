def tours(request):
    tours = Tour.objects.all()
    return render(request, 'tours.html', {'tours': tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})

def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

def cities(request):
    cities = City.objects.all()
    return render(request, 'cities.html', {'cities': cities})

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'city_detail.html', {'city': city})

def places(request):
    places = Place.objects.all()
    return render(request, 'places.html', {'places': places})

def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'place_detail.html', {'place': place}) 