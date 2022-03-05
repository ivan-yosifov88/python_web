from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_file_size_5_MB(value):
    SIZE = 5
    limit = SIZE * 1024 * 1024
    if value.file.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must be greater than {self.min_date}')