# Last Digit of Sum of Fibonacci Numbers

## Description

**Last Digit of Sum of Fibonacci Numbers** is a Python program that calculates the **last digit of the sum of the first `n` Fibonacci numbers** efficiently. It uses the Pisano period property and modular arithmetic to avoid computing large Fibonacci numbers directly.

## Problem Statement

Write a program that:

1. Accepts a non-negative integer `n`.
2. Computes the sum of the first `n` Fibonacci numbers:
    F_0 + F_1 + ... + F_n
3. Returns the **last digit** of this sum.
4. Optimizes the calculation using:
- The Pisano period modulo 10 (which is 60)
- Modular arithmetic to handle very large numbers.

## How to Run

```bash
python last_digit_sum_fib_nums.py
