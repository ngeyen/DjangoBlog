from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet): #custom query set
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
    
    def search(self, query):
        lookup = (
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(User__first_name__icontains=query)|
            Q(User__last_name__icontains=query)|
            Q(User__username__icontains=query)
        )
        return self.filter(lookup)
    


class BlogPostManager(models.Manager):#uses this to only display what is published
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()
    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class BlogPost(models.Model):
    User = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True) #hello world -> hello-world
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField( auto_now=False, auto_now_add=False, blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) #when added to the database, the field changes to that time
    updated = models.DateTimeField(auto_now=True) #when save is hit, the time changes

    objects = BlogPostManager()
    class Meta:
        ordering = ['-updated', '-publish_date', '-timestamp' ]

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
    

    
