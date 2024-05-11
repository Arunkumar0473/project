from django.shortcuts import render
from django.http import HttpResponse
from .forms import ModelBookingForm

# Create your views here.
def SubBookingFunction(request):
    empty=ModelBookingForm()
    if request.method=='POST':
        data=ModelBookingForm(request.POST)
        if data.is_valid()==True:
            data.save()
            return render(request,'subhostel/subBooking.html',{'form':empty,'data':'booking is successfully'})
        else:
            return render(request,'subhostel/subBooking.html',{'form':data,'data':'booking is filed'})

    return render(request,'subhostel/subBooking.html',{'form':empty})