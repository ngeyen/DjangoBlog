
from django.conf import settings
from django.contrib import admin
from django.urls import re_path, path, include
from blog.views import blogPostCreateView
from .views import (
    index, contact,about
)
from searches.views import searchView

urlpatterns = [
   # path('blog/<int:post_id>/', blog_post_detail_page),

    path('blog-new/', blogPostCreateView),
    path('',index),
    path('search/', searchView),
    path('contact/', contact),
    path('about/', about),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),


]
if settings.DEBUG:
    #test mode 
    from django.conf.urls.static import static
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
