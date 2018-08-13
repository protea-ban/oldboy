from django.shortcuts import render

# Create your views here.


def transfer(request):
    return render(request, "transfer.html")