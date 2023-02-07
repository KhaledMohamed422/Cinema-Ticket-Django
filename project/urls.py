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
    path('django/JsonNoModelNorest', no_rest_no_model),#1 To send as json without model and rest
    path('django/JsonModelNorest', model_no_rest), #2 To send as json model and without rest
    path('djangoRestfreamwork/Get_Post', Get_List_Post_Data), #2 request post and get with restfreamwork
    
]
