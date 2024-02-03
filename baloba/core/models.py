from django.db import models
from baloba.utils.base import BaseModel

# Create your models here.

class ContactUsModel(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Name of message sender')
    email = models.EmailField(verbose_name='E-mail of message sender')
    message = models.TextField(verbose_name='Message')
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'All Messages'
    
    def __str__(self):
        return self.name
    
class Subscriber(BaseModel):
    email = models.EmailField(verbose_name='Email address')
    
    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers' 
        
    def __str__(self):
        return self.email       