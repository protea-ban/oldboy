from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def service(request):
    return HttpResponse("技师egon")
