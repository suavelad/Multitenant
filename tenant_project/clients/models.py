from django.db import models

# Create your models here.
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True,blank=True)
    on_trial = models.BooleanField(null=True,blank=True)
    created_on = models.DateField(auto_now_add=True)

class Domain(DomainMixin):
    pass

class Admin(models.Model):
    firstname=models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
