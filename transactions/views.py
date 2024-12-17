from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction, Keyword, Category
from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from .models import Category, Merchant, Keyword
from .serializers import CategorySerializer, MerchantSerializer, KeywordSerializer
from rest_framework.generics import ListAPIView
from .models import Transaction
from .serializers import TransactionSerializer

class EnrichTransactionsAPIView(APIView):
    def post(self, request):
        transactions_data = request.data.get('transactions', [])
        enriched_transactions = []
        uncategorized_transactions = []

        for tx in transactions_data:
            description = tx.get('description', '').lower()
            amount = tx.get('amount')
            date = datetime.strptime(tx.get('date'), "%Y-%m-%d").date()
            keyword_entry = Keyword.objects.filter(keyword__icontains=description).first()
            merchant = keyword_entry.merchant if keyword_entry else None
            category = merchant.category if merchant else None

            if not category:
                category_type = 'expense' if amount < 0 else 'income'
                category = Category.objects.filter(type=category_type).first()

            if not merchant or not category:
                uncategorized_transactions.append(tx)

            enriched_transactions.append({
                "id": tx.get('id'),
                "description": tx.get('description'),
                "amount": amount,
                "date": str(date),
                "merchant": merchant.merchant_name if merchant else None,
                "category": category.name if category else None
            })

        return Response({
            "enriched_transactions": enriched_transactions,
            "uncategorized_transactions": uncategorized_transactions, 
            "metrics": {
                "total_transactions": len(transactions_data),
                "categorized_rate": sum(1 for t in enriched_transactions if t['category']) / len(transactions_data),
                "merchant_identified_rate": sum(1 for t in enriched_transactions if t['merchant']) / len(transactions_data),
            }
        })

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'  

class MerchantViewSet(ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class KeywordViewSet(ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class TransactionListAPIView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer