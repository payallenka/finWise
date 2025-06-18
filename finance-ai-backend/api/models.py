from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    budget_goal = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    data_sharing_enabled = models.BooleanField(default=True)

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']

class BudgetCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget_categories')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=20, default='bg-blue-500')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'name']

class MarketData(models.Model):
    nifty_current = models.DecimalField(max_digits=10, decimal_places=2)
    nifty_change = models.DecimalField(max_digits=10, decimal_places=2)
    nifty_change_percent = models.DecimalField(max_digits=5, decimal_places=2)
    sensex_current = models.DecimalField(max_digits=10, decimal_places=2)
    sensex_change = models.DecimalField(max_digits=10, decimal_places=2)
    sensex_change_percent = models.DecimalField(max_digits=5, decimal_places=2)
    inflation_current = models.DecimalField(max_digits=5, decimal_places=2)
    inflation_previous = models.DecimalField(max_digits=5, decimal_places=2)
    petrol_price = models.DecimalField(max_digits=8, decimal_places=2)
    diesel_price = models.DecimalField(max_digits=8, decimal_places=2)
    gold_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
