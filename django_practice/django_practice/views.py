from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request,"index.html",
    {"title":"Hllo World","l":["ok","kusa","nashi"]})

def hoge(request):
    if request.method == "POST":
        return HttpResponse("Hoge")
    elif request.method =="GET":
        return HttpResponse("hoge")
    else:
        return HttpResponse("Foo")

def fuga(request,foo):
    return render(request,"fuga.html",{'title': foo})

def search(request):
    q = request.GET.get("q")
    return HttpResponse(q)

def render_form(request):
    return render(request,"login.html")

def login(request):
    if (request.POST["username"] and request.POST["email"]):
        return render(request,"check.html",{"email":request.POST["email"],"username":request.POST["username"]})
    else:
        return render(request,"error.html")

def upload(request):
    if (request.method=="POST" 
        and request.FILES
        and request.FILES["image"]):
        binary = request.FILES["image"]
        image = open("static/hoge.png","wb")
        for chunk in binary.chunks():
            image.write(chunk)
        return render(request,"result.html")
    else:
        # return HttpResponseRedirect("/form")
        return render(request,"form.html")

def form(request):
    return render(request,"form.html")