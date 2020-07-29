from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import BlogPost
from django.http import Http404
from .forms import BlogPostForm, BlogPostModelForm

def blogPostListView(request):
    #list out objects or could be a search view
    title = 'All Posts'
    qs = BlogPost.objects.all().order_by('-updated')   # queryset -> list of python objects
    if request.user.is_authenticated:
        new_qs = BlogPost.objects.filter(User=request.user)
        qs = (qs | new_qs).distinct() 
    template_name = 'blog/list.html' 
    context = {'object_list': qs, 'title':title}
    return render(request, template_name, context)

@staff_member_required
#@login_required(login_url='/login')
def blogPostCreateView(request):
    title = 'Create new Post'
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        #print(form.cleaned_data)
        #obj = BlogPost.objects.create(**form.cleaned_data)
        #form = BlogPostForm()
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        #form.save()
        form = BlogPostModelForm()
        
    template_name = 'form.html' 
    context = {'form': form, 'title': title, 'action':'Create Post'}
    return render(request, template_name, context)

def blogPostDetailView(request, slug):
    #1 object -> detail view
    blogObject = get_object_or_404(BlogPost, slug  = slug)
    template_name = "blog/detail.html"
    context = {"object": blogObject}
    return render(request, template_name, context)

@staff_member_required
def blogPostUpdateView(request, slug):
    postInstance = get_object_or_404(BlogPost, slug=slug)
    title = f"Update {postInstance.title}"
    form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=postInstance)
    if form.is_valid():
        form.save()
    
    template_name = "form.html"
    context = {"form": form, "title": title, "action":"Update Post"}
    return render(request, template_name, context)

@staff_member_required
def blogPostDeleteView(request, slug):
    postInstance = get_object_or_404(BlogPost, slug = slug)
    
    template_name = "blog/delete.html"
    if request.method=="POST":
        postInstance.delete()
        return redirect("/blog")
    context = {"object": postInstance}
    return render(request, template_name, context)
