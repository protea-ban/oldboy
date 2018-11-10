from django.shortcuts import render
from .models import Book
from app01.utils.page import Pagination
# Create your views here.


def index(request):
    current_page = request.GET.get("page", 1)
    all_count = Book.objects.all().count()
    base_url = request.path

    pagination = Pagination(all_count, current_page, base_url, request.GET, per_page=1, max_show=3)

    # print(pagination.start)
    # print(pagination.end)

    book_list = Book.objects.all()[pagination.start : pagination.end]
    # book_list = Book.objects.all()

    return render(request, "index.html", locals())
