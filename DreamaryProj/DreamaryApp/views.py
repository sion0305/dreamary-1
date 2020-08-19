from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

# Create your views here.
def home(request):
    blogs = Designer.objects
    return render(request, 'home.html', {'blogs':blogs})
    
def create(request):
    if request.method == 'POST':
        designer = Designer()
        designer.image = request.FILES['p']
        designer.name = request.POST['n']
        designer.address = request.POST['a']
        designer.description = request.POST['d']
        designer.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def delete (request, pk):
    blog = get_object_or_404(Designer, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, pk):
    detail = get_object_or_404(Designer, pk=pk)
    return render(request, 'detail.html', {'detail':detail})