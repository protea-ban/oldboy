from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
# Create your views here.
from .models import *
import datetime


def index(request):
    date = datetime.datetime.now().date()
    time_choices = Book.time_choices
    room_list = Room.objects.all()
    book_list = Book.objects.all()

    htmls = ""
    # 遍历会议室列表，构建预定表格
    for room in room_list:
        htmls += "<tr><td>{}({})</td>".format(room.caption, room.num)

        for time_choice in time_choices:
            booked = False
            for book in book_list:
                # 这个单元格已经被预定
                if book.room_id == room.pk and book.time_id == time_choice[0]:
                    booked = True
                    break

            if booked:
                if request.user.pk == book.user.pk:
                    htmls += "<td class='active item' room_id={} time_id={}>{}</td>".format(room.pk, time_choice[0], book.user.username)
                else:
                    htmls += "<td class='another_active item' room_id={} time_id={}>{}</td>".format(room.pk, time_choice[0], book.user.username)
            else:
                htmls += "<td class='item' room_id={} time_id={}></td>".format(room.pk, time_choice[0])

        # 遍历完之后算是完整一行，再加上</tr>标签
        htmls += "</tr>"

    return render(request, "index.html", locals())


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = auth.authenticate(username=user,password=pwd)
        if user:
            auth.login(request, user)
            return redirect('/index/')

    return render(request, "login.html")


import json
def book(request):

    # print(request.POST)
    post_data = json.loads(request.POST.get("post_data"))
    choose_date = request.POST.get("choose_date")

    res = {"state": True, "msg": None}

    try:
        # 添加预订
        book_list = []
        for room_id, time_id_list in post_data["ADD"].items():

            for time_id in time_id_list:
                book_obj = Book(user=request.user, room_id=room_id, time_id=time_id, date=choose_date)
                book_list.append(book_obj)

        # 一次性创建并保存到数据库中多条数据
        Book.objects.bulk_create(book_list)

        # 批量删除预订
        from django.db.models import Q

        remove_book = Q()
        for room_id,time_id_list in post_data["DEL"].items():
            temp = Q()
            for time_id in time_id_list:
                temp.children.append(("room_id", room_id))
                temp.children.append(("time_id", time_id))
                temp.children.append(("user_id", request.user.pk))
                temp.children.append(("date", choose_date))
                remove_book.add(temp, "OR")

        if remove_book:
            Book.objects.filter(remove_book).delete()


    except Exception as e:
        res["state"] = False
        res["msg"] = str(e)


    return HttpResponse(json.dumps(res))
