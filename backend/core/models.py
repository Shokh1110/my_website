from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Taom nomi")
    price = models.IntegerField(verbose_name="Narx (so'm)")
    category = models.CharField(max_length=50, choices=[
        ('osh', 'Osh'),
        ('salat', 'Salat'),
        ('ichimlik', 'Ichimlik')
    ])
    image = models.ImageField(upload_to="menu/", blank=True)

    def __str__(self):
        return f"{self.name} - {self.price} so'm"