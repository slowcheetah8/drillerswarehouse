from django.shortcuts import render

def index(request):
	return render(request, 'webfront/home.html')
	

