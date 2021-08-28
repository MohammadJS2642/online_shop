from django.db import models


class ProductsModels(models.Model):
    product_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_created=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title
