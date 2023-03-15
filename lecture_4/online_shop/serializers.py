from rest_framework import serializers
from online_shop.models import Category, Product

user = {
    'name': 'Name',
    'surname': 'Surname',
    'password': 'Test1234'
}


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_null=False, allow_blank=False, min_length=10, max_length=255)
    description = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self, validated_data): # POST
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data): # PUT
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_null=False, allow_blank=False)
    price = serializers.FloatField(allow_null=False)
    code = serializers.CharField(allow_null=False, allow_blank=False)
    category = CategorySerializer(required=False, read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.code = validated_data.get('code', instance.code)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance









