# Dual Numbers in Python

This repository provides an implementation of dual numbers in Python. Dual numbers are an extension of real numbers and are useful in automatic differentiation, allowing for efficient computation of derivatives.

## Overview

A dual number is of the form:

```
a + bε
```

where:
- `a` is the real part.
- `b` is the dual part.
- `ε` is the dual unit with the property that ε² = 0, but ε ≠ 0.

## Features

The `Dual` class supports:
- **Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Unary Operations**: Negation.
- **Exponentiation**: Raising to a power (powers greater than or equal to 1).
- **Mathematical Functions**:
    - Exponential (`exp`)
    - Logarithm (`log`)
    - Trigonometric functions (`sin`, `cos`, `tan`)
    - Hyperbolic functions (`sinh`, `cosh`, `tanh`)

## Usage

### Creating Dual Numbers

Import the `Dual` class and create dual numbers by specifying the real and dual parts:

```python
from dual import Dual

# Variable with respect to which differentiation is performed
x = Dual(5, 1)

# Constant
c = Dual(3, 0)
```

### Performing Operations

```python
# Addition
result = x + c

# Subtraction
result = x - c

# Multiplication
result = x * c

# Division
result = x / c
```

### Computing Derivatives

To compute the derivative of a function at a point:

```python
# Function: f(x) = x^2
x = Dual(5, 1)
f = x ** 2

# Function value at x = 5
print(f.real)  # Output: 25

# Derivative at x = 5
print(f.dual)  # Output: 10
```

### Using Mathematical Functions

```python
# Exponential function
result = x.exp()

# Logarithmic function
result = x.log()

# Trigonometric functions
result = x.sin()
result = x.cos()
result = x.tan()

# Hyperbolic functions
result = x.sinh()
result = x.cosh()
result = x.tanh()
```

## Notes

- Division by a dual number with a zero real part raises a `ZeroDivisionError`.
- The exponentiation function supports powers greater than or equal to 1.
