from django.db import models
from django.contrib.auth.models import User
import markdown2

class Mail(models.Model):
    email = models.EmailField(max_length=50)

    def is_user_mail(self):
        try:
            User.objects.get(email=self.email)
            return True
        except User.DoesNotExist:
            return False
    def __str__(self):
        return self.email


class Test(models.Model):
    test = models.CharField(max_length=50)

    def __str__(self):
        return self.test


class Message(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    html_message = models.TextField(max_length=1500, blank=True, null=True)

    class Meta:
        ordering = ['-pk']

    def save(self, *args, **kwargs):
        markdown_message = markdown2.markdown(self.message)
        self.html_message = markdown_message
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject