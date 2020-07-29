
from django.urls import re_path, path
from blog.views import (
    blogPostDetailView,
    blogPostListView,
    blogPostUpdateView,
    blogPostDeleteView,
    blogPostCreateView
)

urlpatterns = [
   # path('blog/<int:post_id>/', blog_post_detail_page),
    
    path('', blogPostListView),
    path('new/', blogPostCreateView),
    path('<str:slug>/', blogPostDetailView),
    path('<str:slug>/edit/', blogPostUpdateView),
    path('<str:slug>/delete/', blogPostDeleteView),
]
