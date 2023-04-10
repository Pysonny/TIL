from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm
# Create your views here.
def index(request):
    albums = Album.objects.all()
    context = {
        'albums' : albums,
    }
    return render(request, 'albums/index.html', context)

def create(request):
    if request.method == 'POST':
        # print(request.FILES)
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            return redirect('albums:index')
    else:
        form = AlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'albums/create.html', context)

def delete(request,pk):
    article = Album.objects.get(pk=pk)
    article.delete()
    return redirect('albums:index')