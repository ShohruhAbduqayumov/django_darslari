from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<font color='blue'><h1>Assalomu aleykum hayrli kun!"
                        " <br> Ozoda bugun ham osh qilasizmi?"
                        "<br> Yoki Sojida opaga aytelikmi</h1></font>")

def goodbye(request):
    return  HttpResponse("Goodbye guruppa!!!")


def ism(request):
    return HttpResponse("<font color='red'><h1><i> ABDUQAYUMOV SHOHRUH</i></h1></font>")

def sahifa(request):
    names = ['Shohruh', 'Shohjahon', 'Sabohat']
    name = 'Shohruh'
    return render(request, 'index.html', {'ism': name, 'ismlar': names})