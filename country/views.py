from django.shortcuts import render, redirect
from .models import Country
from .forms import CountryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountrySerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from pkg.rest import BaseResponse

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def api_index(request):
    countries = _paginate(request)
    serializer = CountrySerializer(countries, many=True)
    return BaseResponse(serializer.data, 200, 'Success')

@login_required
def index(request):
    countries = _paginate(request)
    return render(request, 'country/index.html', {
        'countries': countries,
    })

@login_required
def create(request):
    if request.method == 'POST':
        result = save(request)
        if (result != True) :
            return render(request, 'country/create.html', {
                'form': result,
                'error': 'Please correct the errors below.'
            })
        return redirect('country.index')

    return render(request, 'country/create.html')

@login_required
def edit(request, country_id):
    country = Country.objects.get(id=country_id)

    if not country:
        return redirect('country.index')
    
    if request.method == 'POST':
        result = save(request, country)
        if (result != True) :
            return render(request, 'country/edit.html', {
                'form': result,
                'error': 'Please correct the errors below.'
            })
        return redirect('country.index')
    
    form = CountryForm(instance=country)
    return render(request, 'country/edit.html', {
        'form': form,
        'country': country
    })

@login_required
def delete(request, country_id):
    country = Country.objects.get(id=country_id)

    if not country:
        return redirect('country.index')

    if request.method == 'POST':
        country.delete()
        return redirect('country.index')

    return redirect('country.index')

def save(request, country=None):
    if country:
        form = CountryForm(request.POST, request.FILES, instance=country)
    else:
        form = CountryForm(request.POST, request.FILES)

    if not form.is_valid():
        return form

    form.save()

    return True

def _paginate(request) :
    page_number = request.GET.get('page')
    countries = Country.objects.all()

    query = request.GET.get('search')
    if query:
        countries = countries.filter(country_name__icontains=query)

    paginator = Paginator(countries, 10)
    page_obj = paginator.get_page(page_number)
    return page_obj