from django.shortcuts import render, redirect, get_object_or_404
from .models import Signup
from django.utils import timezone

# Create your views here.
def home(request):
    members = Signup.objects.all()
    return render(request, 'home.html', {'members':members})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_member = Signup()
    new_member.name = request.POST['name']
    new_member.age = request.POST['age']
    new_member.pub_date = timezone.now()
    new_member.email = request.POST['email']
    new_member.introduce = request.POST['introduce']
    new_member.save()
    return redirect('home')

def detail(request, id):
    member = get_object_or_404(Signup, pk=id)
    return render(request, 'detail.html', {'member':member})

def edit(request, id):
    edit_member = get_object_or_404(Signup, id=id)
    return render(request, 'edit.html', {'member':edit_member})

def update(request, id):
    update_member = get_object_or_404(Signup, id=id)
    update_member.name = request.POST['name']
    update_member.age = request.POST['age']
    update_member.pub_date = timezone.now()
    update_member.email = request.POST['email']
    update_member.introduce = request.POST['introduce']
    update_member.save()
    return redirect('detail', str(update_member.id))

def delete(request, id):
    delete_member = get_object_or_404(Signup, id=id)
    delete_member.delete()
    return redirect('home')

    

    
    
    

    
