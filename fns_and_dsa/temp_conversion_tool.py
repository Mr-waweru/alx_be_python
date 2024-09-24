# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            break
        except ValueError:
            print("Please enter a numeric value.")
            continue
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == "C":
        convert_temperature =  convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {convert_temperature}°F")
    elif unit == "F":
        convert_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {convert_temperature}°C")
    else:
        print("Invalid unit!")


if __name__ == "__main__":
    main()










