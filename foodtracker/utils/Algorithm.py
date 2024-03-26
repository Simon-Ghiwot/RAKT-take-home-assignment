from math import radians, cos, sin, asin, sqrt

EARTH_RADIUS = 6371


def haversine_distance_equation(origin_latitude, origin_longitude, destination_latitude, destination_longitude):
    """
    Calculates the haversine distance between two points on the Earth's surface.
    https://en.wikipedia.org/wiki/Haversine_formula
    
    Args:
        origin_latitude (float): Latitude of the origin point in degrees.
        origin_longitude (float): Longitude of the origin point in degrees.
        destination_latitude (float): Latitude of the destination point in degrees.
        destination_longitude (float): Longitude of the destination point in degrees.
    
    Returns:
        float: The haversine distance in kilometers between the origin and destination points.
    """
    # Convert input coordinates to radians
    origin_latitude, origin_longitude, destination_latitude, destination_longitude = map(radians, [origin_latitude, origin_longitude, destination_latitude, destination_longitude])

    # Calculate the differences in longitude and latitude
    distance_longitude = destination_longitude - origin_longitude
    distance_latitude = destination_latitude - origin_latitude

    # Apply the haversine formula
    a = sin(distance_latitude / 2) ** 2 + cos(origin_latitude) * cos(destination_latitude) * sin(distance_longitude / 2) ** 2
    c = 2 * asin(sqrt(a))
    kilometer = EARTH_RADIUS * c

    return kilometer