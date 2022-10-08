"""gift related services goes here"""
from .models import Voucher, VoucherOption, SpecialGift


def get_vouchers(**kwargs):
    """return the voucher QS"""
    return Voucher.objects.filter(**kwargs)


def get_special_gift(**kwargs):
    """return the special gift QS"""
    return SpecialGift.objects.filter(**kwargs)


def get_voucher_options(**kwargs):
    """return the voucher options QS"""
    return VoucherOption.objects.filter(**kwargs)


def get_voucher_option_by_voucher_id(voucher_id):
    return get_voucher_options(voucher_id=voucher_id)
