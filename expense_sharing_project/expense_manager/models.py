from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.CharField(max_length=10)  # 'EQUAL', 'EXACT', 'PERCENT'
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Balance(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owed_to')
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owed_by')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    settled = models.BooleanField(default=False)
