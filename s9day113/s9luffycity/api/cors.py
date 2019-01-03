#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: cors.py 
@time: 2018/12/10
@software: PyCharm  
"""  
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CORSMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # 添加响应头

        # 允许别的域名来获取数据，允许所有用*代替
        response['Access-Control-Allow-Origin'] = '*'

        # 允许你携带Content-Type请求头
        # response['Access-Control-Allow-Headers'] = "Content-Type"

        # 允许你发送DELETE,PUT
        # response['Access-Control-Allow-Methods'] = "DELETE,PUT"

        if request.method == "OPTIONS":
            # 允许你携带Content-Type请求头
            response['Access-Control-Allow-Headers'] = "Content-Type"

            # 允许你发送DELETE,PUT
            response['Access-Control-Allow-Methods'] = "DELETE,PUT"

        return response
