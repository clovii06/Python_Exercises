# 2. Summing Numbers
"""
Pseudocode:
function mysum(*numbers):
    result = 0
    repeat numbers of times:
        result = result + numbers
    return result

display sum
"""

def mysum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result

print(mysum(1, 2, 3))
