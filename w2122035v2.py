# Author: Hansaja Sandeepa
# Date: 11/27/2024
# Student ID: 20244017

# Task A: Input Validation
def validate_date_input(message, start_range, end_range):
    while True:
        try:
            date = int(input(message))
        except ValueError:
            print("Integer required")
            continue
        else:
            if start_range <= date <= end_range:
                return date
            else:
                print(f"Out of range - values must be in the range {start_range} and {end_range}")

def validate_continue_input():
    while True:
        user_input = input("Do you want to load another dataset? (Y/N): ").upper()
        if user_input in ["Y", "N"]:
            return user_input
        print("Invalid input. Please enter Y or N")

# Task B: Process CSV Data
def process_csv_data(file_path):
    outcomes = {
        "total_vehicles": 0,
        "total_trucks": 0,
        "total_electric_vehicles": 0,
        "two_wheeled_vehicles": 0,
        "total_busses_north_elm_rabbit": 0,
        "both_junctions_no_turn": 0,
        "vehicles_over_speed": 0,
        "elm_avenue_vehicles": 0,
        "hanley_highway_vehicles": 0,
        "bicycles_per_hour": 0,
        "scooter_percentage_elm": 0,
        "most_common_hour": None,
        "hours_of_rain": 0
    }

    vehicle_count = {"Bicycle": 0, "Scooter": 0, "Motorcycle": 0}
    hour_counts = {}
    rain_hours = set()

    try:
        with open(file_path, "r") as file:
            for i, line in enumerate(file):
                if i == 0:
                    continue
                data = line.strip().split(",")
                junction, date, time, dir_in, dir_out, weather, speed_limit, vehicle_speed, vehicle_type, electric_hybrid = data
                outcomes["total_vehicles"] += 1

                if vehicle_type == "Truck":
                    outcomes["total_trucks"] += 1
                if electric_hybrid.strip().upper() == "TRUE":
                    outcomes["total_electric_vehicles"] += 1
                if vehicle_type in vehicle_count:
                    outcomes["two_wheeled_vehicles"] += 1
                    vehicle_count[vehicle_type] += 1
                if junction == "Elm Avenue/Rabbit Road" and dir_out == "N" and vehicle_type == "Buss":
                    outcomes["total_busses_north_elm_rabbit"] += 1
                if dir_in == dir_out:
                    outcomes["both_junctions_no_turn"] += 1
                if int(vehicle_speed) > int(speed_limit):
                    outcomes["vehicles_over_speed"] += 1
                if junction == "Elm Avenue/Rabbit Road":
                    outcomes["elm_avenue_vehicles"] += 1
                if junction == "Hanley Highway/Westway":
                    outcomes["hanley_highway_vehicles"] += 1
                    hour = time.split(":")[0]
                    hour_counts[hour] = hour_counts.get(hour, 0) + 1
                if vehicle_type == "Scooter" and junction == "Elm Avenue/Rabbit Road":
                    vehicle_count["Scooter"] += 1
                if weather in ["Light Rain", "Heavy Rain"]:
                    rain_hours.add(time.split(":")[0])

        # Calculations
        outcomes["bicycles_per_hour"] = vehicle_count["Bicycle"] // 24
        if outcomes["elm_avenue_vehicles"]:
            outcomes["scooter_percentage_elm"] = (vehicle_count["Scooter"] * 100) // outcomes["elm_avenue_vehicles"]
        outcomes["most_common_hour"] = max(hour_counts, key=hour_counts.get, default=None)
        outcomes["hours_of_rain"] = len(rain_hours)

        display_outcomes(outcomes)

    except FileNotFoundError:
        print("No file found. Please check the date and try again.")

# Task C: Display Outcomes
def display_outcomes(outcomes):
    print(f"""
The total number of vehicles recorded for this date is {outcomes["total_vehicles"]}  
The total number of trucks recorded for this date is {outcomes["total_trucks"]} 
The total number of electric vehicles for this date is {outcomes["total_electric_vehicles"]} 
The total number of two-wheeled vehicles for this date is {outcomes["two_wheeled_vehicles"]} 
The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {outcomes["total_busses_north_elm_rabbit"]} 
The total number of Vehicles through both junctions not turning left or right is {outcomes["both_junctions_no_turn"]}  
The percentage of total vehicles recorded that are trucks for this date is {outcomes[""]}%
The average number of Bikes per hour for this date is {outcomes["bicycles_per_hour"]} 
 
The total number of Vehicles recorded as over the speed limit for this date is {outcomes["vehicles_over_speed"]}  
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes["elm_avenue_vehicles"]}
The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes["hanley_highway_vehicles"]}  
{outcomes["scooter_percentage_elm"]} of vehicles recorded through Elm Avenue/Rabbit Road are scooters. 
 
The highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes[""]} 
The most vehicles through Hanley Highway/Westway were recorded between 18:00 and 19:00  
The number of hours of rain for this date is {outcomes["hours_of_rain"]}
""")

# Main Program Loop
while True:
    date_dd = 15
    date_MM = 6
    date_YYYY = 2024

    file_name = f"traffic_data{date_dd:02}{date_MM:02}{date_YYYY}.csv"
    process_csv_data(file_name)
    if validate_continue_input() == "N":
        print("Exiting the program.")
        break
