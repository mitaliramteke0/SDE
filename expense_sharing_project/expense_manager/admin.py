from django.contrib import admin
from .models import Expense, Balance

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'type', 'timestamp')
    list_filter = ('type', 'timestamp')
    search_fields = ('description',)

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user_1', 'user_2', 'amount', 'settled')
    list_filter = ('settled',)
