# Chapter 8 - Functions & Recursions

This chapter introduced the power of **functions** in Python — reusable blocks of code that make programs organized and efficient. I also learned about **recursion**, where functions call themselves.

## 🧠 Concepts Covered

* Defining and calling functions with `def`
* Function parameters and return values
* Scope of variables (local vs global)
* Recursion and base cases
* Lambda (anonymous) functions

## 💻 Example Code

```python
# Example: Recursive factorial function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
```

## 📚 Example Output

```
Factorial of 5: 120
```

## 🔗 Navigation

⬅️ [Previous → Chapter 7 - Practice Set](../Chapter%207%20-%20Practice%20Set/)
➡️ [Next → Chapter 8 - Practice Set](../Chapter%208%20-%20Practice%20Set/)
