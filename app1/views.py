from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 

def bhavya(request):
    return render(request, 'bhavya.html') 