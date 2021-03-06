import os
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify


class Theme(models.Model):

    theme_name = models.CharField(max_length=500)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=500,
    )

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.slug
        }
        return reverse('city-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.theme_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:

        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')

    def __str__(self):
        return self.theme_name


class IdealMonth(models.Model):

    month_name = models.CharField(max_length=20)
    month_number = models.IntegerField()

    def __str__(self):
        return self.month_name

class Activities(models.Model):

    activity_name = models.CharField(max_length=500)

    def __str__(self):
        return self.activity_name

class City(models.Model):

    def city_pic_path(self, filename):

        if filename != 'nophoto.jpg':
            basefilename, file_extension = os.path.splitext(filename)
            randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'city_pics/{city_id}/{basename}_{randomstring}{ext}'.format(
                city_id=self.city_id, basename=basefilename, randomstring=randomstr,
                ext=file_extension)

    region_choices = [
        ('North India', 'North India'),
        ('South India', 'South India'),
        ('East India', 'East India'),
        ('West India', 'West India'),
        ('Central India', 'Central India'),
        ('North-East', 'North-East'),
        ('International', 'International')
    ]

    id = None
    city_id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=500)
    # places_to_visit
    state = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    weather = models.CharField(max_length=500)
    ideal_month = models.ManyToManyField(IdealMonth)
    ideal_duration = models.IntegerField()
    nearest_airport = models.CharField(max_length=500)
    # upcoming_events
    about = models.TextField()
    city_pic = models.ImageField(default='nophoto.jpg',
                                 upload_to=city_pic_path)
    # more_on_city
    # articles
    # reviews
    # photos
    # videos
    # how_to_reach
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=500,
    )
    themes = models.ManyToManyField(Theme)
    region = models.CharField(max_length=500, choices=region_choices)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.city_id,
            'slug': self.slug
        }
        return reverse('city-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.city_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:

        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
        return self.city_name



class Place(models.Model):

    def place_pic_path(self, filename):

        if filename != 'nophoto.jpg':
            basefilename, file_extension = os.path.splitext(filename)
            randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'city_pics/{place_id}/{basename}_{randomstring}{ext}'.format(
                place_id=self.place_id, basename=basefilename, randomstring=randomstr,
                ext=file_extension)

    id = None
    place_id = models.BigAutoField(primary_key=True)
    places = models.CharField(max_length=500)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    description = models.TextField()
    # themes = models.TextField()
    themes = models.ManyToManyField(Theme)
    # faqs
    weather = models.CharField(max_length=500)
    time_required = models.CharField(max_length=500)
    timings = models.CharField(max_length=500)
    entry_fee = models.CharField(max_length=500)
    place_pic = models.ImageField(default='nophoto.jpg',
                                 upload_to=place_pic_path)
    # reviews
    tripupp_opinion = models.TextField()
    # food
    # photos
    # videos
    map = models.TextField()
    # how_to_reach
    # articles

    slug = models.SlugField(
        default='',
        editable=False,
        max_length=500,
    )

    activities = models.ManyToManyField(Activities)
    
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('place-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.places
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:

        verbose_name = _('place')
        verbose_name_plural = _('places')

    def __str__(self):
        return self.places
