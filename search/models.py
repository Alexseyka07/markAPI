from django.db import models

# Create your models here.
class mark(models.Model):
    name = models.CharField(max_length=200)
    producer_country_name = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)


class model(models.Model):
    name = models.CharField(max_length=200)
    mark = models.ForeignKey(mark, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)


class path(models.Model):
    name = models.CharField(max_length=200)
    mark = models.ForeignKey(mark, on_delete=models.CASCADE)
    model = models.ForeignKey(model, on_delete=models.CASCADE)
    producer_country_name = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    
