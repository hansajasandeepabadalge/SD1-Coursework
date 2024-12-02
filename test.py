
def count_timestamps_by_hour(file_path):
    timestamps = {}

    with open(file_path, "r") as file:
        for lines in file:
            date = lines.split(",")[2]
            timestamps.append(date)


    # Dictionary to hold counts for each hour
    hour_counts = {}

    # Process each timestamp
    for time in timestamps:
        hour = time.split(":")[0]  # Extract the hour part
        if hour not in hour_counts:
            hour_counts[hour] = 0
        hour_counts[hour] += 1

    # Print the counts
    for hour, count in sorted(hour_counts.items()):
        print(f"Hour {hour}: {count}")

