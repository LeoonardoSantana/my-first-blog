from dataclasses import fields
from pdb import post_mortem
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
