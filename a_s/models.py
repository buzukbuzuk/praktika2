from django.db import models

class AutoSys(models.Model):
    id = models.AutoField(primary_key=True)
    autosys = models.IntegerField(null=False, unique=True)

    def __str__(self):
        return f'{self.id} {self.autosys}'
