from uuid import uuid4
from django.db import models

class Account(models.Model):
    password = models.CharField(max_length=4)
    user_id = models.PositiveIntegerField()
    
    number = models.CharField(max_length=36, unique=True, default=uuid4())
    money = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)