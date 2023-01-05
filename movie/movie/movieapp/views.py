from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import movie
from .forms import MovieForm
# Create your views here.
def index (request):
    a=movie.objects.all()
    return render (request,'index.html',{'a':a})

def detail (request,movie_id):
    b=movie.objects.get(id=movie_id)
    return render (request,'detail.html',{'b':b})

def add (request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        Movie=movie(name=name,age=age,desc=desc,img=img)
        Movie.save();
    return render (request, 'add.html')

def update (request,id):
    mov=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,'edit.html',{'movie':mov,'form':form})

def delete (request,id):
    if request.method=='POST':
        d=movie.objects.get(id=id)
        d.delete()
        return redirect('/')
    return render(request,'delete.html')
