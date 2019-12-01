from djongo import models
from user.models import CustomUser

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    