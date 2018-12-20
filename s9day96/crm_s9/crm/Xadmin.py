#!/usr/bin/env python  
#-*- coding:utf-8 -*-  

from .models import *
from Xadmin.service.Xadmin import site
from Xadmin.service.Xadmin import ModelXadmin
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.db.models import Q
import datetime


class UserInfoConfig(ModelXadmin):
    list_display = ["name", "email", "depart"]


class ClassListConfig(ModelXadmin):

    def display_classname(self, obj=None, is_header=False):
        if is_header:
            return "班级名称"

        class_name = "%s(%s)" % (obj.course.name, str(obj.semester))
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

    def public_customer(self, request):
        # 现在的时间
        now = datetime.datetime.now()
        # 天数切片
        delta_day3 = datetime.timedelta(days=3)
        delta_day15 = datetime.timedelta(days=15)

        user_id = 5
        public_customer_list = Customer.objects.filter(Q(last_consult_date__lt=now-delta_day3)|Q(recv_date__lt=now-delta_day15), status=2).exclude(consultant=user_id)
        # print(public_customer_list)
        return render(request, "public.html", locals())

    def further(self, request, customer_id):
        user_id = 3
        # 现在的时间
        now = datetime.datetime.now()
        # 天数切片
        delta_day3 = datetime.timedelta(days=3)
        delta_day15 = datetime.timedelta(days=15)

        # 位该客户更改课程顾问，和对应时间
        ret = Customer.objects.filter(pk=customer_id).filter(Q(last_consult_date__lt=now-delta_day3)|Q(recv_date__lt=now-delta_day15),status=2).update(consultant=user_id,last_consult_date=now,recv_date=now)

        if not ret:
            return HttpResponse("已经被跟进了")

        # 创建一条新的跟进记录
        CustomerDistrbute.objects.create(customer_id=customer_id, consultant_id=user_id, date=now, status=1)

        return HttpResponse("跟进成功")

    def mycustomer(self, request):
        user_id = 3
        customer_distribute_list = CustomerDistrbute.objects.filter(consultant_id=user_id)
        return render(request, "mycustomer.html", locals())

    # 需要在原始类中添加同样的函数
    def extra_url(self):
        t_url = []
        t_url.append(url(r"cancel_course/(\d+)/(\d+)", self.cancel_course))
        t_url.append(url(r"public/", self.public_customer))
        t_url.append(url(r"further/(\d+)", self.further))
        t_url.append(url(r"mycustomer/", self.mycustomer))

        return t_url


site.register(Department)
site.register(UserInfo, UserInfoConfig)
site.register(Course)
site.register(School)
site.register(ClassList, ClassListConfig)
site.register(Customer, CustomerConfig)

class ConsultRecordConfig(ModelXadmin):
    list_display = ["customer", "consultant", "note", "date"]

site.register(ConsultRecord, ConsultRecordConfig)


class StudentConfig(ModelXadmin):

    def score_view(self, request, sid):
        if request.is_ajax():
            sid = request.GET.get("sid")
            cid = request.GET.get("cid")
            student_record_list = StudyRecord.objects.filter(student=sid, course_record__class_obj=cid)
            # print(student_record_list)

            data_list = []
            for student_record in student_record_list:
                day_num = student_record.course_record.day_num
                data_list.append(["day%s" % day_num, student_record.score])
            print(data_list)
            return JsonResponse(data_list, safe=False)
        else:
            student_obj = Student.objects.filter(pk=sid).first()
            class_list = student_obj.class_list.all()

        return render(request, "score_view.html", locals())

    def extra_url(self):
        list_url = []
        list_url.append(url(r"score_view/(\d+)", self.score_view))

        return list_url


    def score_show(self, obj=None, is_header=False):
        if is_header:
            return "查看成绩"

        return mark_safe("<a href='/Xadmin/crm/student/score_view/%s'>查看成绩</a>" % obj.pk)

    list_display = ["customer", "class_list", score_show]
    list_display_links = ["customer"]

site.register(Student, StudentConfig)


class CourseRecordConfig(ModelXadmin):

    def score(self, request, course_record_id):
        if request.method == "POST":
            # 先看看传回来的数据长什么样
            print(request.POST)
            # 构建我们想要的数据结构
            dic_data = {}
            for key, value in request.POST.items():
                if key == "csrfmiddlewaretoken":continue

                # 将传来的key值分开
                field, pk = key.rsplit("_", 1)

                # 分两种情况存入dic_data中，已有字段和无字段
                if pk in dic_data:# 有字段
                    dic_data[pk][field] = value
                else:# 无字段
                    dic_data[pk] = {field: value}

            # 更新数据库
            for pk, update_data in dic_data.items():
                StudyRecord.objects.filter(pk=pk).update(**update_data)

            # 返回当前页面
            return redirect(request.path)
        else:

            study_record_list = StudyRecord.objects.filter(course_record=course_record_id)
            score_choices = StudyRecord.score_choices
            return render(request, "score.html", locals())


    def extra_url(self):
        list_url = []
        list_url.append(url(r"record_score/(\d+)", self.score))

        return list_url


    def record(self, obj=None, is_header=False):
        """
        记录考勤的自定义字段
        :param obj:
        :param is_header:
        :return:
        """
        if is_header:
            return "考勤"

        return mark_safe("<a href='/Xadmin/crm/studyrecord/?course_record={}'>记录</a>".format(obj.pk))

    def record_score(self, obj=None, is_header=False):
        if is_header:
            return "录入成绩"
        return mark_safe("<a href='record_score/{}'>录入成绩</a>".format(obj.pk))

    list_display = ["class_obj", "day_num", "teacher", record, record_score]

    def patch_studyrecord(self, request, queryset):
        # print(queryset)
        list_studyrecord = []
        for course_record in queryset:
            # 取到与course_record相关的全部学生
            student_list = Student.objects.filter(class_list__id=course_record.class_obj.pk)
            # print(student_list)
            # 对每个学生创建学习记录对象
            for student in student_list:
                obj_studyrecord = StudyRecord(student=student, course_record=course_record)
                list_studyrecord.append(obj_studyrecord)
        # print(list_studyrecord)

        # 批量添加学习记录
        StudyRecord.objects.bulk_create(list_studyrecord)

    patch_studyrecord.short_description = "批量生成学习记录"
    actions = [patch_studyrecord, ]



site.register(CourseRecord, CourseRecordConfig)


class StudyRecordConfig(ModelXadmin):
    list_display = ["course_record", "student", "record", "score", "homework_note"]

    def patch_late(self, request, queryset):
        queryset.update(record="late")

    patch_late.short_description = "迟到"
    actions = [patch_late, ]


site.register(StudyRecord, StudyRecordConfig)
site.register(CustomerDistrbute)