from django.db import models

# Create your models here.
"""gift and voucher related models"""
from decimal import Decimal as D
from django.db import models
from utils.abstract_models import AbstractTitleAndActivatorModel


class Voucher(AbstractTitleAndActivatorModel):
    """voucher model"""
    image = models.ImageField(upload_to="gift/voucher", null=True, blank=True)

    def __str__(self):
        """represent the name"""
        return self.title


class VoucherOption(models.Model):
    """voucher related options"""
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE, related_name="options")
    amount = models.DecimalField(default=D(0.0), max_digits=9, decimal_places=2)

    def __str__(self):

        return f"{self.voucher}- {self.amount}"


class SpecialGift(AbstractTitleAndActivatorModel):
    """special gifts model"""

    def __str__(self):
        """model representation"""
        return self.title
