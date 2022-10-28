from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title':'homepage'
    }
    return render(request,"index.html")
def data(request):
    return render (request,"data.html")
def blog(request):
    return render ("welcome to my 3rd  page ")
def aboutus(request):
    return HttpResponse ("welcome to my 4th page")
