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
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    pass  # Logic for processing data goes here

def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    pass  # Printing outcomes to the console


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

    file_name = f"traffic_data{date_dd:02}{date_MM:02}{date_YYYY}.csv"
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No file found. Please check the date and try again.")            
    
    user_choice = validate_continue_input()
    if user_choice == "N":
        print("Exiting the program.")
        break