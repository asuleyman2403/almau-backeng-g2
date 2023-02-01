from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return 'ID: {}, name: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return 'ID: {}, name: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category.to_json()
        }

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

