from django.shortcuts import render,HttpResponse
from app01 import models
from django.contrib.contenttypes.models import ContentType
# Create your views here.


def test(request):
    # 1.在价格策略表中添加一条数据
    # models.PricePolicy.objects.create(
    #     valid_period=7,
    #     price=6.6,
    #     content_type=ContentType.objects.get(model='course'),
    #     object_id=1
    # )

    # models.PricePolicy.objects.create(
    #     valid_period=14,
    #     price=9.9,
    #     content_object=models.Course.objects.get(id=1)
    # )

    # 2.根据某个价格策略对象，找到他对应的表和数据，如：管理课程名称
    # price = models.PricePolicy.objects.get(id=2)
    # print(price.content_object.name) # 自动帮你找到

    # 3.找到某个课程关联的所有价格策略
    obj = models.Course.objects.get(id=1)
    for item in obj.policy_list.all():
        print(item.id,item.valid_period,item.price)


    return HttpResponse('...')