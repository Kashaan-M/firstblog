from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # print(form.data, form.is_valid(),form.error_messages)
        # print('POST REQUEST')
        # if django validates the data in the form we will save the user
        # django will validate if password1 == password2 and also if user
        # already exists.
        if form.is_valid():
            # print('DJANGO VALIDATED THE FORM')
            # login() accepts a user value for session
            # form.save() automatically provides this info for login()
            login(request, form.save())
            return redirect("home")
        # if django invalidates the data the last return statement executes.
    else:
        # this handles the GET request and creates an empty form.
        form = UserCreationForm()
    # django will internally validate the data for the
    # POST method and in case data is not valid then
    # it will reload the register page, as below.
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        # print("POST for login received")
        form = AuthenticationForm(data=request.POST)
        # print("form",form.error_messages)
        if form.is_valid():
            # print("CREDENTIALS OKAY..LOGING IN")
            # LOGIN user
            login(request, form.get_user())
            return redirect("polls:polls_list")
    else:
        print("INVALID FORM")
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("homepage")
