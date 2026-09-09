# 4. Hexadecimal Output

"""
Pseudocode:

function hex_output():
    decimal_number = 0
    get hex_number

    for power, digit in enumerate(reversed(hex_number)):
        decimal_number = digit * (16 ** power)
    display decimal_number

hex_output()
"""

def hex_output():
    """Convert a hexadecimal number to a decimal"""
    decimal_number = 0
    hex_number = input("Enter a hexadecimal number: ")

    for power, digit in enumerate(reversed(hex_number)):
        decimal_number = int(digit, 16) * (16 ** int(power))
    print(decimal_number)

hex_output()