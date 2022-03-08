from pyexpat import model
from tempfile import template
from unicodedata import category
from urllib import request
from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,FormView
from .models import ROOM,Booking
from .forms import AvailabilityForm
from booking.booking_function.availability import check_availability
# Create your views here.



class RoomList(ListView):
    model = ROOM
    
class BookingList(ListView):
    model = Booking    
class BookingView(FormView):
    form_class = AvailabilityForm

        
            
        
    template_name = 'availability_form.html'
    
    def form_valid(self,form):
        data = form.cleaned_data
        room_list = ROOM.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['start_time'], data['end_time']):
                available_rooms.append(room)
        if len(available_rooms)>0:
                    
            room = available_rooms[0]
            booking = Booking.objects.create(
               user = self.request.user,
               room = room,
               start_time = data['start_time'],
               end_time = data['end_time'],
            
            )   
            booking.save()   
            return HttpResponse(booking)  
        else:
            return HttpResponse('all of these category of rooms are booked! Try another one')
            
    