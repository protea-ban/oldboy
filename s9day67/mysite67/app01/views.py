from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def upload(request):

    if request.method == "POST":
        filename = request.FILES["upload_file"].name

        # 通过一点点读，将上传文件写入项目目录下的一个文件中
        with open(filename, "wb") as f:
            for file_i in request.FILES["upload_file"].chunks():
                f.write(file_i)
    else:
        return render(request, "upload.html")

    return HttpResponse("上传OK")

def book(request, year, title):
    print("year:", year)
    print("title:", title)
    return HttpResponse("来一个！")

def home(request):
    return render(request, 'car/home.html')