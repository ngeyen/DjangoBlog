from django.shortcuts import render
from .models import SearchQuery
from blog.models import BlogPost

# Create your views here.
def searchView(request):
    query =request.GET.get('search', None)
    
    user=None
    if request.user.is_authenticated:
        user = request.user
    context = {'query': query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    
    
    return render(request, 'searches/view.html',context)