from django.shortcuts import render

from django.http.response import HttpResponse

# Create your views here.

def index_view(request):
	return HttpResponse("<h1>USOS MOBILE</h1><br>best project evar<br><br><img src=http://i497.photobucket.com/albums/rr340/RUNDUMMINEM/COMMENTS/sup.jpg>")
