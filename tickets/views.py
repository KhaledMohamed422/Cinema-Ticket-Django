from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import * 
from .models import *
from rest_framework import status, filters
# Create your views here.
# List == GET
# Create == POST
# pk query == GET 
# Update == PUT
# Delete destroy == DELETE


# 1 To send as json  (without model and without rest )
def no_rest_no_model(request):
    response = [
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
    return JsonResponse(response, safe=False)

# 2 To send as json ( model and without rest )
def model_no_rest(request):
    GustObject = Gust.objects.all()
    
    response = {
        "data ": list(GustObject.values("name", "mobile"))
    }
    return JsonResponse(response, safe=True)

# 3.1 GET POST with restfreamwork
@api_view(["GET","POST"])
def Get_List_Post_Data(request):
    # GET
    if request.method == "GET":
        queryListGust = Gust.objects.all()
        serializer = GustSerializer(queryListGust,many=True)
        
        return Response(serializer.data)    
    # POST
    elif request.method == "POST":
        serializer = GustSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
        
       
