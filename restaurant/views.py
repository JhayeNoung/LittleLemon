from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from .models import MenuItem, Booking
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
   

class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


from django.contrib.auth.models import User
from rest_framework.response import Response

@api_view()
def UserView(request):
    user = User.objects.all()
    serialized_user = UserSerializer(user, many=True)
    #return HttpResponse(user)
    return Response(serialized_user.data, 201)