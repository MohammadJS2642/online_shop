from django.db import models


class UsersModels(models.Model):
    users_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    birthdate = models.DateTimeField()
    phoneNumber = models.IntegerField()
    userSignUpDate = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return self.first_name
