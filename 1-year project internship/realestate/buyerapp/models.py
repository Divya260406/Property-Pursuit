from django.db import models
from django.contrib.auth.models import User
from dealerapp.models import property

# Create your models here.
class BookingRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prop = models.ForeignKey(property, on_delete=models.CASCADE)
