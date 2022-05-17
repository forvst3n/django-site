from django.shortcuts import render
from .models import GPU,Comment
from .forms import CommentInputForm


def main_page(request):
    #Main page and all objects
    context = {
        'items':GPU.objects.all(),
    }

    return render(request,'main/index.html',context)
def item_detail(request,title):
    #Show item page if user moved url
    videocart = GPU.objects.get(title=title)
    
    form = CommentInputForm()
    if request.method == 'POST':
        form = CommentInputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.gpu = videocart
            form.save()
    context = {
        'item':videocart,
        'comments':Comment.objects.filter(gpu=videocart), #Get comments 
        'form':form,
    }
    return render(request,'main/detail.html',context)

