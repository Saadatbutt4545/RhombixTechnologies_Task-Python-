# Function to generate Fibonacci series
def fibonacci_series(n):
    fib_sequence = [0, 1]  # Starting two numbers of the Fibonacci sequence
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Display the Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer.")
elif num_terms == 1:
    print("Fibonacci series up to", num_terms, "term: [0]")
else:
    result = fibonacci_series(num_terms)
    print(f"Fibonacci series up to {num_terms} terms: {result}")

