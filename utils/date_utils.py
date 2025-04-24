from datetime import datetime, timedelta

# Function to get tomorrow's date in the format "day month" (e.g., "15 Oct")
def get_tomorrow_day_month():
    # Calculate tomorrow's date by adding 1 day to the current date
    # Format the date as "day month" (e.g., "15 Oct") and return it
    return (datetime.now() + timedelta(days=1)).strftime("%-d %b")

# Function to get tomorrow's weekday in the format "(weekday)" (e.g., "(Mon)")
def get_tomorrow_weekday():
    # Calculate tomorrow's date by adding 1 day to the current date
    # Format the weekday as "(weekday)" (e.g., "(Mon)") and return it
    return (datetime.now() + timedelta(days=1)).strftime("(%a)")
