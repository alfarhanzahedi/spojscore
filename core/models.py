from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length = 80)
    code = models.CharField(max_length = 20)
    users = models.IntegerField()
    score = models.FloatField()

    def __str__(self):
        return self.code

