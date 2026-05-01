# Practice with for loops, range(), and list operations
# From Penn Coursera - Introduction to Python Programming

# --- Example 1: Iterating over a list ---
# Find even numbers in a list and count them

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)
print("There are", len(even_numbers), "even numbers in the list.")


# --- Example 2: Using range() with a step ---
# Print every 7th number from 0 up to 28

for x in range(0, 29, 7):
    print(x)


# --- Example 3: My own twist ---
# Find numbers in a list that are divisible by 3

my_numbers = [10, 15, 22, 27, 30, 41, 45]
divisible_by_three = []

for n in my_numbers:
    if n % 3 == 0:
        divisible_by_three.append(n)

print("Numbers divisible by 3:", divisible_by_three)
