from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
	"""Creating topic form"""
	class Meta:
		model = Topic
		fields = {'text',}
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	"""Creating entry form"""
	class Meta:
		model = Entry
		fields = {'text',}
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}