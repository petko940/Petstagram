from django.shortcuts import render

from Petstagram.photos.models import Photo


# Create your views here.

def photo_add(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
