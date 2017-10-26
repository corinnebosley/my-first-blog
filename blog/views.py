# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
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





