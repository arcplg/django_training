from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=150, null=False, unique=True)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=255, null=False)
    last_login = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2_sha256$"):  # Prevent double hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "companies"

    # def __str__(self):
    #     return self.email
    