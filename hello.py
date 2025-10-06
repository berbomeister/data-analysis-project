import sys

# A function to greet
def greet(name):
    """A function that prints a greeting."""
    print(f"Hello, {name}!") # The main change we want
    # The LLM also added this logging, which we don't want

if __name__ == '__main__':
    greet("Git")