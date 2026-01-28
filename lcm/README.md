# 📐 Least Common Multiple (LCM) in Python

This program computes the **Least Common Multiple (LCM)** of two positive integers using **two different approaches**:
1. A **naive solution** based on factorization
2. A **fast solution** using the **Greatest Common Divisor (GCD)**

---

## 🧠 Problem Statement

Given two integers `a` and `b`, determine their **Least Common Multiple (LCM)**.

The LCM is the **smallest positive integer** that is divisible by both numbers.

---

## 🐢 Naive Solution

### Description

The naive approach calculates the LCM by:
- Repeatedly dividing both numbers by common factors
- Storing the common factors
- Multiplying the remaining values at the end

### Characteristics

- Simple and easy to understand
- Inefficient for large numbers
- High time complexity

---

## ⚡ Fast Solution (Using GCD)

### Description

The optimized solution uses the formula:
    LCM(a, b) = (a × b) / GCD(a, b)

The **Greatest Common Divisor (GCD)** is computed using **Euclid’s Algorithm**, which is highly efficient.

### Characteristics

- Very fast, even for large inputs
- Uses recursion
- Time complexity: **O(log(min(a, b)))**

---

## ▶️ How to Run

```bash
python lcm_naive.py
python lcm_fast.py


