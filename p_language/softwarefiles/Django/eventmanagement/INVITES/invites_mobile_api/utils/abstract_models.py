"""register abstract model here"""
from django.db import models


class AbstractDateTimeModel(models.Model):
    """abstract date time model """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractActivatorModel(models.Model):
    """activator model to activation"""
    DEFAULT_ACTIVATION = True
    is_active = models.BooleanField(default=DEFAULT_ACTIVATION)

    class Meta:
        abstract = True


class AbstractTitleModel(models.Model):
    """abstract title/name model"""
    TITLE_LENGTH = 30
    title = models.CharField(max_length=TITLE_LENGTH, verbose_name="title or name")

    class Meta:
        abstract = True


class AbstractTitleAndActivatorModel(AbstractTitleModel, AbstractActivatorModel):
    """abstract activator model and title model"""

    class Meta:
        abstract = True
