from django.core.exceptions import ValidationError


def validate_file_size(image_object):
    size = 5 * 1024 * 1024
    if image_object.size > size:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')
