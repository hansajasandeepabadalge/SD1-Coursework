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


def count_timestamps_by_hour(file_path):
    timestamps = {}

    with open(file_path, "r") as file:
        for lines in file:
            date = lines.split(",")[2]
            timestamps.append(date)

    hour_counts = {}

    for time in timestamps:
        hour = time.split(":")[0]
        if hour not in hour_counts:
            hour_counts[hour] = 0
        hour_counts[hour] += 1

    for hour, count in sorted(hour_counts.items()):
        print(f"Hour {hour}: {count}")

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

    with open(file_path, "r") as file:
        number_of_vehicles_in_hours = []
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
                    hours_in_csv = timeOfDay.split(":")[0]
                    count_hours = 0
                    for hours in range(1,25):
                        if hours == int(hours_in_csv):
                            count_hours += 1
                        

                if VehicleType == "Scooter" and JunctionName == "Elm Avenue/Rabbit Road":
                    total_number_of_scooters_elm += 1
                
    
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
    print(number_of_vehicles_in_hours)

def display_outcomes(outcomes):
    pass  # Printing outcomes to the console
display_outcomes(outcomes="hi")

# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    pass  # File writing logic goes here

# if you have been contracted to do this assignment please do not remove this line


while True:
    """
    date_dd = validate_date_input("Please enter the day of the survey in the format dd: ", 1,31)
    date_MM = validate_date_input("Please enter the day of the survey in the format MM: ", 1,12)
    date_YYYY = validate_date_input("Please enter the day of the survey in the format YYYY: ", 2000,2024)
    """
    date_dd = 15
    date_MM = 6
    date_YYYY = 2024

    file_name = f"traffic_data{date_dd:02}{date_MM:02}{date_YYYY}.csv"
    try:
        process_csv_data(file_name)
    except FileNotFoundError:
        print("No file found. Please check the date and try again.")            
    
    user_choice = validate_continue_input()
    if user_choice == "N":
        print("Exiting the program.")
        break
