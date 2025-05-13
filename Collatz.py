def collatz_sequence(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
try:
    num = int(input("Enter number: "))
    if num > 0:
        collatz_sequence(num)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input! Please enter an integer.")
