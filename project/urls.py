"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tickets.views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/JsonNoModelNorest', fbv_no_rest_no_model),#1 To send as json without model and rest
    path('django/JsonModelNorest', fbv_model_no_rest), #2 To send as json model and without rest
    
    # #3.1 GET POST from rest framework function based view @api_view
    path('djangoRestfreamwork/Get_Post', fbv_get_list_post_data), 
    
    #3.2 GET PUT DELETE from rest framework function based view @api_view
    path('djangoRestfreamwork/Put_Get_Delete/<int:pk>', fbv_get_list_put_data_delete_data), 

    #4.1 GET POST from rest framework class based view APIView
    path('djangoRestfreamwork/CBV/', CBV_List.as_view()),
    
    #4.2 GET PUT DELETE from rest framework class based view APIView
    path('djangoRestfreamwork/CBV/<int:pk>', CBV_pk.as_view()),
 
    #5.1 GET POST from rest framework class based view mixins
    path('djangoRestfreamwork/mixins/', mixins_list.as_view()),

    #5.2 GET PUT DELETE from rest framework class based view mixins
    path('djangoRestfreamwork/mixins/<int:pk>', mixins_pk.as_view()),

    #6.1 GET POST from rest framework class based view generics
    path('djangoRestfreamwork/generics/', generics_list.as_view()),

    #6.2 GET PUT DELETE from rest framework class based view generics
    path('djangoRestfreamwork/generics/<int:pk>', generics_pk.as_view()),
]
