from tabnanny import check
from unicodedata import category
from django.db import models
from numpy import number
from django.conf import settings

# Create your models here.
class ROOM(models.Model):
    
    ROOM_CATEGORIES=(
        
        ('C','Contact'),
        ('S','Sharing'),
        ('T','Team'),
        
    
    )
    number=models.IntegerField()
    category=models.CharField(max_length=3,choices=ROOM_CATEGORIES)
    
    personcapacity=models.IntegerField()
    
    def __str__(self):
        return f'{self.number}.{self.category} {self.personcapacity}'
    
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(ROOM,on_delete=models.CASCADE) 
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return f'{self.user} {self.room} {self.start_time} {self.end_time} '   
    