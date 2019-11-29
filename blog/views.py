# blog/views.py
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # new
from .models import Post

class BlogListView(ListView):
	model = Post
	template_name = 'home.html'


class BlogDetailView(DetailView): # new
	model = Post
	template_name = 'post_detail.html'

class BlogCreateView(CreateView): # new
	model = Post
	template_name = 'post_new.html'
	fields = '__all__'

class BlogUpdateView(UpdateView): # new
	model = Post
	template_name = 'post_edit.html' 	# new
	fields = ['title', 'body']		# new

class BlogDeleteView(DeleteView): # new
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')