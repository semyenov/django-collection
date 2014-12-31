from django.shortcuts import render_to_response
from music.models import *
from music.forms import *


def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    tracks = album.tracks.order_by('number')
    print(album)
    return render_to_response('album_view.html', {'album': album, 'tracks': tracks})


def band_view(request, album_id):
    band = Band.objects.get(id=album_id)
    print(band)
    album_form = AddAlbum()
    albums = band.albums.order_by('-year')
    return render_to_response('band_view.html', {'band': band, 'albums': albums, 'album_form': album_form})


def create_task(request):
    if request.method == 'POST':
        form = AddAlbum(request.POST, request.FILES,)
        if form.is_valid():
            album = form.save(commit=False)
            if not task.task_photo:
                number = random.randint(1,6)
                task.task_photo = 'task_photos/page4-img'+str(number)+'.jpg'
            task.user = request.user
            task.save()
            return redirect('/task/'+str(task.id))
    return HttpResponseBadRequest()