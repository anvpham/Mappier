from django.shortcuts import render
from .forms import PlaceForm
from .models import Category
import googlemaps
import json
from django.http import Http404


def home(request):
    form = PlaceForm()
    categories = Category.objects.all()
    context = {'form': form, 'categories': categories}
    return render(request, 'home/home.html', context)


def search(request, category):
    _category = category
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            if len(category.split()) > 1:
                category = category.split()
                category = '_'.join(category).lower()
            else:
                category = category.lower()

            api_key = googlemaps.Client(key='AIzaSyBIcFOK0pRJXMQaXpE1NsFBrxnpK1Q5hMk')
            results = api_key.places(query=form['text'].value(), type=category, open_now=False)
            places = results['results']
            if places == []:
                return render(request, 'home/noresults.html')

            place_list = []
            for place in places:
                if place['rating'] != 0:
                    place_details = {
                        'name': place['name'],
                        'rating': str(place['rating']) + '/5',
                        'address': place['formatted_address'],
                    }
                else:
                    continue
                place_list.append(place_details)

            context = {'places': place_list, "category": _category.title(), "location": form['text'].value()}

            return render(request, 'home/results.html', context)
        else:
            raise Http404
    else:
        raise Http404
