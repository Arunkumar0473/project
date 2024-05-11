
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member,booking
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings
from django_otp import devices_for_user
from django_otp.plugins.otp_email.models import EmailDevice
from .models import CustomerSupport
from django.views.decorators.csrf import ensure_csrf_cookie
from .utils import generate_otp
from .import views



def login_view(request):
    if request.method=='POST':
        user=request.POST['user']
        pwd=request.POST['pwd']
        validuser=authenticate(request,username=user,password=pwd)
        if validuser!=None:
            login(request,validuser)
            return redirect('homeurls')
        else:
            return redirect('loginurl')
    return render(request, 'registration/signup1.html')
def LogoutPage(request):
    logout(request)
    return redirect('loginurl')

def signup(request):           #sin
    if request.method == 'POST':
        # Get form data
        username = request.POST('user')
        email = request.POST('email')
        password = request.POST('pwd')
        confirm_password = request.POST('confirm_pwd')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'registration/signup1.html', {'error': 'Passwords do not match'})

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/signup1.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'registration/signup1.html', {'error': 'Email already exists'})

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

                 # Log in the user after registration
        user = authenticate(request, username=username, password=password)
        login(request, user)

               # Redirect to dashboard or any other page
        return redirect('loginurl')  # Replace 'dashboard' with the name of your dashboard URL pattern

    return render(request, 'registration/signup1.html')


def verify_otp(request):
    if request.method == "POST":
        otp_entered = request.POST.get('otp')
        otp_stored = request.session.get('otp_token')
        email = request.session.get('email')
        
        if otp_entered == otp_stored:
            # OTP verification successful
            # Clear session data
            del request.session['otp_token']
            del request.session['email']
            
            # Redirect to password reset form
            return redirect('password_reset_done')
        else:
            # OTP verification failed
            return render(request, 'registration/otp_verification.html', {'error': 'Invalid OTP'})
    return render(request, 'registration/otp_verification.html')
# views.py
def HomePage(request):
    return render(request,'registration/homepage.html')

# def facilities(request):
#     return render(request, 'registration/facilities.html')
# def rooms(request):
#     return render(request, 'registration/rooms.html')

def booking(request):
    
    return render(request, 'registration/booking.html')     #
def support(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('number')
        message = request.POST.get('message')
        CustomerSupport.objects.create(name=name, email=email, phonenumber=phono, message=message)
        return render(request, 'registration/support.html')  # You might want to redirect or render a different template after successful submission
    return render(request, 'registration/support.html')
def checklist(request):
    return render(request, 'registration/listof.html')
def checkgirl(request):
    return render(request, 'registration/listgirl.html')
def checkco(request):
    return render(request, 'registration/listco.html')
def aboutus(request):
    return render(request, 'registration/about.html')
def PaymentFun(request):
    return render(request,'registration/payment.html')
def bookings(request):
    return render(request,'registration/checklist.html')
def bookinggirl(request):
    return render(request,'registration/checkgirl.html')
def bookingco(request):
    return render(request,'registration/checkco.html')

def CardFun(request):
    return render(request,'registration/card.html')
def forgot(request):
    # return HttpResponse('su')
    return render(request,'registration/password_reset_form.html')

def ForgotFun(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Generate OTP (You can use any OTP generation mechanism here)
        otp, secret_key = generate_otp()  # Implement your OTP generation logic

        # Send OTP to the provided email
        subject = 'Your OTP for password reset'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER  # Use your email configured in settings
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            # For demonstration purposes, let's print the OTP in the console
            print("OTP sent:", otp)
            # You can also redirect the user to another page for OTP verification
            return HttpResponse("OTP sent successfully!")  # Replace this with a redirect if needed
        except Exception as e:
            # Handle error if sending email fails
            print("Error sending OTP:", str(e))
            return HttpResponse("Error sending OTP. Please try again later.")
    return render(request, 'registration/HostelForgot.html')

def otp(request):
    return render(request, 'registration/otp_verification.html')

@login_required
def Dashbord(request):
    return render(request, 'registration/dashboard.html')
# views.py
@login_required

def member_details(request):
    owner = request.user
    members = Member.objects.filter(owner=owner)
    return render(request, 'registration/member_details.html', {'members': members})






