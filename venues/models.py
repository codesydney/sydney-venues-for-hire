from django.db import models

class Venue(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    objectid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    streetnumber = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    streetextra = models.CharField(max_length=50, blank=True, null=True)
    suburb = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)

    class Meta:
        db_table = 'venues_for_hire'  # Match the table name in your SQLite database

    def __str__(self):
        return self.name