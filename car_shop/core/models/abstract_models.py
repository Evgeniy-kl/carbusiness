from datetime import datetime

from django.db import models


class IsActive(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True, blank=True)


class CreatedAt(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateField(default=datetime.now(), blank=True)


class UpdatedAt(models.Model):
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(default=datetime.now(), blank=True)
