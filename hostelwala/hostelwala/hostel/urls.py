# hostel/urls.py
# urls.py
from django.urls import path
from . import views  # Import views module
from django.contrib.auth.views import LoginView
from .views import verify_otp


urlpatterns = [
    # Define URL patterns and map them to corresponding views
    path('hostel/', views.login_view, name='loginurl'),  # Assuming login_view is the view function for the login page
    path('logout/',views.LogoutPage,name='logouturl'),
    path('Home/',views.HomePage,name='homeurls'),
    path('dash/', views.Dashbord, name='dashboard'),  # Assuming dashboard is the view function for the dashboard
    path('member-details/', views.member_details, name='member_details'),  # Assuming member_details is the view function for member details
    path('login/', LoginView.as_view(), name='login'),
    path('sign/', views.signup, name='signupurl'),    #sing
    # path('password_reset/', views.password_reset_with_otp, name='password_reset'),
    path('verify_otp/',views.verify_otp, name='verify_otp'),
    path('booking/', views.booking, name='bookingurl'),  #1
    path('support/', views.support, name='supportsurl'),
    path('payment/',views.PaymentFun,name='paymenturl'),
    path('card/',views.CardFun,name='cardurl'),
    path('book/',views.bookings,name='bookurl'),
    path('bookgirl/',views.bookinggirl,name='bookgirls'),
    path('bookco/',views.bookingco,name='bookcourl'),
    path('check/',views.checklist,name='checks'),
    path('checkgirl/',views.checkgirl,name='checkgirl'),
    path('checkco/',views.checkco,name='checkco'),
    path('about/',views.aboutus,name='abouturl'),
    path('forgot/',views.forgot,name='forgoturl'),
    path('otp/',views.otp,name='otpurl'),
    path('forgotpwd/',views.ForgotFun,name='PwdForgoturl'),
    

    


    
]

