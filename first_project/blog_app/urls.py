from django.urls import path
from . import views


app_name = 'blog_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('topics/', views.topics, name='topics'),
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	path('new_topic/', views.new_topic, name='new_topic'),
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	path('topics/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
	path('new_topic/duplicate/', views.topic_duplicate, name='topic_duplicate'),
	path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]