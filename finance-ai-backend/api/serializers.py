from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Transaction, BudgetCategory, MarketData

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'salary', 'budget_goal', 'data_sharing_enabled')
        read_only_fields = ('id',)

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'salary', 'budget_goal')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            salary=validated_data.get('salary'),
            budget_goal=validated_data.get('budget_goal')
        )
        return user

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'description', 'amount', 'category', 'date', 'type', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ('id', 'name', 'amount', 'color', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketData
        fields = '__all__'
        read_only_fields = ('id', 'updated_at') 