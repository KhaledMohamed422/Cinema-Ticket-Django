from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status, filters
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets
# Create your views here.
# List == GET
# Create == POST
# pk query == GET
# Update == PUT
# Delete destroy == DELETE


# JsonResponse --> Django
# Response --> RestFreamWork
# is_valid() --> use with any form or its equivalent

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

# CBV Class based views
# 4.1 List and Create == GET and POST
class CBV_List(APIView):

    # GET
    def get(self, request):
        querysetObject = Gust.objects.all()
        serializer = GustSerializer(querysetObject, many=True)
        return Response(serializer.data)
    # POST

    def post(self, request):
        serializer = GustSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 4.2 GET PUT DELETE cloass based views -- pk
class CBV_pk(APIView):

    # To check about query
    def retriveOneObject(self, pk):
        try:
            return Gust.objects.get(id=pk)
        except:
            return Http404

    # GET
    def get(self, request, pk):
        querysetObject = self.retriveOneObject(pk=pk)
        serializer = GustSerializer(querysetObject)
        return Response(serializer.data)

    # PUT
    def put(self, request, pk):
        querysetObject = self.retriveOneObject(pk=pk)
        serializer = GustSerializer(querysetObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    def delete(self, request, pk):
        querysetObject = self.retriveOneObject(pk=pk)
        querysetObject.delete()
        return Response(status=status.HTTP_200_OK)

#5 Mixins 
#5.1 mixins list
class mixins_list(mixins.ListModelMixin , mixins.CreateModelMixin ,generics.GenericAPIView):
    # mixins.ListModelMixin --> get of all rows 
    # mixins.CreateModelMixin --> post
    # generics.GenericAPIView --> look like @api_view([""]) and APIView 
    
    # I can import 
    #   from rest_framework.mixins import ListModelMixin
    #   call as ListModelMixin
    
    # I override its
    queryset = Gust.objects.all()
    serializer_class = GustSerializer
    
    def get(self , request):
        return self.list(request)
    
    def post(self , request):
        return self.create(request)
    
#5.2 mixins get put delete 
class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    # mixins.RetrieveModelMixin --> retrieve(get) of a particular item
    # mixins.UpdateModelMixin --> put
    # mixins.DestroyModelMixin = delete
    # generics.GenericAPIView --> look like @api_view([""]) and APIView 
    
    # I override its
    queryset = Gust.objects.all()
    serializer_class = GustSerializer
    
    def get(self , request,pk):
        return self.retrieve(request,pk)
    
    def put(self , request,pk):
        return self.update(request,pk)
    
    def delete(self , request,pk):
        return self.destroy(request,pk)
    
    
        
