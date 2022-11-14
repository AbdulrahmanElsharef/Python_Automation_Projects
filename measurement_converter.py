def Celsius():
    '''function that can convert
Fahrenheit to Celcius and back'''
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}% Celsius is:{fahrenheit}% Fahrenheit'.title())
    # Enter temperature in celsius: 35
    # 35.0% Celsius Is:95.0% Fahrenheit

Celsius()

print(100*"*")

def inch_to_cm():
    inch = int(input('Enter the value in inch: '))
    cm= inch * 2.54
    print(f'{inch}inch = {cm}cm')

inch_to_cm()