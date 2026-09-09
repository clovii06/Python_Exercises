# 4. Hexadecimal Output

"""
Pseudocode:

function hex_output():
    get hex_number

    for power, digit in enumerate(reversed(hex_number)):


"""

def hex_output():
    hex_number = input("Enter a hexadecimal number: ")

    for power, digit in enumerate(reversed(hex_number)):
        print(f"{digit} to the power of {power}")
        digit = int(digit, 16) # Convert each digit to integer with base of 16
        print(digit)



hex_output()