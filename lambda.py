#!/usr/bin/python3
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temperatures = (36.5, 37, 37.5, 38, 39)
F = list(map(fahrenheit, temperatures))
print("{}".format(F))
C = list(map(celsius, F))
print("{}".format(C))
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
print("{}".format(temperatures_in_Fahrenheit))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(temperatures_in_Celsius)