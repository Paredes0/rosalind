"""
Problem

Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through  (with space in between), 
inclusively. In other words, we should include elements s[b] and s[d] in our slice.

Sample Dataset:

HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

"""

def slice_string(s:str, a, b, c, d) -> str:
    return s[a:b+1] + " " + s[c:d+1]

with open("rosalind_ini3.txt") as f:
    lines = f.read().strip().split("\n")
    s = lines[0]
    a, b, c, d = map(int, lines[1].split())

print(slice_string(s, a, b, c, d))