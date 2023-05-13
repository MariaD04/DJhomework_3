from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_ = request.GET.get('sort')
    phones_ = Phone.objects.all()
    if sort_ == 'name':
        phones_ = phones_.order_by('name')
    elif sort_ == 'min_price':
        phones_ = phones_.order_by('price')
    elif sort_ == 'max_price':
        phones_ = phones_.order_by('-price')
    context = {'phones': phones_}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)