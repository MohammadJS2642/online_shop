from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor


class UsersModels(models.Model):
    users_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    username = models.CharField(unique=True, max_length=1000)
    birthdate = models.DateTimeField()
    phoneNumber = models.IntegerField()
    userSignUpDate = models.DateField(auto_created=True)
    email = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.first_name
