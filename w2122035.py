#Author: Badalge Hansaja Sandeepa
#Date: 12/23/2024
#Student ID: w2122035

import tkinter as tk
import csv

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

            # Open the histogram
            selected_date = f"{date_dd}/{date_MM:02}/{date_YYYY}"
            processor = MultiCSVProcessor()
            processor.load_csv_file(file_name, selected_date)
            app = HistogramApp(processor.traffic_data, selected_date)
            app.run()
        
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
        
    return date_dd, date_MM, date_YYYY, file_name


# Task D: Histogram Display
class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date
        self.root = tk.Tk()
        self.canvas = None  # Will hold the canvas for drawing

        self.canvas_width = 1200 # canvas width (Chnag)
        self.canvas_height = 600
        self.bar_width = 15
        self.space_between = 30

        self.setup_window()

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.root.title("Histogram")
        self.root.attributes('-topmost', True)  # Bring the window to the front
        self.root.update()
        self.root.attributes('-topmost', False) 
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="#edf2ee")
        self.canvas.pack()
        self.draw_histogram()
        self.add_legend()
        pass  # Setup logic for the window and canvas

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        elm_avenue_data = self.traffic_data.get("Elm Avenue/Rabbit Road", {}).values()
        hanley_highway_data = self.traffic_data.get("Hanley Highway/Westway", {}).values()

        max_elm_avenue = max(elm_avenue_data, default=0)
        max_hanley_highway = max(hanley_highway_data, default=0)

        max_frequency = max(max_elm_avenue, max_hanley_highway)

        if max_frequency > 0:
            scaling_factor = (self.canvas_height - 2 * self.space_between) / (2 * max_frequency)
        else:
            scaling_factor = 1

        # Title on the Canvas
        self.canvas.create_text(
            50,  # x-coordinate
            self.space_between, # Y-coordinate
            text = f"Histogram of Vehicle Frequency per Hour ({self.date})",
            font = ("Arial", 16),
            fill="#2b2b2b",
            anchor="nw" # Set the anchor to top-left corner
        )

        # Draw Bars and labels
        for i in range(24):
            hour = f"{i:02}:00"
            elm_avenue_frequency = self.traffic_data.get("Elm Avenue/Rabbit Road", {}).get(hour, 0)
            hanley_highway_frequency = self.traffic_data.get("Hanley Highway/Westway", {}).get(hour, 0)

            x0 = self.space_between + i * (self.bar_width * 3)
            x1 = x0 + self.bar_width
            x2 = x1 + self.bar_width

            # Elm Avenue bar
            elm_avennue_bar_top = self.canvas_height - self.space_between - (elm_avenue_frequency * scaling_factor)
            self.canvas.create_rectangle(
                x0, elm_avennue_bar_top,
                x1, self.canvas_height - self.space_between,
                fill = "#9af997"
            )

            # Add value on top of Elm Avenue bar
            self.canvas.create_text(
                (x0 + x1) // 2, elm_avennue_bar_top - 10,
                text = str(elm_avenue_frequency),
                font = ("Arial", 8),
                fill = "green"
            )

            # Hanley Highway bar
            hanley_highway_bar_top = self.canvas_height - self.space_between - (hanley_highway_frequency * scaling_factor)
            self.canvas.create_rectangle(
                x1, hanley_highway_bar_top,
                x2, self.canvas_height - self.space_between,
                fill = "#f69993"
            )

            # Add value on top of Hanley Highway bar
            self.canvas.create_text(
                (x1 + x2) // 2, hanley_highway_bar_top - 10,
                text = str(hanley_highway_frequency),
                font = ("Arial", 8),
                fill = "red"
            )

            # Hour label
            self.canvas.create_text(
                (x0 + x2) // 2, self.canvas_height - self.space_between + 10,
                text = hour,
                font = ("Arial", 8)
            )

        # Draw X axis
        self.canvas.create_line(
            self.space_between + 20, self.canvas_height - self.space_between,
            self.canvas_width - self.space_between-20, self.canvas_height - self.space_between,
            width = 2,
            fill = "#4c4c4c"
        )

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        # Legend for Elm Avenue/Rabbit Road
        self.canvas.create_rectangle(50, 60, 65, 75, fill="#9af997")
        self.canvas.create_text(70, 59, text="Elm Avenue/Rabbit Road", font=("Arial", 12), fill="#2b2b2b", anchor="nw")

        # Legend for Hanley Highway/Westway
        self.canvas.create_rectangle(50, 80, 65, 95, fill="#f69993")
        self.canvas.create_text(70, 79, text="Hanley Highway/Westway", font=("Arial", 12), fill="#2b2b2b", anchor="nw")

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.root.mainloop()


# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.traffic_data = {}
        self.current_data = None

    def load_csv_file(self, file_path, selected_date):
        """
        Loads a CSV file and processes its data.
        """
        try:
            with open(file_path, mode = "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Date"] == selected_date:
                        junction = row['JunctionName']
                        hour = row['timeOfDay'][:2] + ":00" # Extract hours

                        if junction not in self.traffic_data:
                            self.traffic_data[junction] = {}

                        if hour not in self.traffic_data[junction]:
                            self.traffic_data[junction][hour] = 0
                        
                        self.traffic_data[junction][hour] += 1
        except KeyError as e:
            print(f"Format issue: Missing column {e}")

    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        self.traffic_data.clear()

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        day, month, year, file_path = main()

        selected_date = f"{day}/{month:02}/{year}"

        return file_path, selected_date

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            self.clear_previous_data()
            file_path, selected_date = self.handle_user_interaction()

            if not file_path or not selected_date:
                continue

            self.load_csv_file(file_path, selected_date)

if __name__ == "__main__":
    main()