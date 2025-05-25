print("Name   : Sahil Gurav")
print("USN    : 1AY24AI093")
print("Section: O\n")
grid = [
    [' ', ' ', '*', '*', '*', ' ', ' '],
    [' ', '*', ' ', ' ', ' ', '*', ' '],
    ['*', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', '*'],
    [' ', '*', ' ', ' ', ' ', '*', ' '],
    [' ', ' ', '*', '*', '*', ' ', ' ']
]
for row in grid:
    row_string = ''.join(row)
    print(row_string)
