from django.forms import ModelForm
from . import models
from django import forms

class bookingform(ModelForm):
    class Meta:
        model = models.property
        fields = "__all__"
        exclude = ('user','prop',)