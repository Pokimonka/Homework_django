from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=150)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now = True)