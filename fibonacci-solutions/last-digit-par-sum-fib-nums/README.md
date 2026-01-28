# Last Digit of Partial Sum of Fibonacci Numbers

## Description

This Python program computes the **last digit of the sum of Fibonacci numbers from index `m` to index `n` (inclusive)**.  
It is optimized using the **Pisano period modulo 10**, which allows handling very large indices efficiently.

## Problem Statement

Given two non-negative integers `m` and `n`, calculate:
    F_m + F_{m+1} + ... + F_n

and output **only the last digit** of this sum.

## Key Concepts Used

- Fibonacci sequence
- Modular arithmetic
- Pisano period (mod 10 → period = 60)
- Efficient iteration without large integers

## How It Works

1. Reduce `m` and `n` using modulo 60 (Pisano period for mod 10).
2. Generate Fibonacci numbers up to `n`.
3. Sum Fibonacci values only when the index is ≥ `m`.
4. Return the last digit of the total sum.

## How to Run

```bash
python last_digit_par_sum_fib_nums.py

