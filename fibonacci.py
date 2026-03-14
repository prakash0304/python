# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence:", n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1, end=" ")
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1
