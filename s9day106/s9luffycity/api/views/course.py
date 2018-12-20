#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: course.py 
@time: 2018/12/10
@software: PyCharm  
"""  
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.course import CourseSerializer, CourseDetailSerializer
from api import models


# class CourseView(APIView):
#     """
#     方式一
#     对于两个url通过一个get函数的判断来区分
#     """
#     def get(self,request,*args,**kwargs):
#         ret = {"code":1000, "data":None}
#
#         try:
#             pk = kwargs.get('pk')
#             if pk:
#                 obj = models.Course.objects.filter(id=pk).first()
#                 ser = CourseSerializer(instance=obj, many=False)
#             else:
#                 queryset = models.Course.objects.all()
#                 ser = CourseSerializer(instance=queryset, many=True)
#             ret["data"] = ser.data
#         except Exception as e:
#             ret["code"] = 1001
#             ret["error"] = "获取课程失败"
#
#         return Response(ret)


from rest_framework.viewsets import ViewSetMixin
class CourseView(ViewSetMixin, APIView):
    """
    方式二
    通过list和retrieve函数分配
    """
    def list(self,request,*args,**kwargs):
        """
        获取课程列表的接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {"code":1000, "data":None}

        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)
            ret["data"] = ser.data
        except Exception as e:
            ret["code"] = 1001
            ret["error"] = "获取课程失败"

        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        获取课程详情的接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {"code":1000, "data":None}

        try:
            pk = kwargs.get('pk')

            # 从Course表中获取信息
            # obj = models.Course.objects.filter(id=pk).first()

            # 从CourseDetail表中获取信息
            obj = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializer(instance=obj, many=False)
            print('*********', ser)
            ret["data"] = ser.data
        except Exception as e:
            ret["code"] = 1001
            ret["error"] = "获取课程失败"

        return Response(ret)


from api.auth.auth import LufyyAuth
class MicroView(APIView):
    authentication_classes = [LufyyAuth]

    def get(self, request, *args, **kwargs):
        ret = {'code':1000, 'title':'微学位'}
        return Response(ret)