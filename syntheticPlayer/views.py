from datetime import date
from django.shortcuts import redirect, render, get_object_or_404
from .models import syntheticPlayer, categories
from django.core.paginator import Paginator

# Create your views here.



def index(request):
    subscriptions = syntheticPlayer.objects.filter(isActive=1, isHome=1)
    kategoriler = categories.objects.all()

    return render(request, 'syntheticPlayer/index.html', {
        'categories': kategoriler,
        'subscriptions': subscriptions
    })
    
def search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q = request.GET["q"]
        subscriptions = syntheticPlayer.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler = categories.objects.all()
    else:
        return redirect("/subscriptions")
    
    
    return render(request, 'syntheticPlayer/search.html', {
        'categories': kategoriler,
        'subscriptions': subscriptions,
    })
    

def details(request, slug):
    subscriptions = get_object_or_404(syntheticPlayer, slug=slug)

    context = {
        'subscriptions': subscriptions
    }
    return render(request, 'syntheticPlayer/details.html', context)


def getSubscriptionsByCategory(request, slug):
    subscriptions = syntheticPlayer.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = categories.objects.all()
    
    paginator = Paginator(subscriptions, 2)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)
    
    
    return render(request, 'syntheticPlayer/list.html', {
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })