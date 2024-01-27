from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
from django.conf import settings

from django.core.mail import send_mail

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(models.Model):   
    name     = models.CharField(max_length=255)
    email    = models.EmailField(unique=True)
    phone    = models.CharField(max_length=15, unique=True)
    age      = models.PositiveIntegerField()
    college  = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    otp = models.IntegerField(null=True)
    participation = models.BooleanField(default=False)
    participated_event = models.CharField(max_length=50,null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'age', 'college']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.otp = random.randint(1000, 9999)
            subject = 'Verify your email'
            message = f'Your OTP is: {self.otp}'
            from_email = settings.EMAIL_HOST_USER
            to_email = self.email
            send_mail(subject, message, from_email, [to_email])

        super(User, self).save(*args, **kwargs)


class College(models.Model):
    title = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
class Games(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images',null=True)
    
    
    def __str__(self):
        return self.title
    
class SubEvents(models.Model):
    title = models.CharField(max_length=500)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True)
    rules = models.TextField(null=True)
    participants = models.ManyToManyField(User, related_name="events_participated",blank=True)
    def __str__(self):
        return self.title
    
class MainEvent(models.Model):
    title = models.CharField(max_length=500,null=True)
    image = models.ImageField(upload_to='main_event_images',null=True)
    sub_events = models.ManyToManyField(SubEvents,related_name="sub_events")
    def __str__(self):
        return self.title
    
