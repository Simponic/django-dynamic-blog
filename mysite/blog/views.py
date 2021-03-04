from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Blog, Comment

import time

def index(request):
    latest_blogs = Blog.objects.order_by('-posted')[:5]
    return render(request, "blog/base_index.html", {'latest_blogs' : latest_blogs})

def blog(request, blog_id):
    blog_entry = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/base_blog.html", {"blog_entry" : blog_entry, 'comments' : blog_entry.comment_set.order_by("-posted")})

def archive(request):
    return render(request, "blog/base_archive.html", {"blogs": Blog.objects.order_by('-posted')})

def about(request):
    unix_timestamp = str(time.time())
    return render(request, "blog/base_about.html", {"unix_timestamp" : unix_timestamp})

def tips(request):
    unix_timestamp = str(time.time())
    return render(request, "blog/base_tips.html", {"unix_timestamp" : unix_timestamp})

def comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        commenter = request.POST['username']
        email = request.POST['email']
        content = request.POST['content']
        posted = timezone.now()
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'blog/base_index.html')
    else:
        blog.comment_set.create(commenter=commenter, email=email, content=content, posted=posted)
        blog.save()
        return HttpResponseRedirect(reverse('blog:blog', args=(blog_id,)))