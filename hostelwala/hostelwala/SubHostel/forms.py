from hostel.models import booking,Payment
from django.forms import ModelForm
from django import forms
class ModelBookingForm(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'
class Paymentform(forms.ModelForm):
    class Meta:
        model=Payment
        fields='__all__'