from .models import Food_Truck
from django.http import JsonResponse
from .serializers import Food_Truck_serialzer
from rest_framework.decorators import api_view
from .utils import Algorithm

'''
    Endpoint to get the nearst food trucks 
    
    To get all food trucks with the get request use http://127.0.0.1:8000/foodtrucks/

    To get the nearst food trucks with the post request use http://127.0.0.1:8000/foodtrucks/ 
        payload = {
        "origin_latitude" : "xxx.xxxxx",
        "origin_longtiude" : "xxx.xxxxx"
        }

'''
@api_view(['POST', 'GET'])
def get_all_food_truck(request):

    # Getting all the food trucks from database
    food_trucks = Food_Truck.objects.all()
    food_serializer = Food_Truck_serialzer(food_trucks, many = True)

    # Return all food trucks if the request is a get request
    if request.method == 'GET':
        return JsonResponse({"data" : food_serializer.data})
    
    # Accept the data that comes through the request object
    origin_latitude, origin_longtiude = float(request.data['origin_latitude']), float(request.data['origin_longtiude']) 
    nearest_food_trucks = []
    

    # Iterate through the food trucks and calculate the distance using haversine_distance_equation algorithim
    for food_truck in food_serializer.data:

        destination_latitude, destination_longtiude = food_truck['latitude'], food_truck['longitude']
        distance = Algorithm.haversine_distance_equation(origin_latitude, origin_longtiude, destination_latitude, destination_longtiude )
        distance = float(str(distance).split('e')[0])
        nearest_food_trucks.append((distance, food_truck))

    # Sort the food trucks based on the distance in ascending order
    nearest_food_trucks.sort(key=lambda x: float(x[0]) - 0)

    result = []
    # Modify the response data format
    for i in range(5):
        result.append({"distance" : nearest_food_trucks[i][0], "food_truck" : nearest_food_trucks[i][1]})

    return JsonResponse({"data" : result })