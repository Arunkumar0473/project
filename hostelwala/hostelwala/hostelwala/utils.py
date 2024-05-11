from django_otp.oath import TOTP
import base64
import os

def generate_otp():
    # Generate a random secret key (base32 encoded)
    secret_key = base64.b32encode(os.urandom(10)).decode('utf-8')
    
    # Create a TOTP object with the generated secret key
    totp = TOTP(secret_key)
    
    # Generate the OTP
    otp = totp.token()
    
    return otp, secret_key