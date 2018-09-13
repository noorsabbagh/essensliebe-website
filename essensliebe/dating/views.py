from django.shortcuts import render
from . import zomato_api
import json


# Create your views here.
def date_view(request):
    
    config={
        "user_key":"0af766e8f013b40c87691e93e0dd63a1"
    }

    zomato  = zomato_api.initialize_app(config)

    user_location = request.user.profile.location
    city_ID = zomato.get_city_ID(user_location)
    collections = zomato.get_collections(city_ID)

    cuisines = json.dumps(collections, indent=4, sort_keys=True)
    context = {
        'cuisines': cuisines,
    }

    return render(request, 'dating.html', context)