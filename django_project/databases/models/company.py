from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=150, null=False, unique=True)
    name = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "companies"