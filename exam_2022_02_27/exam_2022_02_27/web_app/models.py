from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 2
    MIN_AGE = 0
    REGEX_PATTERN = '^[a-zA-Z0-9_]*$'
    ERROR_MESSAGE = "Ensure this value contains only letters, numbers, and underscore."

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_USERNAME),
            RegexValidator(regex=REGEX_PATTERN,
                           message=ERROR_MESSAGE),
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE),
        ),
    )


class Album(models.Model):

    MAX_LENGTH_ALBUM_NAME = 30
    MAX_LENGTH_ARTIST_NAME = 30
    MAX_LENGTH_GENRE = 30
    MIN_PRICE = 0

    UPLOAD_TO_DIR = 'profiles/'

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    R_AND_B_MUSIC = 'R&B Music'
    ROCK = 'Rock'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'
    CHOICES = [(x, x) for x in [
        POP_MUSIC, JAZZ_MUSIC, R_AND_B_MUSIC, ROCK, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER]]

    album_name = models.CharField(
        max_length=MAX_LENGTH_ALBUM_NAME,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_LENGTH_ARTIST_NAME,
    )

    genre = models.CharField(
        # max_length=max(len(x) for _, x in CHOICES,
        max_length=MAX_LENGTH_GENRE,
        choices=CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()
    # image_url = models.ImageField(
    #     upload_to=UPLOAD_TO_DIR
    # )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
    )

    @property
    def formatted_price(self):
        return f"{self.price:.2f}"




