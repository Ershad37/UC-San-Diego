# 📈 Maximum Dot Product (Greedy + Merge Sort)

A Python program that calculates the **maximum dot product** of two integer arrays.

The maximum dot product is obtained by rearranging the arrays so that large numbers are multiplied together.

---

## 📌 Problem Description

Given two arrays of integers:

- Rearrange both arrays
- Multiply corresponding elements
- Return the maximum possible sum of products

Mathematically:
max Σ (a[i] × b[i])

---

## 🧠 Algorithm

The solution uses a **greedy strategy**:

1. Sort both arrays in **descending order**
2. Multiply elements at the same indices
3. Sum the products

Sorting is implemented using **Merge Sort**.

### Why it works?

Pairing the largest numbers together always maximizes the total sum.

---

## ⏱ Complexity

- **Time Complexity:** `O(n log n)` (due to merge sort)
- **Space Complexity:** `O(n)`

---

## ▶️ Example

```python
arr1 = [2, 3, 9]
arr2 = [7, 4, 2]
sorted:
arr1 → [9, 3, 2]
arr2 → [7, 4, 2]
Dot Product:
9×7 + 3×4 + 2×2 = 63 + 12 + 4 = 79

Output:
79

