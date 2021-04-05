from django.shortcuts import render
from .models import Topic

def index(request):
	return render(request, 'blog_app/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'blog_app/topics.html', context)

# Create your views here.
