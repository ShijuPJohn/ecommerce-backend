from rest_framework import serializers

from base.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
