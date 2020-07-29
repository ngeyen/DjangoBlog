from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost


def index(request):
    title = "Welcome to Victory's Blog"
    
    qs = BlogPost.objects.all().published()[:3]
    context = {"intro": title, 'blog_list': qs}
    return render(request,"index.html", context) #rendering context within html

def contact(request):

    template_name = "form.html"
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        print(form.cleaned_data)
   
    context = {
        "title": "Contact Us",
        "form": form,
        "action": "Send message"

    }
   
    return render(request, template_name, context)

def about(request):

    template_name = "about.html"
    context = {
        "title": "About Us",
    }
    return render(request, template_name, context)

 





def exammple_page(request):
    context= {"title": "Example"}
    template_name ="index.html"
    if request.user.is_authenticated:
        context = {"title": request.user, "message": ["Sandblasting", "Painting", "Lead exposure", "Compressed air", "Benzene", "Organic solvents", "Carbon dioxide and nitrogen", "Asbestos, fiberglass and manmade mineral fibers", "Mercury","Methanol"], "card_title": "Your Message"}
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item) 

