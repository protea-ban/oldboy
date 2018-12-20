from django.shortcuts import render, HttpResponse
from app01.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *


# Create your views here.
class BookViewSet(APIView):
    def get(self, request, *args, **kwargs):
        book_list = Book.objects.all()
        # from django.forms.models import model_to_dict
        # import json
        # data = []
        # for obj in book_list:
        #     data.append(model_to_dict(obj))
        #
        # return HttpResponse(json.dumps(data))

        # 方式2
        # data = serializers.serialize("json", book_list)
        # return HttpResponse(data)

        # 方式3
        # bs = BookSerializers(book_list, many=True)
        # bs = BookModelSerializers(book_list, many=True)

        # 超链接时需要增加参数
        bs = BookModelSerializers(book_list, many=True, context={'request': request})
        return Response(bs.data)

    def post(self, request, *args, **kwargs):
        # bs = BookSerializers(data=request.data, many=False)
        # request.data：post的数据
        # bs = BookModelSerializers(data=request.data, many=False)

        # 超链接时需要增加参数
        bs = BookModelSerializers(data=request.data, many=False, context={'request': request})

        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return HttpResponse(bs.errors)


class PublishViewSet(APIView):
    def get(self, request, *args, **kwargs):
        publish_list = Publish.objects.all()
        ps = PublishModelSerializers(publish_list, many=True)

        return Response(ps.data)

    def post(self, request):
        ps = PublishModelSerializers(data=request.data, many=False)

        if ps.is_valid():
            print(ps.validated_data)
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.error)


class AuthorViewSet(APIView):
    def post(self, request):
        ass = AuthorSerializers(data=request.data)

        if ass.is_valid():
            ass.save()
            return Response(ass.data)
        else:
            return Response(ass.errors)


class BookDetailView(APIView):
    def get(self, request, id):
        book_obj = Book.objects.filter(pk=id).first()
        # bs = BookModelSerializers(book_obj)

        # 超链接时需要增加参数
        bs = BookModelSerializers(book_obj, context={'request': request})
        return Response(bs.data)

    def put(self, request, id):
        book_obj = Book.objects.filter(pk=id).first()
        # bs = BookModelSerializers(book_obj, data=request.data)

        # 超链接时需要增加参数
        bs = BookModelSerializers(book_obj, data=request.data, context={'request': request})
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, id):
        Book.objects.filter(pk=id).delete()
        return Response()


class PublishDetailView(APIView):
    def get(self, request, pk):
        print("id######", pk)
        publish_obj = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish_obj)
        return Response(ps.data)

    def put(self, request, pk):
        publish_obj = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish_obj, data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors)

    def delete(self, request, pk):
        Publish.objects.filter(pk=pk).delete()
        return Response()
