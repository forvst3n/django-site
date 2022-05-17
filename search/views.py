from django.http import HttpResponse
from django.shortcuts import render
from main.models import GPU


def search(request):
    #Search item 
    data = request.GET['q'] #Get data with url 
    print(data)
    necessary = []
    for v in GPU.objects.all():
        if data in v.title and len(data) >= 3:
            necessary.append(v)
        if v.title == data and data not in v.title:
            necessary.append(v)
    context = {
        'items':necessary,
    }
    return render(request,'search/search_detail.html',context)
    
