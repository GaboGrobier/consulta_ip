from django.db import models


class ingresoIp(models.Model):
    ip = models.CharField(max_length = 16)
