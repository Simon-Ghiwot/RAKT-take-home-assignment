from django.db import models

class Food_Truck(models.Model):
    '''
    Model representing a food truck.
    '''

    location_id = models.IntegerField()
    # Unique ID of the food truck location

    applicant = models.CharField(max_length=255)
    # Name of the food truck applicant

    facility_type = models.CharField(max_length=255)
    # Type of facility the food truck operates in

    cnn = models.IntegerField()
    # Census Block Number of the food truck location

    location_description = models.CharField(max_length=255)
    # Description of the food truck's location

    address = models.CharField(max_length=255)
    # Address of the food truck

    block_lot = models.CharField(max_length=255)
    # Block and lot information of the food truck

    block = models.CharField(max_length=255)
    # Block information of the food truck

    lot = models.CharField(max_length=255)
    # Lot information of the food truck

    permit = models.CharField(max_length=255, null=True, blank=True)
    # Permit information of the food truck (nullable)

    status = models.CharField(max_length=255)
    # Status of the food truck

    food_items = models.CharField(max_length=255)
    # Food items offered by the food truck

    x = models.FloatField()
    # X-coordinate of the food truck location

    y = models.FloatField()
    # Y-coordinate of the food truck location

    latitude = models.FloatField()
    # Latitude of the food truck location

    longitude = models.FloatField()
    # Longitude of the food truck location

    schedule = models.CharField(max_length=255)
    # Schedule information of the food truck

    days_hours = models.CharField(max_length=255)
    # Days and hours of operation for the food truck

    approved = models.DateTimeField(null=True, blank=True)
    # Date and time of approval for the food truck (nullable)

    received = models.DateTimeField(null=True, blank=True)
    # Date and time of receiving application for the food truck (nullable)

    prior_permit = models.IntegerField(null=True, blank=True)
    # Prior permit information for the food truck (nullable)

    expiration_date = models.DateField(null=True, blank=True)
    # Expiration date of the food truck permit (nullable)

    fire_prevention_districts = models.IntegerField()
    # Fire prevention district associated with the food truck

    police_districts = models.IntegerField()
    # Police district associated with the food truck

    supervisor_districts = models.IntegerField()
    # Supervisor district associated with the food truck

    zip_codes = models.IntegerField()
    # ZIP code associated with the food truck

    neighborhoods = models.CharField(max_length=255)
    # Neighborhoods where the food truck operates