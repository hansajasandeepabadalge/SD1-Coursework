#Author: Hansaja Sandeepa
#Date: 11/27/2024
#Student ID: 20244017

# Task A: Input Validation
def validate_date_input(message, start_range, end_range):
    while True:
        try:
            date = int(input(message))
        except ValueError:
            print("Integer required")
            continue
        else:
            if date is not None and start_range <= date <= end_range:
                break
            else:
                print(f"Out of range - values must be in the range {start_range} and {end_range}")
                continue
    return date

def validate_continue_input():
    while True:
        user_input = input("Do you want to load another dataset? (Y/N): ")
        if user_input in ["Y","N"]:
            return user_input
        else:
            print("Invalid input. Please enter Y or N")

# Task B: Processed Outcomes
def process_csv_data(file_path):
    lines_in_csv = 0
    total_vehicles = 0
    total_trucks = 0
    total_electric_vehicles = 0
    two_wheeled_vehicles = 0
    total_busses_north_elm_rabit = 0
    both_junctions_without_turning_left_or_right = 0
    percentage_of_all_vehicles_recorded_that_are_trucks = 0
    average_number_bicycles_per_hour = 0
    total_number_of_vehicles_recorded_as_over_the_speed = 0
    total_number_of_vehicles_elm_avenue_rabbit_road = 0
    total_number_of_vehicles_hanley_highway_westway = 0
    percentage_of_scooters_through_elm_avenue_rabbit = 0

    total_number_of_bicycle = 0
    total_number_of_scooters_elm = 0

    hours = []
    hours_for_rains = []

    with open(file_path, "r") as file:
        for lines in file:
            JunctionName = lines.split(",")[0]
            Date = lines.split(",")[1]
            timeOfDay = lines.split(",")[2]
            travel_Direction_in = lines.split(",")[3]
            travel_Direction_out = lines.split(",")[4]
            Weather_Conditions = lines.split(",")[5]
            JunctionSpeedLimit = lines.split(",")[6]
            VehicleSpeed = lines.split(",")[7]
            VehicleType = lines.split(",")[8]
            elctricHybrid = lines.split(",")[9].strip().upper()

            lines_in_csv += 1

            if lines_in_csv == 1:
                continue
            else:
                total_vehicles += 1
                if VehicleType == "Truck":
                    total_trucks += 1
                if elctricHybrid == "TRUE":
                    total_electric_vehicles += 1
                if VehicleType == "Bicycle" or VehicleType == "Scooter" or VehicleType == "Motorcycle":
                    two_wheeled_vehicles += 1
                if JunctionName == "Elm Avenue/Rabbit Road"  and travel_Direction_out == "N" and VehicleType == "Buss":
                    total_busses_north_elm_rabit += 1
                if travel_Direction_in == travel_Direction_out:
                    both_junctions_without_turning_left_or_right += 1
                if VehicleType == "Bicycle":
                    total_number_of_bicycle += 1
                if int(JunctionSpeedLimit) < int(VehicleSpeed):
                    total_number_of_vehicles_recorded_as_over_the_speed += 1
                if JunctionName == "Elm Avenue/Rabbit Road":
                    total_number_of_vehicles_elm_avenue_rabbit_road += 1
                if JunctionName == "Hanley Highway/Westway":
                    total_number_of_vehicles_hanley_highway_westway += 1
                    hour = timeOfDay.split(":")[0]
                    hours.append(hour)
                if VehicleType == "Scooter" and JunctionName == "Elm Avenue/Rabbit Road":
                    total_number_of_scooters_elm += 1
                if Weather_Conditions == "Light Rain" or Weather_Conditions == "Heavy Rain":
                    hour_of_rain = timeOfDay.split(":")[0]
                    hours_for_rains.append(hour_of_rain)

    hour_counts = {}
    hour_of_rain_counts = {}

    for hour in hours:
        if hour not in hour_counts:
            hour_counts[hour] = 0
        hour_counts[hour] += 1
    
    for hour_of_rain in hours_for_rains:
        if hour_of_rain not in hour_of_rain_counts:
            hour_of_rain_counts[hour_of_rain] = 0
        hour_of_rain_counts[hour_of_rain] +=1
    
    hour_count = list(hour_counts.values())
    hour_of_rain_count = list(hour_of_rain_counts.keys())

    most_common_hours = {}

    for key, value in hour_counts.items():
        if value == max(hour_count):
            most_common_hours[key]=value
    
    
    percentage_of_all_vehicles_recorded_that_are_trucks = round((total_trucks/total_vehicles)*100)
    average_number_bicycles_per_hour = round(total_number_of_bicycle/24)
    percentage_of_scooters_through_elm_avenue_rabbit = round((total_number_of_scooters_elm/total_number_of_vehicles_elm_avenue_rabbit_road)*100)
    
    print(total_vehicles)
    print(total_trucks)
    print(total_electric_vehicles)
    print(two_wheeled_vehicles)
    print(total_busses_north_elm_rabit)
    print(both_junctions_without_turning_left_or_right)
    print(f"{percentage_of_all_vehicles_recorded_that_are_trucks}%")
    print(average_number_bicycles_per_hour)
    print(total_number_of_vehicles_recorded_as_over_the_speed)
    print(total_number_of_vehicles_elm_avenue_rabbit_road)
    print(total_number_of_vehicles_hanley_highway_westway)
    print(f"{percentage_of_scooters_through_elm_avenue_rabbit}%")
    print(max(hour_count))
    for key, value in most_common_hours.items():
        print(f"{key}:00 between {int(key)+1}:00")
    print(f"{len(hour_of_rain_count)}h")
    return total_vehicles, total_trucks, total_electric_vehicles, two_wheeled_vehicles, total_busses_north_elm_rabit, both_junctions_without_turning_left_or_right, percentage_of_all_vehicles_recorded_that_are_trucks
    

def display_outcomes(outcomes):
    print(
f"""The total number of vehicles recorded for this date i
The total number of trucks recorded for this date is 109
The total number of electric vehicles for this date is 368
The total number of two-wheeled vehicles for this date is 401
The total number of Busses leaving Elm Avenue/Rabbit Road heading North is 15
The total number of Vehicles through both junctions not turning left or right is 363
The percentage of total vehicles recorded that are trucks for this date is 11% the average number of Bikes per hour for this date is 7
        
The total number of Vehicles recorded as over the speed limit for this date is 205
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is 494 The total number of vehicles recorded through Hanley Highway/Westway junction is 543
10% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.
        
The highest number of vehicles in an hour on Hanley Highway/Westway is 39
The most vehicles through Hanley Highway/Westway were recorded between 18:00 and 19:00
The number of hours of rain for this date is 0
    """)

# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    pass  # File writing logic goes here

# if you have been contracted to do this assignment please do not remove this line


while True:
    date_dd = validate_date_input("Please enter the day of the survey in the format dd: ", 1,31)
    date_MM = validate_date_input("Please enter the day of the survey in the format MM: ", 1,12)
    date_YYYY = validate_date_input("Please enter the day of the survey in the format YYYY: ", 2000,2024)
    """
    date_dd = 16
    date_MM = 6
    date_YYYY = 2024
    """

    file_name = f"traffic_data{date_dd:02}{date_MM:02}{date_YYYY}.csv"
    try:
        process_csv_data(file_name)
        pass
    except FileNotFoundError:
        print("No file found. Please check the date and try again.")            
    
    user_choice = validate_continue_input()
    if user_choice == "N":
        print("Exiting the program.")
        break
