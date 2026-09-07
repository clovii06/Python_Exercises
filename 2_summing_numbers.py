# 2. Summing Numbers
"""
Pseudocode:
function mysum(*numbers):
    result = 0
    repeat i amount of times:
        result = result + i
    return result

display sum
"""

def mysum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result

print(mysum(10, 20, 30))
