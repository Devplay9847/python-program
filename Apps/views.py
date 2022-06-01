from django.shortcuts import render
from django.http import HttpResponse
from Apps import forms
from Apps.forms import ContactForm, LoginForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Data Successfully Inserted")
        else:
            print(forms.errors)
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'cform': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Successfully Logged In")
        else:
            print(forms.errors)
    else:
        form = LoginForm()
        return render(request, 'login.html', {'lform': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})