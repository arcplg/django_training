from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from apps.company.models import Company
from django.contrib.auth.hashers import check_password

class AdminAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, group_name=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) and user.groups.filter(name=group_name).exists():
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class CompanyAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, group_name=None, **kwargs):
        try:
            company = Company.objects.get(email=email)
            print(company.user)
            if check_password(password, company.password):  # Ensure password is hashed
                #  and company.user.groups.filter(name='CONTRACTOR').exists()
                print(company.user.groups.filter(name='CONTRACTOR'))
                if company.user is not None and company.user.groups.filter(name=group_name).exists():
                    return company.user
            return None
        except Company.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            company = Company.objects.get(pk=user_id)
            return company.user
        except Company.DoesNotExist:
            return None