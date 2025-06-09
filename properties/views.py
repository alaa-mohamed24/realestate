from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Property

def property_list(request):
    property_list = Property.objects.all()

    category = request.GET.get('category')
    if category:
        property_list = property_list.filter(category=category)

    property_type = request.GET.get('property_type')
    if property_type:
        property_list = property_list.filter(property_type=property_type)

    max_price = request.GET.get('max_price')
    if max_price:
        property_list = property_list.filter(price__lte=max_price)
    
    location = request.GET.get('location')
    if location:
        property_list = property_list.filter(location=location)

    for p in property_list:
        p.formatted_price = intcomma(int(p.price)).replace(",", ".")

    paginator = Paginator(property_list, 4)  # 4 عقارات في الصفحة

    page_number = request.GET.get('page')
    try:
        page_number = int(page_number)
        if page_number < 1:
            page_number = 1
    except (TypeError, ValueError):
        page_number = 1

    page_obj = paginator.get_page(page_number)

    all_locations = Property.objects.values_list('location', flat=True).distinct()

    context = {
        'page_obj': page_obj,
        'category': category,
        'property_type': property_type,
        'max_price': max_price,
        'location': location,
        'all_locations': all_locations,  # ع
    }

   
    return render(request, 'properties/property_list.html', context)

def property_detail(request, property_id): 
    property = get_object_or_404(Property, id=property_id)
 
    formatted_price = intcomma(int(property.price)).replace(",", ".")

    amenities_list = property.amenities.split(',') if property.amenities else []

    return render(request, 'properties/property_detail.html', {
        'property': property,
        'formatted_price': formatted_price,
        'amenities_list': amenities_list,
    })

def about_us(request):
    return render(request, 'properties/about_us.html')