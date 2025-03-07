from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager


class Subtask(models.Model):

    text = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    tel = PhoneNumberField(blank=True, null=True, region="DE") # Gestaltet sich das beim Serializer Schwierig?

    def __str__(self):
        return self.name


class Account(Contact, AbstractUser):

    username = None
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.name


class Task(models.Model):

    PRIO_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('Urgent', 'Urgent')
    ]

    title = models.CharField(max_length=60)
    worker = models.ManyToManyField("Contact", related_name="tasks")
    description = models.TextField()
    date = models.DateField()
    prio = models.CharField(max_length=10, choices=PRIO_CHOICES, default='medium')
    subtasks = models.ManyToManyField("Subtask", related_name="tasks")
    category = models.CharField(max_length=60)
    todo = models.BooleanField()
    progress = models.BooleanField()
    feedback = models.BooleanField()
    done = models.BooleanField()

    def __str__(self):
        return self.title