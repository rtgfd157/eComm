from django.shortcuts import render ,redirect, HttpResponseRedirect, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import URLShortener
from .forms import URLShortenerForm ,URLShortenerUpdatingForm
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404



class URLShortenerListView(ListView):
    """
    a class for home page that will display exsiting hash links

    will have links to CRUD actions on URLShortener model
    """
    template_name = 'URLShortener_app/home.html'
    context_object_name='ob'
    model = URLShortener

    def get_queryset(self):
        context = {
            'urlshortener': URLShortener.objects.all()
        }
        return context



class URLShortenerCreateView(FormView):
    """
    class for adding URLShortener model by form
    """
    model = URLShortener
    template_name = 'URLShortener_app/add.html'
    form_class =  URLShortenerForm   
    
    def get_success_url(self):
        return reverse("URLShortener-home")

    def get_context_data(self, *args, **kwargs):
        context = super(URLShortenerCreateView, self).get_context_data(*args, **kwargs)
        context["mess"] = "add URLShortener"
        context["button"] = "create"
        return context

    def form_valid(self, form):
        if  not  form.instance.hash or   form.instance.hash  == None:
            print("inn if")
            form.instance.hash = URLShortener.make_hash()
        form.save()
        return super(URLShortenerCreateView, self).form_valid(form)

    

class URLShortenerDeleteView(DeleteView):
    """
    class that will delete URLShortener object 
    """
    model = URLShortener
    template_name = 'URLShortener_app/del.html'

    def get_success_url(self):
        return reverse("URLShortener-home")

    def get_context_data(self, *args, **kwargs):
        context = super(URLShortenerDeleteView, self).get_context_data(*args, **kwargs)
        context["mess"] = "URLShortener"
        return context


# function that will update URLShortener model values
def urlshortener_updateview(request, pk):    
    obj = get_object_or_404(URLShortener, id = pk) 

    if request.method == 'POST':
        p_form=URLShortenerUpdatingForm(request.POST ,instance=obj)
        if  p_form.is_valid():
            if  not  p_form.instance.hash or   p_form.instance.hash  == None:
                p_form.instance.hash = URLShortener.make_hash()
            
            p_form.save()
            
            return redirect ('/')
    else:
        p_form=URLShortenerUpdatingForm(instance=obj)
    context={
            'p_form':p_form
        }

    return render (request ,'URLShortener_app/up.html',context)