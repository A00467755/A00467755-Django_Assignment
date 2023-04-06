from django.urls import path
from . import views

urlpatterns = [
    path('hotelist/', views.GetHotelList.as_view()),
    path('createhotel/', views.HotelCreate.as_view()),
]
