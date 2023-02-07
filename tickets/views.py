from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

#1 way 1 to send as json without model and rest
def no_rest_no_model(request):
    data = [
        {
            "id" : 1,
            "name" : "khaled",
            "age"  : "21",
        },
        {
            "id" : 2,
            "name" : "shams",
            "age"  : "18", 
        },
        {
            "id" : 3,
            "name" : "fathy",
            "age"  : "12", 
        }
    ]
    return JsonResponse(data, safe=False)

    