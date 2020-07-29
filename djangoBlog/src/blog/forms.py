from django import forms
from .models import BlogPost
from bootstrap_datepicker_plus import DatePickerInput

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)
    publish_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']
        widgets = {
            'publish_date': DatePickerInput(format='%d/%m/%Y %H:%M')
        }

    #Custom form validation method
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        #title_iexact -> disables the case sensitive property t =T
        # icontains -> if title is contained in 'title', the error will be raised
        instance = self.instance
        qs = BlogPost.objects.filter(title=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # same as id = instance.id

        if qs.exists():
            raise forms.ValidationError("This tile has already been used. Please try a new title")
        return title 
