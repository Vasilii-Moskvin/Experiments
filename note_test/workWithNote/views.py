from django.shortcuts import render, HttpResponseRedirect
from .forms import SaveNoteForm
import datetime
import uuid
from workWithNote.models import Note
from django.contrib.auth.models import User

# Create your views here.

def create_note(request):
    form = SaveNoteForm()
    return render(request, 'create_note.html', {'form': form})


def open_note(request, note_uuid):
    note = list(Note.objects.filter(unique_id=note_uuid))[0]
    form = SaveNoteForm(initial={'header_note': note.header_note,
                                 'category': note.category,
                                 'text': note.text,
                                 'favorites': note.favorites})
    return render(request, 'open_note.html', {'form': form, 'unique_id': note.unique_id})


def change_note(request, unique_id):
    if request.method == 'POST':
        qs = Note.objects.get(pk=unique_id)
        form = SaveNoteForm(request.POST, instance=qs)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.username = request.user
            temp.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/user/change_note/' + str(unique_id) + '/')
    return HttpResponseRedirect('/user/create_note/' + str(unique_id) + '/')


def save_note(request):
    if request.method == 'POST':
        form = SaveNoteForm(request.POST, {'dt': datetime.datetime.now(),
                                           'unique_id': uuid.uuid4(),
                                           'username': request.user})
        if form.is_valid():
            temp = form.save(commit=False)
            temp.username = request.user
            temp.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/user/create_note/')
    return HttpResponseRedirect('/user/create_note/')


def delete_note(request, unique_id):
    if request.method == 'POST':
        qs = Note.objects.get(pk=unique_id)
        qs.delete()

    return HttpResponseRedirect('/')


