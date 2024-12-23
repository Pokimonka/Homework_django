from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')

def get_phones(sort):
    if sort == 'name':
        phone_obj = Phone.objects.all().order_by('name').values()
    elif sort == 'min_price':
        phone_obj = Phone.objects.all().order_by('price').values()
    elif sort == 'max_price':
        phone_obj = Phone.objects.all().order_by('-price').values()
    else:
        phone_obj = Phone.objects.all()
    return phone_obj

def show_catalog(request):
    sort = request.GET.get('sort')
    phone_obj = get_phones(sort)

    template = 'catalog.html'

    context = {
        'phones': phone_obj
    }
    return render(request, template, context)


def create_current_phone_dict(slug):
    # не получилось просто передать phone_obj в show_product
    # не работает потому что в product.html нет перебора по элементам phone
    # в общем, пришлось делать словарь
    phone_obj = Phone.objects.filter(slug=slug)
    phone = {}
    for p in phone_obj:
        phone['name'] = p.name
        phone['price'] = p.price
        phone['image'] = p.image
        phone['release_date'] = p.release_date
        phone['lte_exists'] = p.lte_exists
    return phone

def show_product(request, slug):
    template = 'product.html'
    phone = create_current_phone_dict(slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
