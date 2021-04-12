from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
import json
from django.core.serializers.json import DjangoJSONEncoder
from PIL import Image


# Create your views here.
"""
# Create login function
def login(request):
    # email = "wrong email or password"
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
                request.session.set_expiry(5)
            # else:
            # raise RuntimeError("wrong email or password")
    else:
        mylogin = LoginForm()

    return render(request, 'pages/Home.html', {'form': mylogin})
"""
"""
def formview(request):
    if 'email' in request.session:
        # email = request.session['email']
        return render(request, 'pages/Home.html', {})
    else:
        mylogin = LoginForm()
        return render(request, 'pages/Signin.html', {'form': mylogin})
"""
"""
def logout(request):
    try:
        del request.session['email']
    except:
        pass
    mylogin = LoginForm()
    return render(request, 'pages/Signin.html', {'form': mylogin})
"""

# Handle login
def login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            if email == 'test@gmail.com' and password == '123':
                return HttpResponseRedirect('/home')
    else:
        loginform = LoginForm()
    return render(request, 'registration/Signin.html', {'form': loginform})
# Handle sign up
data = {} # Declare global argument
def signup1(request):
    global data
    # Get request from client
    if request.method == 'POST':
        signupform1 = SignUpForm1(request.POST)
        # Get data from client
        if signupform1.is_valid():
            cmndid = signupform1.cleaned_data['cmnd']
            id = cmndid.rjust(12, "0")
            data = {
                    "_id":id,
                    "REFERRAL CODE":signupform1.cleaned_data['referralcode'],
                    "EMAIL":signupform1.cleaned_data['emailsignup'],
                    "PASSWORD":signupform1.cleaned_data['passwordsignup'],
                    "NAME":signupform1.cleaned_data['name'],
                    "CMND":signupform1.cleaned_data['cmnd'],
                    "BIRTHDAY":signupform1.cleaned_data['birthday'],
                    "PHONE":signupform1.cleaned_data['phone'],
                    "ADDRESS":signupform1.cleaned_data['address'],
            }
            """
            with open("data.json", "w") as f:
                json.dump(data1, f, sort_keys=True, cls=DjangoJSONEncoder)
                f.close()
            """
            return HttpResponseRedirect('/signup2')
    else:
        signupform1 = SignUpForm1()
    return render(request, 'registration/Signup1.html', {'form': signupform1})

"""
def signup2(request):
    global data2
    # Get request from client
    if request.method == 'POST':
        signupform2 = SignUpForm2(request.POST)
        # Get data from client
        if signupform2.is_valid():
            data2 = {
                    "BIRTHDAY":signupform2.cleaned_data['birthday'],
                    "PHONE":signupform2.cleaned_data['phone'],
                    "ADDRESS":signupform2.cleaned_data['address']}

            with open("data.json", "a") as f:
                json.dump(data2, f, sort_keys=True)
                f.close()

            return HttpResponseRedirect('/signup3')
    else:
        signupform2 = SignUpForm2()
    return render(request, 'registration/Signup2.html', {'form': signupform2})
"""

def signup2(request):
    global data
    # data = {**data1, **data2} # Merge data1 and data2
    # Get request from client
    if request.method == 'POST':
        signupform2 = SignUpForm2(request.POST, request.FILES) # Get file from client
        if signupform2.is_valid():
            # Save image in project's root
            img1 = signupform2.cleaned_data['cmndimg1']
            img2 = signupform2.cleaned_data['cmndimg2']
            with Image.open(img1) as im1:
                im1.save(str(data.get('NAME'))+" 1", "png")
            with Image.open(img2) as im2:
                im2.save(str(data.get('NAME'))+" 2", "png")
            # Save data in project's root
            with open(str(data.get('NAME'))+".json", "w") as f:
                json.dump(data, f, cls=DjangoJSONEncoder)
                f.close()
            return HttpResponseRedirect('/')
    else:
        signupform2 = SignUpForm2()
    return render(request, 'registration/Signup2.html', {'form': signupform2})


"""
def signup1(request):
    if request.method == 'POST':
        signupform1 = SignUpForm(request.POST)
        if signupform1.is_valid():
            return HttpResponseRedirect('/signup2')
    else:
        signupform1 = SignUpForm()
    return render(request, 'registration/Signup1.html', {'form': SignUpForm})


def signup2(request):
    if request.method == 'POST':
        signupform2 = SignUpForm(request.POST)
        if signupform2.is_valid():
            return HttpResponseRedirect('/signup3')
    else:
        signupform2 = SignUpForm()
    return render(request, 'registration/Signup2.html', {'form': SignUpForm})


def signup3(request):
    if request.method == 'POST':
        signupform3 = SignUpForm(request.POST, request.FILES)
        if signupform3.is_valid():
            return HttpResponseRedirect('/')
    else:
        signupform3 = SignUpForm()
    return render(request, 'registration/Signup3.html', {'form': SignUpForm})
"""
