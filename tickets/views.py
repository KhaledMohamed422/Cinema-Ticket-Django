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
def fbv_no_rest_no_model(request):
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
    # Safe is false --> because the response data is a list of dictionaries, not a single dictionary
    return JsonResponse(response, safe=False)

# 2 To send as json ( model and without rest )


def fbv_model_no_rest(request):
    GustObject = Gust.objects.all()

    response = {
        "data ": list(GustObject.values("name", "mobile"))
    }
    return JsonResponse(response, safe=True)

# 3.1 GET POST with restfreamwork


@api_view(["GET", "POST"])
def fbv_get_list_post_data(request):
    # GET
    if request.method == "GET":
        queryListGust = Gust.objects.all()

        # serializer --> convert objecet of data to json as (dic)
        # instance --> to pass object that i want to convert it
        # many=True --> in the serializer function indicates that the data being serialized is a queryset that contains multiple objects, rather than a single object. This argument is used to indicate that multiple instances should be serialized and returned as a list of dictionaries, rather than a single dictionary representing a single object.
        serializer = GustSerializer(instance=queryListGust, many=True)

        # serializer.data --> json
        return Response(serializer.data)
    # POST
    elif request.method == "POST":
        # data=request.data --> To create a new object based of data
        serializer = GustSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 3.2 GET PUT DELETE with restfreamwork


@api_view(["GET", "PUT", "DELETE"])
def fbv_get_list_put_data_delete_data(request, pk):
    # To check id is exist or no , as get() return erro if not exist
    try:
        queryGust = Gust.objects.get(id=pk)
    except Gust.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == "GET":
        serializer = GustSerializer(instance=queryGust)
        return Response(serializer.data)
    # PUT
    elif request.method == "PUT":
        # instance=queryGust, data=request.data --> to edit on the object based a new data (update)
        serializer = GustSerializer(instance=queryGust, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == "DELETE":
        queryGust.delete()
        return Response(status=status.HTTP_201_CREATED)
