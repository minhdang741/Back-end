from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .connect import Connect
import json
from .models import LoginForm
import cgi


# Create your views here.

"""
class LoginViewSite(LoginView):
    template_name = 'pages/Signin.html'


class HomeViewSite(LoginRequiredMixin, TemplateView):
    template_name = 'pages/Home.html'
"""

"""
# Create login function
def login(request):
    # email = "wrong email or password"
    mylogin = LoginForm()
    if request.method == 'POST':
        mylogin = LoginForm(request.POST)
        # email = mylogin.cleaned_data['email']
        # password = mylogin.cleaned_data['password']
        if mylogin.is_valid():
            email = mylogin.cleaned_data['email']
            password = mylogin.cleaned_data['password']
            # if mylogin.cleaned_data['email'] == 'test@gmail.com' and mylogin.cleaned_data['password'] == '123':
            if email == 'test@gmail.com' and password == '123':
                email = mylogin.cleaned_data['email']
                request.session['email'] = email
                request.session.set_expiry(0)
            # else:
            # raise RuntimeError("wrong email or password")
    # else:
        # mylogin = LoginForm()

    return render(request, 'pages/Home.html', {})


def formview(request):
    if 'email' in request.session:
        # email = request.session['email']
        return render(request, 'pages/Home.html', {})
    else:
        return render(request, 'pages/Signin.html')


def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'pages/Signin.html')
"""

"""
def index(request):
    customer = Connect.connection()
    file = open('/home/dang/Documents/customer/customer (another copy).json', 'r')
    
     with open('/home/dang/Documents/customer/customer (copy).json') as f:
        data = json.loads(f)
    
    data = json.load(file)
    # print(data)
    customer.insert_many(data)
    file.close()
    return HttpResponse("Done")
"""
"""
def login(request):
    return render(request, 'pages/Home.html')

def logout(request):
    return render(request, 'pages/login.html')
"""
