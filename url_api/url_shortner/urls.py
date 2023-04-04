from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view() , name='index'),
    path('url_data/<int:pk>/', url_datatDetail.as_view()),
    path('urlDetail/<int:pk>/', urlDetail.as_view()),   
]