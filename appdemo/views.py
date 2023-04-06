from .models import Hotel
from .serializer import HotelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView

class GetHotelList(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def get_queryset(self):
        return super().get_queryset()
    
class HotelCreate(CreateAPIView):
    serializer_class = HotelSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    