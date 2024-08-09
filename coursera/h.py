import re
import os

def sum_numbers_in_file(filename):
    try:
        with open(filename, 'r') as file:
            total_sum = 0
            for line in file:
                # Find all numbers in the line
                numbers = re.findall(r'[0-9]+', line)
                # Convert extracted strings to integers and sum them
                total_sum += sum(int(num) for num in numbers)
        return total_sum
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Check the current working directory
print(f"Current working directory: {os.getcwd()}")

# Sample file for testing
sample_filename = r'e:\AUES\Third Term\Phyton\Codes\coursera\regex_sum_42.txt'

sample_sum = sum_numbers_in_file(sample_filename)
print(f"Sum of numbers in sample file: {sample_sum}")

# Actual file for the assignment
actual_filename = r'e:\AUES\Third Term\Phyton\Codes\coursera\regex_sum_2059020.txt'
actual_sum = sum_numbers_in_file(actual_filename)
print(f"Sum of numbers in actual file: {actual_sum}")
