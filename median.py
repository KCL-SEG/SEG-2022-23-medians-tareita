"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import statistics

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

median = statistics.median(map(float, numbers))
print(f"Median: {median}")
