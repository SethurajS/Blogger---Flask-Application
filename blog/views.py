from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    contexts = {
        'posts': Blog.objects.all(),
        'title': 'Home'
    }

    return render(request,'blog/home.html',contexts)

class PostListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-posted']

class PostDetailView(DetailView):
    model = Blog

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})
