from django.shortcuts import render, redirect
from django.http import request, response
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from .forms import NewUserForm

# Create your views here.
def home(request):
    return render(request, 'main.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def game(request):
    return render(request, 'game.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
            # print(request)
            # print(user)
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("home")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
            form = AuthenticationForm()
            return render(request=request, template_name="main/login.html", context={"login_form":form})
        if request.method == "GET":
            return redirect('home')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def save(request):
    pass

@login_required
def load(request):
    pass

def play(request):
    return render(request, 'uno.html')