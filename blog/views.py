# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.urls import reverse_lazy
from blog.forms import Updateform

# Create your views here.

#def home(request):
#    context = {
#    'posts' : Post.objects.all()
#    }
#    return render(request, 'blog/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #slug_field = 'product_slug'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


#def UpdateFormView(request):
#    form = Updateform(request.POST)
#    if form.is_valid():
#        form.save()
#        return redirect('blog-home')
#    return render(request,'blog/post_form.html')


# LoginRequiredMixin, UserPassesTestMixin,
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content']
    #template_name = 'blog/post_form.html'
    context_object_name = 'post'

    #def get_object(self):
    #    return MyModel.objects.get(pk=self.request.GET.get('pk'))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView ):
    model = Post
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html',{'title_name':'About'})
