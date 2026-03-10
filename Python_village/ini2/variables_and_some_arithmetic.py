"""
Problem

Given: Two positive integers a and b , each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

Notes:

The dataset changes every time you click "Download dataset".
We check only your final answer to the downloaded dataset in the box below, not your code itself. If you would like to provide your code as well, 
you may use the upload tool. Please also note that the correct answer to this problem will not in general be 34; it is simply an example of what 
you should return in the specific case that the legs of the triangle have length 3 and 5.
"""

def hypotenuse(a, b) -> int:
    return a**2 + b**2

with open("rosalind_ini2.txt") as f:
    a, b = map(int, f.read().strip().split())

print(hypotenuse(a,b))