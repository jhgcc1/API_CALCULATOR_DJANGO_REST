from django.db import models

# Create your models here.
class Cal(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.IntegerField()
    var1 = models.IntegerField()
    var2 = models.IntegerField()
    def __str__(self):
        return str(self.id)
