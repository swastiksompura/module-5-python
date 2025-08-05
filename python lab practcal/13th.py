# Q13. Write a generator function that generates the first 10 even numbers.

# Generator function
def even_numbers():
    for i in range(10):
        yield i * 2

# Using the generator
for num in even_numbers():
    print(num)
