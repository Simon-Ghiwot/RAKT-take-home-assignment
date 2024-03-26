import csv
from datetime import datetime
from foodtracker.models import Food_Truck

# Path to the CSV file
csv_file_path = 'food-truck-data.csv'

def import_food_truck_data():
    """
    Imports food truck data from a CSV file and creates Food_Truck instances in the database.
    """
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create a Food_Truck instance with data from each row in the CSV file
            food_truck_instance = Food_Truck(
                location_id = row['locationid'] if row['locationid'] else 0,
                applicant = row['Applicant'] if row['Applicant'] else "",
                facility_type = row['FacilityType'] if row['FacilityType'] else "",
                cnn = row['cnn'] if row['cnn'] else 0,
                location_description = row['LocationDescription'] if row['LocationDescription'] else 0,
                address = row['Address'] if row["Address"] else "",
                permit = row['permit'] if row['permit'] else "",
                block_lot = row['blocklot'] if row["blocklot"] else "",
                block = row['block'] if row['block'] else "",
                lot = row['lot'] if row['lot'] else "",
                status = row['Status'] if row["Status"] else "",
                food_items = row['FoodItems'] if row["FoodItems"] else "",
                x = row['X'] if row['X'] else 0,
                y = row['Y'] if row['Y'] else 0,
                latitude = row['Latitude'] if row["Latitude"] else 0,
                longitude = row['Longitude'] if row["Longitude"] else 0,
                schedule = row['Schedule'] if row["Schedule"] else "",
                days_hours = row['dayshours'] if row["dayshours"] else "",
                received = datetime.strptime(row['Received'], "%Y%m%d").strftime("%Y-%m-%d") if row["Received"] else "0000-00-00",
                prior_permit = row['PriorPermit'] if row["PriorPermit"] else 0,
                fire_prevention_districts = row['Fire Prevention Districts'] if row["Fire Prevention Districts"] else 0,
                police_districts = row['Police Districts'] if row["Police Districts"] else 0,
                supervisor_districts = row['Supervisor Districts'] if row["Supervisor Districts"] else 0,
                zip_codes = row['Zip Codes'] if row['Zip Codes'] else 0,
                neighborhoods = row['Neighborhoods (old)'] if row["Neighborhoods (old)"] else 0
            )
            food_truck_instance.save()
            print("Instance created:", food_truck_instance)

    print("Data import completed.")

# Call the function to import the data
import_food_truck_data()