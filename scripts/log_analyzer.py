from pathlib import Path

# Location of the log file
log_file = Path("logs/app.log")

# Check that the log file exists
if log_file.exists():
    print("Log file found.")

    # Read the entire log file
    log_contents = log_file.read_text()
    print(log_contents)

    # Split the log into individual lines
    lines = log_contents.splitlines()

    # Counters
    info_count = 0
    warning_count = 0
    error_count = 0

    # Store error messages
    error_messages = []

    # Analyze each log line
    for line in lines:
        if "INFO" in line:
            info_count += 1

        elif "WARNING" in line:
            warning_count += 1

        elif "ERROR" in line:
            error_count += 1

            # Remove date, time, and severity from the message
            error_message = " ".join(line.split()[3:])
            error_messages.append(error_message)

    # Display summary
    print("\n--- Log Summary ---")
    print(f"INFO: {info_count}")
    print(f"WARNING: {warning_count}")
    print(f"ERROR: {error_count}")

    # Display error messages
    print("\n--- Errors Found ---")

    for error in error_messages:
        print(error)

else:
    print("Log file not found.")
