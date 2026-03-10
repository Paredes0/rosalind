"""
Problem

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset
100 200

Sample Output
7500

"""

def odd_sum(a, b) -> int:
    total_sum = 0
    for i in range(a,b+1):
        if i % 2 != 0:
            total_sum += i
    return total_sum

with open("rosalind_ini4.txt") as f:
    a, b = map(int, f.read().strip().split())

print(odd_sum(a,b))