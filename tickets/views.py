from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

# 1 To send as json  (without model and without rest )
def no_rest_no_model(request):
    data = [
        {
            "id": 1,
            "name": "khaled",
            "age": "21",
        },
        {
            "id": 2,
            "name": "shams",
            "age": "18",
        },
        {
            "id": 3,
            "name": "fathy",
            "age": "12",
        }
    ]
    return JsonResponse(data, safe=False)


# 2 To send as json ( model and without rest )
def model_no_rest(request):
    GustObject = Gust.objects.all()
    
    data = {
        "data ": list(GustObject.values("name", "mobile"))
    }
    return JsonResponse(data, safe=True)
