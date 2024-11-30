date_dd = 15
date_MM = 7
date_YYYY = 2024


def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
    file_name = f"traffic_data{date_dd:02}{date_MM:02}{date_YYYY}.csv"
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
            
    except FileNotFoundError:
        print("No file found. Please check the date and try again.")            
    

validate_continue_input()