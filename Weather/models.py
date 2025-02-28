from django.db import models

class WeatherRequest(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    humidity = models.FloatField()
    cloud_coverage = models.FloatField()
    rain = models.FloatField(default=0)

    def __str__(self):
        return f"Weather for {self.city} on {self.timestamp}"
