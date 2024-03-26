from django.db import models

class Food_Truck(models.Model):
    '''
    Model representing a food truck.
    '''

    location_id = models.IntegerField(verbose_name='Location ID')
    applicant = models.CharField(max_length=255, verbose_name='Applicant')
    facility_type = models.CharField(max_length=255, verbose_name='Facility Type')
    cnn = models.IntegerField(verbose_name='Census Block Number')
    location_description = models.CharField(max_length=255, verbose_name='Location Description')
    address = models.CharField(max_length=255, verbose_name='Address')
    block_lot = models.CharField(max_length=255, verbose_name='Block and Lot')
    block = models.CharField(max_length=255, verbose_name='Block')
    lot = models.CharField(max_length=255, verbose_name='Lot')
    permit = models.CharField(max_length=255, null=True, blank=True, verbose_name='Permit')
    status = models.CharField(max_length=255, verbose_name='Status')
    food_items = models.CharField(max_length=255, verbose_name='Food Items')
    x = models.FloatField(verbose_name='X-coordinate')
    y = models.FloatField(verbose_name='Y-coordinate')
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    schedule = models.CharField(max_length=255, verbose_name='Schedule')
    days_hours = models.CharField(max_length=255, verbose_name='Days and Hours')
    approved = models.DateTimeField(null=True, blank=True, verbose_name='Date and Time of Approval')
    received = models.DateTimeField(null=True, blank=True, verbose_name='Date and Time of Receipt')
    prior_permit = models.IntegerField(null=True, blank=True, verbose_name='Prior Permit')
    expiration_date = models.DateField(null=True, blank=True, verbose_name='Expiration Date')
    fire_prevention_districts = models.IntegerField(verbose_name='Fire Prevention Districts')
    police_districts = models.IntegerField(verbose_name='Police Districts')
    supervisor_districts = models.IntegerField(verbose_name='Supervisor Districts')
    zip_codes = models.IntegerField(verbose_name='ZIP Codes')
    neighborhoods = models.CharField(max_length=255, verbose_name='Neighborhoods')

    def __str__(self):
        return self.applicant