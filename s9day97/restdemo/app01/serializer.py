#!/usr/bin/env python  
#-*- coding:utf-8 -*-
from app01.models import *
from rest_framework import serializers


# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     pub_date = serializers.DateField()
#     # 一对多用CharField，里面加上source
#     publish = serializers.CharField(source="publish.name")
#     # 多对多用SerializerMethodField
#     authors = serializers.SerializerMethodField()
#
#     # 此时authors值取决于下面函数的返回值
#     def get_authors(self, obj):
#         authors_temp = []
#         for authors_obj in obj.authors.all():
#             authors_temp.append(authors_obj.name)
#
#         return ",".join(authors_temp)


class BookModelSerializers(serializers.ModelSerializer):
    # 默认将普通字段转化
    class Meta:
        model = Book
        fields = "__all__"

    # 定制url
    publish = serializers.HyperlinkedIdentityField(
        view_name="detailpublish",
        lookup_field="publish_id",
        lookup_url_kwarg="pk"
    )

    # 特殊字段可以自己添加
    # 一对多用CharField，里面加上source
    # publish = serializers.CharField(source="publish.name")
    # publish = serializers.CharField(source="publish.pk")
    # 多对多用SerializerMethodField
    # authors = serializers.SerializerMethodField()
    #
    # # 此时authors值取决于下面函数的返回值
    # def get_authors(self, obj):
    #     authors_temp = []
    #     for authors_obj in obj.authors.all():
    #         authors_temp.append(authors_obj.name)
    #
    #     return ",".join(authors_temp)

    # 存在定制字段，所以要改写create方法
    # def create(self, validated_data):
    #     print("validated_data", validated_data)
    #     book_obj = Book.objects.create(title=validated_data["title"], price=validated_data["price"], pub_date=validated_data["pub_date"], publish_id=validated_data["publish"]["pk"])
    #     book_obj.authors.add(*validated_data["authors"])
    #
    #     return book_obj


# class PublishSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length=32)
#     email = serializers.EmailField()
class PublishModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"


class AuthorSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
