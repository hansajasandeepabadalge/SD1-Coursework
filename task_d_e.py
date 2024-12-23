# Task D: Histogram Display
import tkinter as tk
import csv

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
            scaling_factor = (self.canvas_height - 2 * self.space_between) / max_frequency
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
        print("Previous data cleared.")

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        date_input = input("Please enter the date of the survey in the format DDMMYYYY: ").strip()
        if len(date_input) != 8 or not date_input.isdigit():
            print("Invalid format. Please use DDMMYYYY.")
            return None, None

        day, month, year = date_input[:2], date_input[2:4], date_input[4:]
        selected_date = f"{day}/{month}/{year}"

        file_path = f"traffic_data{date_input}.csv"
        print(f"Processing file: {file_path}")

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

            if not self.traffic_data:
                print(f"No data found for the selected date: {selected_date}")
                continue

            app = HistogramApp(self.traffic_data, selected_date)
            app.run()

            continue_prompt = input("Do you want to select another data file for a different date? Y/N: ").strip().lower()
            if continue_prompt == 'n':
                print("End of run.")
                break

if __name__ == "__main__":
    processor = MultiCSVProcessor()
    processor.process_files()
