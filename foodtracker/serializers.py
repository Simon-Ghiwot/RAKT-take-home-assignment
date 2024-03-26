from rest_framework import serializers
from .models import Food_Truck


class Food_Truck_serialzer(serializers.ModelSerializer):
    '''
        Serializer for the food truck model
    '''
    class Meta:
        model = Food_Truck
        fields = [ 'id', 'location_id', 'applicant', 'facility_type', 'cnn', 'location_description', 'address', 'block_lot', 'block','lot', 'permit',
                'status', 'food_items', 'x', 'y', 'latitude','longitude','schedule', 'days_hours', 'approved',
                'received', 'prior_permit', 'expiration_date', 'fire_prevention_districts','police_districts','supervisor_districts',
                'zip_codes', 'neighborhoods' ] 