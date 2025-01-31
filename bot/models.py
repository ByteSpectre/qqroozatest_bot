from django.db import models

class Text(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

class User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    first_interaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User ID: {self.user_id}"
