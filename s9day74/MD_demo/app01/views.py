from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    print("来自index视图函数")
    return HttpResponse("O98k")

