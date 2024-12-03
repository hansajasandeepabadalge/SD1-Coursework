#Author: Hansaja Sandeepa
#Date: 11/27/2024
#Student ID: 20244017

# Task A: Input Validation
def validate_date_input(message, start_range, end_range):
    while True:
        try:
            date = int(input(message))
            if start_range <= date <= end_range:
                return date
            else:
                print(f"Out of range - values must be in the range {start_range} and {end_range}")
        except ValueError:
            print("Integer required")

def validate_continue_input():
    while True:
        user_input = input("Do you want to load another dataset? (Y/N): ")
        if user_input in ["Y", "N"]:
            return user_input
        else:
            print("Invalid input. Please enter Y or N")

# Task B: Processed Outcomes
def process_csv_data(file_path):
    stats = {
        "total_vehicles": 0,
        "total_trucks": 0,
        "total_electric_vehicles": 0,
        "two_wheeled_vehicles": 0,
        "total_busses_north_elm_rabit": 0,
        "both_junctions_without_turning_left_or_right": 0,
        "total_number_of_vehicles_recorded_as_over_the_speed": 0,
        "total_number_of_vehicles_elm_avenue_rabbit_road": 0,
        "total_number_of_vehicles_hanley_highway_westway": 0,
        "total_number_of_bicycle": 0,
        "total_number_of_scooters_elm": 0,
        "hours": []
    }

    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            data = line.strip().split(",")
            stats["total_vehicles"] += 1
            if data[8] == "Truck":
                stats["total_trucks"] += 1
            if data[9].strip().upper() == "TRUE":
                stats["total_electric_vehicles"] += 1
            if data[8] in ["Bicycle", "Scooter", "Motorcycle"]:
                stats["two_wheeled_vehicles"] += 1
            if data[0] == "Elm Avenue/Rabbit Road" and data[4] == "N" and data[8] == "Buss":
                stats["total_busses_north_elm_rabit"] += 1
            if data[3] == data[4]:
                stats["both_junctions_without_turning_left_or_right"] += 1
            if data[8] == "Bicycle":
                stats["total_number_of_bicycle"] += 1
            if int(data[6]) < int(data[7]):
                stats["total_number_of_vehicles_recorded_as_over_the_speed"] += 1
            if data[0] == "Elm Avenue/Rabbit Road":
                stats["total_number_of_vehicles_elm_avenue_rabbit_road"] += 1
            if data[0] == "Hanley Highway/Westway":
                stats["total_number_of_vehicles_hanley_highway_westway"] += 1
                stats["hours"].append(data[2].split(":")[0])
            if data[8] == "Scooter" and data[0] == "Elm Avenue/Rabbit Road":
                stats["total_number_of_scooters_elm"] += 1

    hour_counts = {hour: stats["hours"].count(hour) for hour in set(stats["hours"])}
    hour_count = list(hour_counts.values())

    print(stats["total_vehicles"])
    print(stats["total_trucks"])
    print(stats["total_electric_vehicles"])
    print(stats["two_wheeled_vehicles"])
    print(stats["total_busses_north_elm_rabit"])
    print(stats["both_junctions_without_turning_left_or_right"])
    print(f"{round((stats['total_trucks'] / stats['total_vehicles']) * 100)}%")
    print(round(stats["total_number_of_bicycle"] / 24))
    print(stats["total_number_of_vehicles_recorded_as_over_the_speed"])
    print(stats["total_number_of_vehicles_elm_avenue_rabbit_road"])
    print(stats["total_number_of_vehicles_hanley_highway_westway"])
    print(f"{round((stats['total_number_of_scooters_elm'] / stats['total_number_of_vehicles_elm_avenue_rabbit_road']) * 100)}%")
    print(max(hour_count))

def display_outcomes(outcomes):
    pass  # Printing outcomes to the console

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

    if validate_continue_input() == "N":
        print("Exiting the program.")
        break
