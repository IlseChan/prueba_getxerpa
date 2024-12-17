from rest_framework import serializers
from .models import Transaction, Category, Merchant, Keyword

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

    def validate(self, data):
        if Keyword.objects.filter(keyword=data['keyword'], merchant=data['merchant']).exists():
            raise serializers.ValidationError("Este keyword ya existe para el merchant proporcionado.")
        return data

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
