from django.shortcuts import render


def greet(request):
    return render(request, 'post/welcome.html')
# Create your views here.
