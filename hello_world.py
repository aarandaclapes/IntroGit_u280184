# My first file tracked by Git
# Author: Andreu Aranda Clapés

def greet(name):
    """Return a welcome message for the given name."""
    return f"Hello, {name}! Welcome to Git."

def farewell(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}! See you next commit."

def count_words(text):
    """Count the number of words in the given text."""
    words = text.split()  # Split the string by whitespace into a list
    return len(words)     # Return the number of elements in the list

# This block runs only when the file is executed directly,
# not when it is imported as a module from another file.
if __name__ == "__main__":
    print(greet("World"))  # Call the greet function and print the result
    print(farewell("World"))  # Call the farewell function and print the result
    print(f"Word count: {count_words('Hello World Welcome to Git')}")