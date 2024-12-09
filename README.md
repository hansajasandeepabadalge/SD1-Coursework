# Traffic Analysis Program

## Overview
This program analyzes traffic data collected from two road junctions (`Elm Avenue/Rabbit Road` and `Hanley Highway/Westway`). It allows council staff to:
- Analyze traffic data for a specific date (CSV file).
- View summarized results.
- Save results to a text file.
- Generate visualizations (histograms).

## Features
### 1. Input Validation
- Ensures users provide valid input for dates in `DD MM YYYY` format.
- Displays errors for:
  - Invalid data types (e.g., non-integer inputs).
  - Out-of-range inputs (e.g., day > 31, month > 12, year outside 2000-2024).
- Validates user decision to:
  - Load another dataset (`Y`).
  - Quit the program (`N`).

### 2. Data Analysis
The program computes:
- Total number of vehicles and specific categories (e.g., trucks, electric vehicles).
- Total two-wheeled vehicles (bikes, motorbikes, scooters).
- Traffic counts at specific junctions or directions.
- Number of speed violations.
- Peak traffic hours and timestamps.
- Weather impact (e.g., hours of rain).

### 3. Results Storage
- Saves analysis results in a text file: `results.txt`.
- Appends results if additional datasets are analyzed.
