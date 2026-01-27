# Last Digit of Sum of Squares of Fibonacci Numbers

## Description

This Python program computes the **last digit of the sum of the squares of the first `n` Fibonacci numbers** efficiently. It leverages properties of Fibonacci numbers and modular arithmetic to calculate the result without computing all Fibonacci numbers explicitly.

## Problem Statement

Write a program that:

1. Accepts a non-negative integer `n`.
2. Computes the sum of squares of the first `n` Fibonacci numbers:
    F_0^2 + F_1^2 + ... + F_n^2
3. Returns the **last digit** of this sum.
4. Optimizes the calculation using the fact that:
    Sum of squares of first n Fibonacci numbers = F_n * F_(n+1)
and uses modulo arithmetic to avoid large number computations.

## How to Run

```bash
python sum_squares.py
