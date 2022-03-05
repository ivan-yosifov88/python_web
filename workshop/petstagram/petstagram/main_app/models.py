import datetime

from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.main_app.validators import validate_file_size_5_MB


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = "Female"
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x, x) for x in [MALE, FEMALE, DO_NOT_SHOW]]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ),
    )

    profile_picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for (x, _) in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    @property
    def name(self):
        full_name = self.first_name + " " + self.last_name if self.last_name else self.first_name
        return full_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    PET_TYPE = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    pet_type = models.CharField(
        max_length=max(len(x) for (x, _) in PET_TYPE),
        choices=PET_TYPE,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user_profile', 'name')

    def __str__(self):
        return f"{self.name} the {self.pet_type}"


class PetPhoto(models.Model):
    MAX_PHOTO_SIZE_MB = 5

    photo = models.ImageField()

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    datetime_of_creation = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return f"{self.photo}"