from django.db import models

# Models for an MVP version of the project

class Email(models.Model):
    sender = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Task(models.Model):
    email = models.OneToOneField(Email, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description