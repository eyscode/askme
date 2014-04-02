# coding=utf-8
from django import forms
from web.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        labels = {
            'title': 'Título',
            'content': 'Descripción'
        }
        fields = ('title', 'content')