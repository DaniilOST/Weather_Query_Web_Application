from django.db import models

class WeatherRequest(models.Model):
    city = models.CharField(max_length=100)  # Название города
    timestamp = models.DateTimeField(auto_now_add=True)  # Временная метка запроса
    temperature = models.FloatField()  # Температура в Цельсиях
    wind_speed = models.FloatField()  # Скорость ветра
    humidity = models.FloatField()  # Влажность
    cloud_coverage = models.FloatField()  # Облачность
    rain = models.FloatField(default=0)  # Дождь (если есть, иначе 0)

    def __str__(self):
        return f"Weather for {self.city} on {self.timestamp}"
