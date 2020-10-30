from django.db import models

# Create your models here.
class Query(models.Model):
    search_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=128, null=True)
    middle_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    address = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=128, null=True)
    zip_code = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=128, null=True)
    birth_date = models.CharField(max_length=128, null=True)
    def __str__(self):  
        return self.first_name + self.last_name

class Human(models.Model):
    search_id = models.OneToOneField(Query, on_delete=models.CASCADE)
    result = models.CharField(max_length=128)
    def __str__(self):  
        return self.search_id