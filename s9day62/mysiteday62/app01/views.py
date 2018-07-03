from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.

def publisher_list(request):
    ret = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list':ret})

def add_publisher(request):
    err_msg = ""
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name')
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        else:
            err_msg = "出版社名称不能为空！"
    return render(request, 'add_publisher.html', {"error":err_msg})

def delete_publisher(request):
    del_id = request.GET.get('id', None)
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse('删除失败，该出版社不存在')

# 编辑出版社
def edit_publisher(request):
    # 如果是POST请求，说明是要更新出版社名称
    if request.method == 'POST':
        # 获取要更新的id
        edit_id = request.POST.get("id", None)
        # 获取新的名字
        new_name = request.POST.get("publisher_name")
        # 通过id获得出版社对象
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        # 赋值新名字
        publisher_obj.name = new_name
        # 提交到数据库中执行
        publisher_obj.save()

        return redirect('/publisher_list/')

    edit_id = request.GET.get("id", None)
    if edit_id:
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, 'edit_publisher.html', {"publisher":publisher_obj})
    else:
        return HttpResponse('编辑的出版社不存在！')