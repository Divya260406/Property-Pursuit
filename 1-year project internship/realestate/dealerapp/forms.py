from django.forms import ModelForm
from . import models
from django import forms
class detailsform(ModelForm):
    class Meta:
        model = models.property
        fields = "__all__"
        exclude=('user',)
        widget = {
            'p_direction': forms.RadioSelect()
        }

class Imageform(forms.ModelForm):
    class Meta:
        model=models.Image
        fields = "__all__"

        
class updateform(ModelForm):
    class Meta:
        model = models.property
        fields = "__all__"
        exclude = ('user',)

