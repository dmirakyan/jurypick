from django.db import models

# Create your models here.
class Query(models.Model):
    search_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip_code = models.IntegerField()
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    birth_date = models.CharField(max_length=128)
    def __str__(self):  
        return self.first_name

class Human(models.Model):
    search_id = models.OneToOneField(Query, on_delete=models.CASCADE)
    result = models.CharField(max_length=128)
    def __str__(self):  
        return self.search_id