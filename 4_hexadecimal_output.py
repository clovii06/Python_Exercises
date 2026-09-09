# 4. Hexadecimal Output

"""
Pseudocode:

function hex_output():
    get hex_number

    for power, digit in enumerate(hex_number):
        print(power, digit)

"""

def hex_output():
    hex_number = input("Enter a hexadecimal number: ")

    for power, digit in enumerate(reversed(hex_number)):
        print(f"{digit} to the power of {power}")

hex_output()