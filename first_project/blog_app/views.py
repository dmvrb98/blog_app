from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404

def index(request):
	'''this one is rendering home page, and this is the only one page that
	visitor can see without registration'''
	return render(request, 'blog_app/index.html')

@login_required
def topics(request):
	'''this one is showing all topics ordered by date'''
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'blog_app/topics.html', context)

@login_required
def topic(request, topic_id):
	'''this one shows all entries bellowing to a chosen topic starting
	from the latest one'''
	topic = Topic.objects.get(id=topic_id)
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'blog_app/topic.html', context)

@login_required
def new_topic(request):
	'''this one is creating new topic and binding user with topic'''
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('blog_app:topics')

	context = {'form': form}
	return render(request, 'blog_app/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	'''this one is creating new entry in a chosen topic'''
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

@login_required
def edit_entry(request, entry_id):
	'''this one allows editors to make changes in their entries'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method !='POST':
		form=EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog_app:topic', topic_id=topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'blog_app/edit_entry.html', context)


# Create your views here.
