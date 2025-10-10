# -------------------------------
# mymodule.py
# Custom module example
# -------------------------------

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def greet(name):
    print(f"Hello, {name}! Welcome to Python modules demo.")

# This function runs only if file executed directly, not when imported
if __name__ == "__main__":
    print("This code runs only when you directly run mymodule.py")
    print("Testing add(2,3):", add(2, 3))
