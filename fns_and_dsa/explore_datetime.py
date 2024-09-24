from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now().replace(microsecond=0)
    format_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print()
    print(f"Current date and time: {format_date}")


def calculate_future_date():
    future_date = int(input("Number of days to add to the current date(as an interger): "))
    current_date = datetime.now().replace(microsecond=0)
    future_date = current_date + timedelta(days=future_date)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    print()

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()


