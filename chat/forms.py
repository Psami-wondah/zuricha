from django import forms
from .models import Room



class NewRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']