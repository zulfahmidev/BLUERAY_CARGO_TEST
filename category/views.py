from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
from country.models import Country
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from pkg.rest import BaseResponse

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def api_index(request):
    categories = _paginate(request)
    serializer = CategorySerializer(categories, many=True)
    return BaseResponse(serializer.data, status=200, message='Success')

@login_required
def index(request, country_id):
    country = Country.objects.get(id=country_id)

    if not country:
        return redirect('country.index')
    
    categories = _paginate(request, country)
    return render(request, 'category/index.html', {
        'categories': categories,
        'country': country
    })

@login_required
def create(request, country_id):
    country = Country.objects.get(id=country_id)

    if not country:
        return redirect('country.index')
    
    if request.method == 'POST':
        result = save(request, country)
        if (result != True) :
            return render(request, 'category/create.html', {
                'form': result,
                'error': 'Please correct the errors below.',
                'country': country
            })
        return redirect('category.index', country_id=country_id)

    return render(request, 'category/create.html', {
        'country': country
    })

@login_required
def edit(request, country_id, category_id):
    country = Country.objects.get(id=country_id)
    category = Category.objects.get(id=category_id)

    if not country or not category:
        return redirect('category.index', country_id=country_id)
    
    if request.method == 'POST':
        result = save(request, country, category)
        if (result != True) :
            return render(request, 'category/edit.html', {
                'form': result,
                'error': 'Please correct the errors below.',
                'category': category,
                'country': country
            })
        return redirect('category.index', country_id=country_id)
    
    form = CategoryForm(instance=category)
    return render(request, 'category/edit.html', {
        'form': form,
        'category': category,
        'country': country
    })

@login_required
def delete(request, country_id, category_id):
    country = Country.objects.get(id=country_id)
    category = Category.objects.get(id=category_id)

    if not country or not category:
        return redirect('category.index', country_id=country_id)

    if request.method == 'POST':
        category.delete()
        return redirect('category.index', country_id=country_id)

    return redirect('category.index', country_id=country_id)

def save(request, country, category=None):
    data = request.POST.copy()
    data['country'] = country
    if category:
        form = CategoryForm(data, instance=category)
    else:
        form = CategoryForm(data)

    if not form.is_valid():
        return form

    form.save()

    return True

def _paginate(request, country=None) :
    page_number = request.GET.get('page')
    if country:
        categories = Category.objects.filter(country=country)
    else:
        categories = Category.objects.all()

    query = request.GET.get('search')
    if query:
        categories = categories.filter(category_title__icontains=query)


    country_id = request.GET.get('country_id')
    if country_id:
        categories = categories.filter(country_id=country_id)

    paginator = Paginator(categories, 10)
    page_obj = paginator.get_page(page_number)
    return page_obj