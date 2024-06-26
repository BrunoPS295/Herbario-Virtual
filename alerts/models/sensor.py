from django.db import models

from . import TypeSensor, Station
from .base import BaseModel


class Sensor(BaseModel):
    name = models.CharField(
        "Nome",
        max_length=100,
    )
    type = models.ForeignKey(
        TypeSensor, verbose_name="Tipo do sensor", on_delete=models.PROTECT
    )
    station = models.ForeignKey(
        Station, verbose_name="Estação", on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return f"{self.type} - {self.station}"

    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"
