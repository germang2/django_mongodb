from djongo import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user.email
    