"""helper functions"""
import base64
from hashlib import md5
from django.utils import timezone


def convert_base64_string(_str):
    """convert the base64 string """
    sample_string_bytes = _str.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    return base64_bytes.decode("ascii")


def generate_hash(encoded_string: str):
    """generate hash value for given string"""
    generated_hash = md5(encoded_string.encode())
    return generated_hash.hexdigest()


def generate_file_name(prefix_name):
    current_time_stm = timezone.now().strftime("%d-%m-%y_%H-%M-%S")
    file_name = f"{prefix_name}_{current_time_stm}"
    return file_name


def make_bank_hashing_string(params: dict):
    """will generate in order"""
    list_of_values = [str(each_values) for each_values in params.values()]
    return "|".join(list_of_values)
