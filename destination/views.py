from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from pkg.rest import BaseResponse

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def api_index(request):
    search = request.GET.get('search', '-')
    limit = 10
    page = request.GET.get('page', 0)
    offset = int(page) * int(limit)

    response = requests.get(f"https://rajaongkir.komerce.id/api/v1/destination/domestic-destination", 
    headers={
        'key': 'wT35ADDK53b8aa3829979dc7qijLo6mc'
    },
    params={
        'search': search,
        'limit': limit,
        'offset': offset
    })
    data = response.json()

    return BaseResponse(
        data=data.get('data', []),
        status=response.status_code,
        message=data.get('message', 'Success'),
        error=data.get('error', None)
    )