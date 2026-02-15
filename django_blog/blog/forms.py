from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "content"]
    

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        tag_names = self.cleaned_data['tags'].split(',')
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name.strip())
            instance.tags.add(tag)

        return instance

