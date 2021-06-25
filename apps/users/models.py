from django.db import models
from datetime import datetime


class User(models.Model):
    """Store user information."""
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    join_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'userinfo'
        verbose_name_plural = 'userinfo'
        ordering = ['join_time', 'name']


class EmailVerification(models.Model):
    """Send email-verification code."""
    code = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    send_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
    
    class Meta:
        verbose_name = 'emailcode'
        verbose_name_plural = 'emailcode'
