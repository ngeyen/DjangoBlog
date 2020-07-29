from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404
# Create your views here.

"""
    to raise the 404 exceptions we could either catch it or use get_object_or_404 method,
    surrounding the lookup with a try-except block will become combersome with time and make the 
    class uneccerarily long
"""
#right method

# GET -> 1 Object is returned
# filter -> list [] of objects 
def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 0:
        raise Http404
    blogObject = queryset.first()

    #blogObject = get_object_or_404(BlogPost, slug = slug)
    template_name = "blog_post_detail.html"
    context = {"object": blogObject}
    return render(request, template_name, context)


def blogPostListView(request):
    #list out objects or could be a search view
    qs = BlogPost.objects.all() # queryset -> list of python objects
    template_name = 'blog_post_list.html' 
    context = {'object_list': qs}
    return render(request, template_name, context)

def blogPostCreateView(request):
    template_name = 'blog_post_create.html' 
    context = {'form': []}
    return render(request, template_name, context)

def blogPostDetailView(request):
    #1 object -> detail view
    blogObject = get_object_or_404(BlogPost, slug = slug)
    template_name = "blog_post_detail.html"
    context = {"object": blogObject}
    return render(request, template_name, context)

def blogPostUpdateView(request):
    blogObject = get_object_or_404(BlogPost, slug = slug)
    template_name = "blog_post_update.html"
    context = {"object": blogObject, "form": None}
    return render(request, template_name, context)

def blogPostDeleteView(request):
    blogObject = get_object_or_404(BlogPost, slug = slug)
    template_name = "blog_post_delete.html"
    context = {"object": blogObject}
    return render(request, template_name, context)









'''
Method 2

def blog_post_detail_page(request, post_id):
    try:
        blogObject = BlogPost.objects.get(id=post_id)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise http404

    template_name = "blog_post_detail.html"
    context = {"object": blogObject}
    return render(request, template_name, context)
'''