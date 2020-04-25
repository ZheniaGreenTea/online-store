from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, SelectDateWidget
from django.http import request, QueryDict

from .models import Profile, Post, Message, Comment






class CommentForm(ModelForm):

    class Meta:
        model = Comment

        fields = ('user', 'text',)

