from django.db import models
from django.db.models import URLField
import datetime
from django.utils.timezone import now


# Create your models here.
class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFF = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(choices=CompanyStatus.choices, default=CompanyStatus.HIRING, max_length=30)
    last_update = models.DateField(default=datetime.date.today, editable=True)
    application_link = URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"
