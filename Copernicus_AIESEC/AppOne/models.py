from django.db import models

# Create your models here.
class Local_Comittee(models.Model):
    lc_name = models.CharField(max_length = 64, unique=True)
