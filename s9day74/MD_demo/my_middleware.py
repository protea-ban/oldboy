from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MD1(MiddlewareMixin):

    def process_request(self, request):
        print("这是我的第一个中间件:MD1")
        return HttpResponse("MD1: process_request")

    def process_response(self, request, response):
        print("中间件MD1的response")
        return HttpResponse("MD1: process_response")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("中间件MD1的process_view")
        return HttpResponse("MD1:process_view")



class MD2(MiddlewareMixin):

    def process_request(self, request):
        print("这是我的第一个中间件:MD2")
        return HttpResponse("MD2: process_request")

    def process_response(self, request, response):
        print("中间件MD2的response")
        return HttpResponse("MD2: process_response")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("中间件MD2的process_view")
        return HttpResponse("MD2:process_view")

