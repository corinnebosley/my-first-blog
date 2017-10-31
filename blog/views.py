# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.

# This is the root view.
def post_list(request):
    # Filter the list of posts to find all the ones with a publish date and
    # then put them in ascending date order (you can reverse this with a
    # preceding '-', like '-publish_date'
    posts = Post.objects.filter(published_date__lte=timezone.now()).\
        order_by('published_date')
    # Show the rendered page having passed this request object to the
    # post_list template.  The items in the dictionary are to fill in the
    # fields in the template.
    return render(request, 'blog/post_list.html', {'posts': posts})

# This is for a single post in detail.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# This allows the user to create(?) a new blog.  Maybe...
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


# This is for editing an existing post.
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

