def celcius_to_fahrenheit(x):
    return (x*(9/5)+32)

def fahrenheit_to_celcius(x):
    return ((x-32)*5)/9
choice=""
while choice != "exit":
    choice=input("Please enter your choice (f = Celsius to Fahrenheit, c = Fahrenheit to Celsius, exit = Exit): ").lower()
    if choice=="exit":
        break
    try:
        x=float(input("Please enter the temperature value::"))
        if choice=="f":
            result=celcius_to_fahrenheit(x)
            print(f"{x}°C is equal to {result}°F")
        elif choice =="c":
            result=fahrenheit_to_celcius(x)
            print(f"{x}°F is equal to {result}°C")
        else:
            print("Invalid choice! Please enter 'f', 'c', or 'exit'.")
    except ValueError:
        print("Invalid input! Please enter a numeric temperature value.")