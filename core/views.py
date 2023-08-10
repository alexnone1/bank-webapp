from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import AccountUsers


def register_view(request):
    if request.method == "POST":
        form = AccountUsers(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("home_view")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = AccountUsers()
    return render(request=request, template_name="signup.html", context={"form": form})


def home_view(request):

    return render(request, "dashboard/home.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_view')
        else:
            messages.success(
                request, ("Your password is incorrect, Kindly check the password and try again!"))
            return redirect('login_view')
    else:
        return render(request, "dashboard/login.html")


def logout_view(request):
    logout(request)
    return redirect('home_view')


def dashboard_view(request):
    username = "James Smith"
    account_balance = "$69,254,300.43"

    context = {
        "username": username,
        "account_balance": account_balance
    }
    return render(request, "dashboard/dashboard.html", context)
