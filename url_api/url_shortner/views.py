from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .serializers import *
from .models import *

class index(APIView):
    def post(self,request,format=None):
            print(request.data)
            serializer=url_dataSerializer(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                return Response({'id': obj.id})
            return Response(status.HTTP_400_BAD_REQUEST)

class url_datatDetail(APIView):
    def get(self, request, pk,format=None):
        data = url_data.objects.values().get(id=pk)
        title = data["title"]
        description = data["description"]
        image = data["img"]
        link = data["link"]

        # updating the counter 
        data = url_data.objects.get(id=pk)
        data.link_counter = data.link_counter + 1
        data.save()
        
        return render(request, 'link_preview.html', {
            'url': link,
            'title': title,
            'description': description,
            'image_url': image,
        })

class urlDetail(APIView):
    def get(self, request, pk,format=None):
        data = url_data.objects.values().get(id=pk)
        return Response(data)