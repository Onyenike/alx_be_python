FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
   A = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
   print(A)
    



def convert_to_fahrenheit(celsius):
   B = celsius *CELSIUS_TO_FAHRENHEIT_FACTOR 
   print(B)
 
 
Temp = float(input('Enter the temperature to convert'))
UNIT = input('Is this temperature in Celsius or Fahrenheit?');
if UNIT == 'F':
    convert_to_celsius(Temp)
else:
    convert_to_fahrenheit(Temp)
