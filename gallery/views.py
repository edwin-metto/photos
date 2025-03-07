from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import Image

def home(request):
    
    if request.user.is_authenticated:
        return redirect('upload_image')  
    else:
        return redirect('login')  


def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('upload_image')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def upload_image(request):

    if request.method == 'POST' and request.FILES.get('image'):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')  
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


@login_required
def image_list(request):

    images = Image.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})
@login_required
def profile(request):
    return render(request, 'registration/profile.html')


def like_image(request, image_id):
    image = Image.objects.get(id=image_id)
    image.likes += 1
    image.save()
    return redirect('image_list')

def dislike_image(request, image_id):
    image = Image.objects.get(id=image_id)
    image.dislikes += 1
    image.save()
    return redirect('image_list')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')  
    
    return redirect('image_list')  


@login_required
def image_list(request):
    images = Image.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})

