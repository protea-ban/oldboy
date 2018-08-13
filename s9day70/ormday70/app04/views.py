from django.shortcuts import render, HttpResponse

# Create your views here.


def transfer(request):
    if request.method == "POST":
        from_ = request.POST.get("from")
        to_ = request.POST.get("to")
        money = request.POST.get("money")

        print("{} 给 {} 转了 {} 块钱".format(from_, to_, money))
        return HttpResponse("转账成功")

    return render(request, "transfer.html")