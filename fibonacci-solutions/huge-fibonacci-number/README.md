# Huge Fibonacci Number Modulo

## Description

**Huge Fibonacci Number Modulo** is a Python program that efficiently computes the remainder of a very large Fibonacci number `F_n` when divided by `m`. The program uses the **Pisano period** property to handle extremely large Fibonacci numbers without calculating them directly.

## Problem Statement

Write a program that:

1. Accepts two integers:
   - `n` → the index of the Fibonacci number
   - `m` → the modulus
2. Computes `F_n mod m` efficiently using:
   - The **Pisano period**: Fibonacci numbers modulo `m` repeat in cycles.
3. Returns the result without computing all Fibonacci numbers up to `n`.

### Key Concepts

- **Pisano period**: For any integer `m`, the sequence of Fibonacci numbers modulo `m` repeats with a certain period.
- Using the period allows reducing `n` modulo the period to avoid computing extremely large numbers.

## How to Run

```bash
python huge_fibonacci_number.py
