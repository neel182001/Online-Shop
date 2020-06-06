from django.shortcuts import render

# Create your views here.

def first(request):
    return render(request, 'page1.html')

def two(request):
    return render(request, 'page2.html')


                  
