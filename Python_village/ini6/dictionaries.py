"""
Problem

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, 
and the lines in the output can be in any order.

Sample Dataset
We tried list and we tried dicts also we tried Zen

Sample Output
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1

"""

def create_dictionary(file: str) -> dict:
    with open(file) as f:
        words = f.read().strip().split()
    
    d = {}

    for word in words:
        d[word] = d.get(word, 0) + 1
    
    return d

rosalind_dict = create_dictionary("rosalind_ini6.txt")

for word, count in rosalind_dict.items():
    print(word, count)