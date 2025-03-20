from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, User

from JoinApp.models import Contact
from JoinBackend import settings

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):

    def create_user(self , email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, email):  
        return self.get(email=email)

class Account(Contact, AbstractUser):
    username = None  # Username entfernen, damit nur die E-Mail zählt
    # email = models.EmailField(unique=True)  # E-Mail als eindeutiges Login-Feld

    USERNAME_FIELD = 'email'  # E-Mail als Login-Feld
    REQUIRED_FIELDS = []  # Hier kannst du weitere Pflichtfelder definieren

    objects = AccountManager()  # Benutzerdefinierten Manager setzen

    def __str__(self):
        return self.email  # Gibt die E-Mail als Repräsentation zurück
