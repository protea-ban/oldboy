from django.shortcuts import render, HttpResponse
import json
# Create your views here.


# def service(request):
#     info = {"name": "egon", "age": 34, "price": 200}
#     func = request.GET.get("callbacks")
#     return HttpResponse("%s('%s')" % (func, json.dumps(info)))


def service(request):
    info = {"name": "egon", "age": 34, "price": 200}
    response = HttpResponse(json.dumps(info))
    response["Access-Control-Allow-Origin"] = "*"
    return response
