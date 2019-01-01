#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: shoppingcar.py 
@time: 2018/12/31
@software: PyCharm  
"""  
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.response import BaseResponse
from api.auth.auth import LufyyAuth
from api import models
from utils.exception import PricePolicyInvalid
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import json
from django_redis import get_redis_connection

class ShoppingCarViewSet(APIView):
    authentication_classes = [LufyyAuth, ]
    conn = get_redis_connection("default")

    def post(self, request, *args, **kwargs):
        """
        将课程添加到购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()

        try:
            # 1. 获取用户提交的课程ID和价格策略
            course_id = int(request.data.get('courseid'))
            policy_id = int(request.data.get('policyid'))

            # 2. 获取专题课信息
            course = models.Course.objects.get(id=course_id)

            # 3. 获得该课程相关的所有价格策略
            price_policy_list = course.price_policy.all()
            price_policy_dict = {}

            for price_policy_item in price_policy_list:
                price_policy_dict[price_policy_item.id] = {
                    "period": price_policy_item.valid_period,
                    "period_display": price_policy_item.get_valid_period_display(),
                    "price": price_policy_item.price
                }

            # 4. 判断用户提交的价格策略是否合法
            if policy_id not in price_policy_dict:
                # 价格策略不合法
                raise PricePolicyInvalid("价格策略不合法")

            # 5. 将购物信息添加到redis中
            car_key = settings.SHOPPING_CAR_KEY % (request.auth.user_id, course_id, )
            car_dict = {
                "title": course.title,
                "img": course.course_img,
                "default_policy": policy_id,
                "policy": json.dumps(price_policy_dict)
            }
            self.conn.hmset(car_key, car_dict)
            ret.data = "添加成功"

        except PricePolicyInvalid as e:
            ret.code = 2001
            ret.error = e.msg
        except ObjectDoesNotExist as e:
            ret.code = 2001
            ret.error = "课程不存在"
        except Exception as e:
            ret.code = 1001
            ret.error = "获取购物车失败"

        return Response(ret.dict)

    def delete(self, request, *args, **kwargs):
        """
        删除购物车中的课程
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()

        try:
            course_id_list = request.data.get('courseids')
            key_list = [settings.SHOPPING_CAR_KEY%(request.auth.user_id, course_id, ) for course_id in course_id_list]
            self.conn.delete(*key_list)
        except Exception as e:
            ret.code = 1002
            ret.error = "删除失败"

        return Response(ret.dict)

    def patch(self,  request, *args, **kwargs):
        """
        修改购物车的课程
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()

        try:
            # 1. 获取价格策略ID和课程ID
            course_id = int(request.data.get('courseid'))
            policy_id = str(request.data.get('policyid'))

            # 2. 拼接课程的key
            key = settings.SHOPPING_CAR_KEY%(request.auth.user_id, course_id)

            if not self.conn.exists(key):
                ret.code = 1002
                ret.error = "购物车中不存在此课程"
                return Response(ret.dict)

            # 3. redis中获取所有的价格策略
            policy_dict = json.loads(self.conn.hget(key, 'policy').decode('utf-8'))

            if policy_id not in policy_dict:
                ret.code = 1003
                ret.error = "价格策略不合法"
                return Response(ret.dict)

            # 4. 在购物车中修改该课程的默认价格策略
            self.conn.hset(key, 'default_policy', policy_id)

            ret.data = "修改成功"

        except Exception as e:
            ret = 1004
            ret.error = "修改失败"

        return Response(ret.dict)

    def get(self, request, *args, **kwargs):
        """
        查看购物车中的所有商品
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()

        try:
            key_match = settings.SHOPPING_CAR_KEY%(request.auth.user_id, "*")

            course_list = []

            for key in self.conn.scan_iter(key_match, count=10):
                info = {
                    "title": self.conn.hget(key, "title").decode('utf-8'),
                    "img": self.conn.hget(key, "img").decode('utf-8'),
                    "policy": json.loads(self.conn.hget(key, "policy").decode('utf-8')),
                    "default_policy": self.conn.hget(key, "default_policy").decode('utf-8'),
                }
                course_list.append(info)

            ret.data = course_list

        except Exception as e:
            ret.code = 1002
            ret.error = "获取失败"

        return Response(ret.dict)
