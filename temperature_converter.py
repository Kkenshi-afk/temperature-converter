def celcius_to_fahrenheit(x):
    return (x*(9/5)+32)

def fahrenheit_to_celcius(x):
    return ((x-32)*5)/9
choice=""
while choice != "exit":
    choice=input("Please enter your choice(f=celcius to fahrenheit),(c=fahrenheit to celcius) and (exit = exit):")
    if choice=="exit":
        break
    x=int(input("Please enter your veriable:"))
    if choice=="f":
        result=celcius_to_fahrenheit(x)
    elif choice =="c":
        result=fahrenheit_to_celcius(x)
    else:
        print("Please enter true veriable!!!")