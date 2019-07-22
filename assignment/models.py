from django.db import models


# Create your models here.
class Adult(models.Model):
    age = models.PositiveIntegerField(null=False, blank=False)
    work = models.CharField(max_length=20, null=False, blank=False)
    fnlwgt = models.PositiveIntegerField(null=False, blank=False)
    education = models.CharField(max_length=20, null=False, blank=False)
    education_num = models.PositiveIntegerField(null=False, blank=False)
    marital_status = models.CharField(max_length=30, null=False, blank=False)
    occupation = models.CharField(max_length=30, null=False, blank=False)
    relationship = models.CharField(max_length=20, null=False, blank=False)
    race = models.CharField(max_length=30, null=False, blank=False)

    SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    sex = models.CharField(max_length=10, choices=SEX_CHOICES,
                                    default='Male')
    capital_gain = models.PositiveIntegerField(default=0)
    capital_loss = models.PositiveIntegerField(default=0)
    hours_per_week = models.PositiveIntegerField(null=False, blank=False)
    native_country = models.CharField(max_length=50, null=False, blank=False)
    salary = models.CharField(max_length=10, null=False, blank=False)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)