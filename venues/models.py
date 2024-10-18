from django.db import models

class VenuesForHire(models.Model):
    x = models.FloatField(db_column='X')  # Field name made lowercase.
    y = models.FloatField(db_column='Y')  # Field name made lowercase.
    objectid = models.IntegerField(db_column='OBJECTID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    streetnumber = models.TextField(db_column='Streetnumber')  # Field name made lowercase.
    street = models.TextField(db_column='Street')  # Field name made lowercase.
    streetextra = models.TextField(db_column='Streetextra', blank=True, null=True)  # Field name made lowercase.
    suburb = models.TextField(db_column='Suburb')  # Field name made lowercase.
    postcode = models.IntegerField(db_column='Postcode')  # Field name made lowercase.

    class Meta:
        db_table = 'venues_for_hire'
