from django.db import models
from django.contrib.auth.models import User
import uuid
# from django.contrib.auth.models import User

# # Create your models here.
class Account(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False,
        default=uuid.uuid4
    )
    logged_in_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="logged_in_user")
    account_number = models.IntegerField(unique=True, blank=False, null=False)
    balance = models.DecimalField(decimal_places=2, max_digits=15)
