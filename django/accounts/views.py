from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def profile(request):
    return HttpResponse("profile page.")
