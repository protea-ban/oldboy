from django.shortcuts import render, HttpResponse
from app01 import models

# Create your views here.

def home(request):

    return HttpResponse("没错，我就是首页！")


def delete(request, title, id):
    # 删除语句
    # models.Book.objects.get(id=id).delete()

    # 数据库中保存的类名都是首字母大写的
    title = title.capitalize()

    # 从另一个文件根据字符串反射到具体的变量
    if hasattr(models, title):
        title_class = getattr(models, title)
        try:
            title_class.objects.get(id=id).delete()
        except Exception as e:
            print(str(e))
            print("id值不存在")
            return HttpResponse("名称：{} id:{}".format(title, id))
    else:
        return HttpResponse("表{}不存在".format(title))
