from django.db import models
from django.contrib.auth.models import User

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

    # username = models.CharField(max_length=128, null=True)

    created_at = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):  
        return str(self.search_id)

class Human(models.Model):
    search_id = models.OneToOneField(Query,to_field='search_id',primary_key=True, on_delete=models.CASCADE)
    # username = models.CharField(max_length=128, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    result = models.CharField(max_length=10000,null=True)
    result_clean = models.CharField(max_length=10000,null=True)
    result_clean_json = models.JSONField(null=True)
    response_status = models.CharField(max_length=10000,null=True)
    hidden = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    def __str__(self):  
        return self.search_id.first_name