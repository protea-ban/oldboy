#!/usr/bin/env python  
#-*- coding:utf-8 -*-  

from .models import *
from Xadmin.service.Xadmin import site
from Xadmin.service.Xadmin import ModelXadmin
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import render,redirect

class UserInfoConfig(ModelXadmin):
    list_display = ["name", "email", "depart"]

class ClassListConfig(ModelXadmin):

    def display_classname(self, obj=None, is_header=False):
        if is_header:
            return "班级名称"

        class_name = "%s(%s)"%(obj.course.name, str(obj.semester))
        return class_name

    list_display = [display_classname, "school", "tutor", "teachers"]


class CustomerConfig(ModelXadmin):
    def display_gender(self, obj=None, is_header=False):
        if is_header:
            return "性别"
        return obj.get_gender_display()

    def display_course(self, obj=None, is_header=False):
        if is_header:
            return "咨询课程"
        t_course = []
        for course in obj.course.all():
            s = "<a href='/Xadmin/crm/customer/cancel_course/{}/{}' style='border:1px solid #369;padding:3px 6px'><span>{}</span></a>&nbsp;".format(obj.pk, course.pk, course.name)
            t_course.append(s)
        return mark_safe("".join(t_course))

    list_display = ["name", display_gender, display_course, "consultant"]

    # 在某个特定表中用到的视图函数即url可以在该表的配置类中定义
    def cancel_course(self, request, customer_id, course_id):
        cancel_obj = Customer.objects.filter(pk=customer_id).first()
        cancel_obj.course.remove(course_id)
        return redirect(self.get_list_url())

    # 需要在原始类中添加同样的函数
    def extra_url(self):
        t_url = []
        t_url.append(url(r"cancel_course/(\d+)/(\d+)", self.cancel_course))

        return t_url

site.register(Department)
site.register(UserInfo, UserInfoConfig)
site.register(Course)
site.register(School)
site.register(ClassList, ClassListConfig)
site.register(Customer, CustomerConfig)
site.register(ConsultRecord)
site.register(Student)
site.register(CourseRecord)
site.register(StudyRecord)
