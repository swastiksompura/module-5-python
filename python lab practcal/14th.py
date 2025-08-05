# Q14.Write a Python program that uses a custom iterator to iterate over a list of integers.

# Custom iterator class
class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # returns the iterator object itself

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# List of integers
numbers = [10, 20, 30, 40, 50]

# Create iterator object
my_iterator = ListIterator(numbers)

# Iterate through the list using the custom iterator
for num in my_iterator:
    print(num)
