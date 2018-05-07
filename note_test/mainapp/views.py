from django.shortcuts import render
from workWithNote.models import Note, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from workWithNote.forms import CategoryForm
import datetime

# Create your views here.

def main(request):
    if request.user and not request.user.is_anonymous:
        form = CategoryForm(initial={'id': 4})
        sort_type = request.POST.get('sort')
        filter_type = request.POST.get('filter')
        notes = None
        if sort_type:
            if sort_type == 'Date':
                notes = Note.objects.filter(username=request.user).order_by('-dt')
            elif sort_type == 'Category':
                notes = Note.objects.filter(username=request.user).order_by('-category')
            elif sort_type == 'Favorites':
                notes = Note.objects.filter(username=request.user).order_by('-favorites')
            else:
                notes = Note.objects.filter(username=request.user).order_by('-dt')
        elif filter_type:
            # if filter_type == 'Date':
            #     clndr_dt = tuple(map(int, request.POST.get('calendar').split('-')))
            #     notes = Note.objects.filter(dt=datetime.date(*clndr_dt))
            #     print(clndr_dt)
            if filter_type == 'Category':
                cat = request.POST.get('category')
                if cat:
                    notes = Note.objects.filter(username=request.user, category=cat)
                cat = None
            elif filter_type == 'Favorites':
                notes = Note.objects.filter(username=request.user, favorites=True)
        if notes is None:
            notes = Note.objects.filter(username=request.user).order_by('-dt')

        paginator = Paginator(notes, 5)
        page = request.GET.get('page')
        try:
            notes = paginator.page(page)
        except PageNotAnInteger:
            notes = paginator.page(1)
        except EmptyPage:
            notes = paginator.page(paginator.num_pages)

        return render(request, 'index.html', {'notes': notes, 'form': form})

    return render(request, 'index.html')