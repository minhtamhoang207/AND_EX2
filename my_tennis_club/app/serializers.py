from rest_framework import serializers
from .model import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country # this is the model that is being serialized
        fields = ('country_name', 'local_currency')