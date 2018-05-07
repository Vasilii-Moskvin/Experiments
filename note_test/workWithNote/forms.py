from django import forms
from .models import Note, Category
from django.db import models

class SaveNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['dt', 'unique_id', 'username']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['category']