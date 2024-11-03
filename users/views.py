from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Hardcoded credentials
        hardcoded_username = 'admin'
        hardcoded_password = 'password123'

        if username == hardcoded_username and password == hardcoded_password:
            return redirect('success')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'users/login.html')

def success_view(request):
    return render(request, 'users/success.html')
