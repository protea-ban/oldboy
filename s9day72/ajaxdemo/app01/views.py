from django.shortcuts import render, HttpResponse
from app01 import models

# Create your views here.


def index(request):
    return render(request, "index.html")


def ajax_add(request):
    print(request.GET)
    i1 = request.GET.get("i1")
    i2 = request.GET.get("i2")
    ret = int(i1) + int(i2)
    print(ret)

    return HttpResponse(ret)


def test(request):
    url = ""
    return HttpResponse(url)


def ajax_post_add(request):
    i1 = request.POST.get("i1")
    i2 = request.POST.get("i2")
    ret = int(i1) + int(i2)

    return HttpResponse(ret)


def persons(request):
    all_persons = models.Person.objects.all()
    return render(request, "persons.html", {"persons": all_persons})


def delete(request):
    import time
    time.sleep(4)
    delId = request.POST.get("id")
    models.Person.objects.filter(id=delId).delete()

    return HttpResponse("删除成功了！")


