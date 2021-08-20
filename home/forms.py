#from django import forms
from django.forms import ModelForm
from .models import Contact

# class contactForm(forms.Form):
#     name=forms.CharField(max_length=50)
#     email=forms.EmailField()
    
#     message=forms.CharField(max_length=2000,
#     widget=forms.Textarea()
#     )


class Contactform(ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']