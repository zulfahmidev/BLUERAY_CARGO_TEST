import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from category.models import Category
from country.models import Country
from country.serializers import CountrySerializer
from .serializers import FreightInputSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from pkg.rest import BaseResponse

RAJAONGKIR_API_KEY = "wT35ADDK53b8aa3829979dc7qijLo6mc"

@csrf_exempt
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def calculate_freight(request):
    serializer = FreightInputSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        country_id = data['country_id']
        category_id = data['category_id']
        destination_id = data['destination_id']
        weight = data['weight']

        try:
            country = Country.objects.get(pk=country_id)
            category = Category.objects.get(pk=category_id, country=country)
        except (Country.DoesNotExist, Category.DoesNotExist):
            return BaseResponse(message='Error', error={"error": "Invalid country or category"}, status=400)

        rajaongkir_url = f"https://rajaongkir.komerce.id/api/v1/calculate/domestic-cost"
        headers = {
            "key": RAJAONGKIR_API_KEY,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            'origin': destination_id,
            'destination': destination_id,
            'weight': weight,
            'courier': 'jne'
        }
        try:
            raja_response = requests.post(rajaongkir_url, headers=headers, params=params)
            if raja_response.status_code != 200:
                return BaseResponse(message='Error', error={"error": "Failed to get domestic price"}, status=502)
            domestic_data = raja_response.json()

            domestic_price = domestic_data.get('data', {})[0].get('cost', 0)
        except Exception as e:
            return BaseResponse(message='Error', error={"error": "Error connecting to RajaOngkir API", "detail": str(e)}, status=500)

        international_price = weight * float(category.price_per_kilo)
        total_price = international_price + float(domestic_price)

        return BaseResponse({
            "origin": CountrySerializer(country, many=False).data,
            "destination_id": destination_id,
            "category_name": category.category_title,
            "international_price": international_price,
            "domestic_price": domestic_price,
            "total_price": total_price
        }, 200, 'Success')
    return BaseResponse(message='Error', status=status.HTTP_400_BAD_REQUEST, error=serializer.errors)