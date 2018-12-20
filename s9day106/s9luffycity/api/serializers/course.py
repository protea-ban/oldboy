#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: course.py 
@time: 2018/12/14
@software: PyCharm  
"""  
from api import models
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    """
    课程序列化
    """

    level = serializers.CharField(source='get_level_display')

    class Meta:
        model = models.Course
        # fields = "__all__"
        fields = ['id', 'title', 'course_img', 'level']

class CourseDetailSerializer(serializers.ModelSerializer):
    """
    课程详细序列化
    """

    # o2o/fk/choice字段的获取
    title = serializers.CharField(source='course.title')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')

    # m2m字段的获取
    recommends = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        # fields = "__all__"
        fields = ['course', 'title', 'img', 'level', 'slogon', 'why', 'recommends', 'chapter']

    def get_recommends(self, obj):
        """
        获取所有的推荐课程
        :param obj:
        :return:
        """
        queryset = obj.recommend_course.all()

        return [{'id': item.id, 'title': item.title} for item in queryset]

    def get_chapter(self, obj):
        """
        获取该课程的章节信息
        :param obj:
        :return:
        """
        queryset = obj.course.chapter_set.all()
        print('####', queryset)
        return [{'num': item.num, 'name': item.name} for item in queryset]
