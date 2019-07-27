from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def login_view(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = "Noooooooooo"

    Context = {
        "error" : error
    }
    return render(request, 'auth/login.html', Context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')