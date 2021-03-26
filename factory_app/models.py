from django.db import models


# Create your models here.

class Feet(models.Model):
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "feet"


class Leg(models.Model):
    feet = models.ForeignKey(Feet, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "leg"


class Table(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "table"

    def __str__(self):
        return self.name


class TableLeg(models.Model):
    leg = models.OneToOneField(Leg, on_delete=models.PROTECT, related_name="legs", null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="tables", null=True)

    class Meta:
        db_table = "tableleg"
