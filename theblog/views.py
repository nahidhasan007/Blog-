from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, ovimot
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
#	return render(request,'home.html',{})
class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'addpost.html'
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'updatepost.html'
	fields = ['title','body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'deletepost.html'
	success_url = reverse_lazy('home')

class CommentView(CreateView):
	model = ovimot
	template_name = 'commentpost.html'
	fields = '__all__'
	success_url = reverse_lazy('home')








