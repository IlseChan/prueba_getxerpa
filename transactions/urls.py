from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrichTransactionsAPIView, CategoryViewSet, MerchantViewSet, KeywordViewSet
from django.urls import path, include
from .views import EnrichTransactionsAPIView, TransactionListAPIView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('merchants', MerchantViewSet, basename='merchant')
router.register('keywords', KeywordViewSet, basename='keyword')

urlpatterns = [
    path('enrich/', EnrichTransactionsAPIView.as_view(), name='enrich-transactions'),
    path('transactions/', TransactionListAPIView.as_view(), name='list-transactions'),
    path('', include(router.urls)), 
]