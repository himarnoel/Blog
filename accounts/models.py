from django.db import models
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.

class CustomerManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields ):
        pass
    def create_superuser(self,email, password, **extra_fields):
        pass

