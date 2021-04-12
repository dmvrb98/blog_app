from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

def index(request):
	return render(request, 'blog_app/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'blog_app/topics.html', context)

def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'blog_app/topic.html', context)

def new_topic(request):
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog_app:topics')

	context = {'form': form}
	return render(request, 'blog_app/new_topic.html', context)


def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method !='POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('blog_app:topic', topic_id=topic_id)
	context = {'topic': topic, 'form': form}
	return render(request, 'blog_app/new_entry.html', context)

# Create your views here.
