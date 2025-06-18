from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'budget-categories', views.BudgetCategoryViewSet, basename='budget-category')
router.register(r'market-data', views.MarketDataViewSet, basename='market-data')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
] 