from django.db import models

# Create your models here.
class SaveFile(models.Model):
    user_id = models.IntegerField()
    pickle = models.CharField(max_length=2000)
