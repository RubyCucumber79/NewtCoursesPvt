# Coding & Debugging Prompts - Advanced Prompt Engineering

## Debug Python Code

**Prompt:**
```
This code throws an error. Fix it:

```
def add_numbers(a, b)
    return a + b
```
```

**ChatGPT Response:**
```
The error is due to a missing colon after the function definition.
Corrected code:
```
def add_numbers(a, b):
    return a + b
```
```

## Explain Code Prompt

**Prompt:**
```
What does the following Python code do?

```
squares = [x**2 for x in range(10) if x % 2 == 0]
```
```

**ChatGPT Response:**
```
This code creates a list of the squares of even numbers from 0 to 9. Result: [0, 4, 16, 36, 64]
```

