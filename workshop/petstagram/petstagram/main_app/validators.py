from django.core.exceptions import ValidationError


def validate_file_size_5_MB(value):
    SIZE = 5
    limit = SIZE * 1024 * 1024
    if value.file.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')
