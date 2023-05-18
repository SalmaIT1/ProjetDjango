from django.forms.models import ModelForm
from artyprod_blog.views import PostModel
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import DeleteView

from .models import Comment,PostModel

class PostForm(ModelForm):
    image = forms.ImageField(required=False)
    class Meta :
        model = PostModel
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostModel
    success_url = '/blog'    