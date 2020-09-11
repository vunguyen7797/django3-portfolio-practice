from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def all_blogs(request):
    blogs = BlogPost.objects.order_by('-date')

    return render(request, 'blog/all_blogs.html', {"blogs": blogs})
def detail(request, blog_id):
    blog_post = get_object_or_404(BlogPost,pk=blog_id)
    return render(request, 'blog/detail.html',{'id': blog_id, 'blog_post':blog_post})
