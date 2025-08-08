from rest_framework import serializers

class FreightInputSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    destination_id = serializers.IntegerField()
    weight = serializers.FloatField(min_value=0.1)
