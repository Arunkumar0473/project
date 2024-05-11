# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerSupport,booking,sharing_type,Payment
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = UserCreationForm
        fields = ('username', 'email', 'password1', 'password2')

class BookinModelForm(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'
        def __init__(self, *args, **kwargs):
              super(BookinModelForm, self).__init__(*args, **kwargs)
              self.fields['sharing_type'].queryset = sharing_type.objects.all()

