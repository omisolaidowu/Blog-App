from django import forms
from .models import art_gallery
from .models import *
from django.contrib import messages
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class my_engine(forms.ModelForm):
	published = forms.BooleanField(required=False)
	title = forms.CharField(widget=forms.Textarea(attrs={"rows":1, "cols":70, "placeholder":"Enter the Title of your work"}))
	content = forms.CharField(widget=SummernoteWidget(attrs={"class": "custom-class"}))
	desc_of_art = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":70, "placeholder":"Enter a short description of your art work"}))
	pictures  = forms.ImageField(label='upload an image')
	
	class Meta:
		model = art_gallery
		fields=('published','title', 'content', 'desc_of_art', 'pictures','category',)


