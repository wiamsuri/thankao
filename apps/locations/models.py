from django.db import models
from stdimage.models import StdImageField

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=120)
    country = models.ForeignKey(Country)

    meta_title = models.CharField(max_length=150)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=100)

    ordering = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)
    image = StdImageField(null=True, blank=True,
                          upload_to='images', variations={
                              'large': (1440, 300, True),
                              'normal': (900, 600, True),
                              'thumbnail': (150, 100, True)
                          })

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
