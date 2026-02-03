# 🧮 Fractional Knapsack — Naive vs Fast Implementation

This project implements two versions of the **Fractional Knapsack Problem** in Python:

1. A **naive greedy implementation**
2. An **optimized version using merge sort (O(n log n))**

The goal is to maximize the total value placed into a bag with limited capacity by selecting fractions of items based on their **value-to-weight ratio**.

---

## 📌 Problem Description

Given:
- A list of item values  
- A list of corresponding item weights  
- A maximum bag capacity  

We want to select items (possibly fractionally) so that the total value in the bag is as large as possible.

The optimal greedy strategy is to take items in decreasing order of:
value density = value / weight

---

## 🧪 Example

```python
values  = [40, 44, 49, 32]
weights = [5, 4, 7, 8]
bag     = 9
| Item | Value | Weight | Value / Weight |
| ---- | ----- | ------ | -------------- |
| 1    | 40    | 5      | 8.0            |
| 2    | 44    | 4      | 11.0           |
| 3    | 49    | 7      | 7.0            |
| 4    | 32    | 8      | 4.0            |
The algorithm should take the highest ratios first.

