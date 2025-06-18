from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Transaction, BudgetCategory, MarketData

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'salary', 'budget_goal', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Financial Information', {'fields': ('salary', 'budget_goal', 'data_sharing_enabled')}),
    )

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'amount', 'category', 'date', 'type')
    list_filter = ('type', 'category', 'date')
    search_fields = ('description', 'category')
    date_hierarchy = 'date'

class BudgetCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount', 'color')
    list_filter = ('user',)
    search_fields = ('name',)

class MarketDataAdmin(admin.ModelAdmin):
    list_display = ('nifty_current', 'sensex_current', 'inflation_current', 'updated_at')
    readonly_fields = ('updated_at',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(BudgetCategory, BudgetCategoryAdmin)
admin.site.register(MarketData, MarketDataAdmin)
