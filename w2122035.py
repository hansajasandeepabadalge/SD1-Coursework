#Author: Badalge Hansaja Sandeepa
#Date: 11/27/2024
#Student ID: w2122035

# Task A: Input Validation
def validate_date_input(message, start_range, end_range, year=None, month=None): # Reference: Learn it from in Class Activities
    while True:
        try:
            date = int(input(message))
        except ValueError: # Value Error Hadling
            print("Integer required")
            continue
        else:
            if date is not None:  # hadling leap year and other months dates end date
                if year and month:
                    if month == 2:
                        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                            end_range = 29
                        else:
                            end_range = 28
                    elif month in [4, 6, 9, 11]:
                        end_range = 30
                if start_range <= date <= end_range: # Cheaking If the range is correct or not
                    break
                else:
                    print(f"Out of range - values must be in the range {start_range} and {end_range}") # out of range when input wrong range  
                    continue
    return date 


def validate_continue_input():
    while True: 
        user_input = input("Do you want to load another dataset? (Y/N): ")
        if user_input in ["Y","N"]: # Validate input (Reference: ChatGPT)
            return user_input
        else:
            print("Invalid input. Please enter Y or N")

# Task B: Processed Outcomes
def process_csv_data(file_path):
    # A dictionary to store various outcomes from the CSV data processing (Reference: https://www.w3schools.com/python/python_dictionaries.asp, ChatGPT)
    outcomes = {
        "lines_in_csv": 0,
        "total_vehicles": 0,
        "total_trucks": 0,
        "total_electric_vehicles": 0,
        "two_wheeled_vehicles": 0,
        "total_busses_north_elm_rabbit": 0,
        "both_junctions_no_turn": 0,
        "percentage_trucks": 0,
        "bicycles_per_hour": 0,
        "vehicles_over_speed": 0,
        "elm_avenue_vehicles": 0,
        "hanley_highway_vehicles": 0,
        "scooter_percentage_elm": 0,
        "total_bicycles": 0,
        "total_scooters_elm": 0,
        "hours": [],
        "hours_for_rains": [],
        "hours_of_rain_count": 0
    }

    with open(file_path, "r") as file:
        for lines in file:
            # split csv file in to fields
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

            outcomes["lines_in_csv"] += 1

            if outcomes["lines_in_csv"] == 1:
                continue # skip header line in csv
            else:
                outcomes["total_vehicles"] += 1  # addition total vehicle count
            
                if VehicleType == "Truck":
                    outcomes["total_trucks"] += 1  # addition truck count
            
                if elctricHybrid == "TRUE":
                    outcomes["total_electric_vehicles"] += 1  # addition electric vehicle count
            
                if VehicleType in ["Bicycle", "Scooter", "Motorcycle"]:
                    outcomes["two_wheeled_vehicles"] += 1  # addition two-wheeled vehicle count
            
                if JunctionName == "Elm Avenue/Rabbit Road" and travel_Direction_out == "N" and VehicleType == "Buss":
                    outcomes["total_busses_north_elm_rabbit"] += 1  # addition bus count for specific junction and direction
            
                if travel_Direction_in == travel_Direction_out:
                    outcomes["both_junctions_no_turn"] += 1  # addition count for vehicles not turning
            
                if VehicleType == "Bicycle":
                    outcomes["total_bicycles"] += 1  # addition bicycle count
            
                if int(JunctionSpeedLimit) < int(VehicleSpeed):
                    outcomes["vehicles_over_speed"] += 1  # addition count for vehicles over the speed limit
            
                if JunctionName == "Elm Avenue/Rabbit Road":
                    outcomes["elm_avenue_vehicles"] += 1  # addition vehicle count for Elm Avenue/Rabbit Road
            
                if JunctionName == "Hanley Highway/Westway":
                    outcomes["hanley_highway_vehicles"] += 1  # addition vehicle count for Hanley Highway/Westway
                    hour = timeOfDay.split(":")[0]  # Extract the hour from the time of day
                    outcomes["hours"].append(hour)
            
                if VehicleType == "Scooter" and JunctionName == "Elm Avenue/Rabbit Road":
                    outcomes["total_scooters_elm"] += 1  # addition scooter count for Elm Avenue/Rabbit Road
            
                if Weather_Conditions in ["Light Rain", "Heavy Rain"]:
                    hour_of_rain = timeOfDay.split(":")[0]  # Extract the hour from the time of day
                    outcomes["hours_for_rains"].append(hour_of_rain)  # Append the hour to the list of hours with rain

    hour_counts = {} # Count the number of vehicles per hour adding to a Dictionary
    hour_of_rain_counts = {} # Count the number of hours with rain to a Dictionary

    # Count the number of vehicles for each hour
    for hour in outcomes["hours"]:
        if hour not in hour_counts:
            hour_counts[hour] = 0
        hour_counts[hour] += 1
    
    # Count the number of hours with rain
    for hour_of_rain in outcomes["hours_for_rains"]:
        if hour_of_rain not in hour_of_rain_counts:
            hour_of_rain_counts[hour_of_rain] = 0
        hour_of_rain_counts[hour_of_rain] += 1
    
    # Convert the counts to lists
    hour_count = list(hour_counts.values())
    hour_of_rain_count = list(hour_of_rain_counts.keys())

    most_common_hours = {} # Dictionary to store the most common hours

    # Find the hours with the maximum number of vehicles
    for key, value in hour_counts.items(): # Reference: https://www.w3schools.com/python/python_for_loops.asp, ChatGPT
        if value == max(hour_count):
            most_common_hours[key] = value
    
    # Calculate the percentage of trucks out of the total vehicles
    outcomes["percentage_trucks"] = round((outcomes["total_trucks"] / outcomes["total_vehicles"]) * 100)
    
    # Calculate the average number of bicycles per hour
    outcomes["bicycles_per_hour"] = round(outcomes["total_bicycles"] / 24)
    
    # Calculate the percentage of scooters at Elm Avenue/Rabbit Road
    outcomes["scooter_percentage_elm"] = round((outcomes["total_scooters_elm"] / outcomes["elm_avenue_vehicles"]) * 100)
    
    # Count the number of hours with rain
    outcomes["hours_of_rain_count"] = len(hour_of_rain_count)
    
    return outcomes

def display_outcomes(outcomes):
    data =(
f"""The total number of vehicles recorded for this date is {outcomes["total_vehicles"]}
The total number of trucks recorded for this date is {outcomes["total_trucks"]}
The total number of electric vehicles for this date is {outcomes["total_electric_vehicles"]}
The total number of two-wheeled vehicles for this date is {outcomes["two_wheeled_vehicles"]}
The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {outcomes["total_busses_north_elm_rabbit"]}
The total number of Vehicles through both junctions not turning left or right is {outcomes["both_junctions_no_turn"]}
The percentage of total vehicles recorded that are trucks for this date is {outcomes["percentage_trucks"]}% 
The average number of Bikes per hour for this date is {outcomes["bicycles_per_hour"]}

The total number of Vehicles recorded as over the speed limit for this date is {outcomes["vehicles_over_speed"]}
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes["elm_avenue_vehicles"]}
The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes["hanley_highway_vehicles"]}
{outcomes["scooter_percentage_elm"]}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.

The highest number of vehicles in an hour on Hanley Highway/Westway is {max(outcomes["hours"].count(hour) for hour in outcomes["hours"])}
The most vehicles through Hanley Highway/Westway were recorded between {max(outcomes["hours"], key=outcomes["hours"].count)}:00 and {int(max(outcomes["hours"], key=outcomes["hours"].count)) + 1}:00
The number of hours of rain for this date is {outcomes["hours_of_rain_count"]}
    """)
    return data # Returning the data outcome to print on the shell and the text file

# Task C: Save Results to Text File
def save_results_to_file(outcomes, csv_file_name, file_name="results.txt"):
    with open(file_name, 'a') as file: # Open the file in append mode and write the "data" and CSV file name
        file.write(f"data file selected is {csv_file_name}\n")
        file.write(outcomes)
        file.write("\n***************************\n\n")
# if you have been contracted to do this assignment please do not remove this line


def main():
    while True:
        date_dd = validate_date_input("Please enter the day of the survey in the format dd: ", 1, 31)
        date_MM = validate_date_input("Please enter the day of the survey in the format MM: ", 1, 12)
        date_YYYY = validate_date_input("Please enter the year of the survey in the format YYYY: ", 2000, 2024)

        # Making the file name based on the validated date inputs
        file_name = f"traffic_data{date_dd:02}{date_MM:02}{date_YYYY}.csv"
        
        try:
            # Process the CSV data and get the outcomes
            outcomes = process_csv_data(file_name)
            
            # Display the selected file name and outcomes
            print("\n***************************")
            print(f"data file selected is {file_name}")
            print("***************************")
            print(display_outcomes(outcomes))
            
            # Save the outcomes to a text file
            save_results_to_file(display_outcomes(outcomes), file_name)
        
        # Handle file is not found
        except FileNotFoundError:
            print("No file found. Please check the date and try again.")
        
        # Handle permission error
        except PermissionError:
            print("Permission denied. Please check your file permissions and try again.")
        
        # Ask the user to load another dataset
        user_choice = validate_continue_input()
        if user_choice == "N":
            print("Exiting the program.")
            
            break

if __name__ == "__main__":
    main()
