from django.shortcuts import render
from django.http import HttpResponse
from .connect import Connect
import json


# Create your views here.


def index(request):
    return render(request, 'pages/Signin.html')


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
