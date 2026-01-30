# Largest Concatenated Number

This project implements two versions of an algorithm that arranges a list of digits so that their concatenation forms the **largest possible number**.

Two implementations are provided:

- A **naive** approach using repeated maximum selection  
- A **fast** approach using **Merge Sort**

---

## 🧠 Problem Description

Given a list of digits, reorder them so that when they are concatenated, they form the largest possible number.

Example:

Input: [0, 6, 8, 9, 2, 9, 1, 0]

Sorted order for maximum concatenation:

[9, 9, 8, 6, 2, 1, 0, 0]

Result: 99862100


---

## 📁 Project Structure

├── naive.py # Brute-force solution
└── fast.py # Optimized Merge Sort solution


---

## 🐢 Naive Version

The naive implementation works by repeatedly finding the largest remaining number and appending it to the result.

### How it works
1. Find the largest element in the list
2. Append it to the result string
3. Remove it from the list
4. Repeat until the list is empty

### Time Complexity
Finding the maximum takes **O(n)** and is done **n times**, so: O(n²)


---

## ⚡ Fast Version (Merge Sort)

This implementation sorts the list in descending order using **Merge Sort**, then concatenates the numbers.

### How it works
1. Sort the list in descending order
2. Concatenate the digits into a string

### Time Complexity
- Merge Sort: **O(n log n)**
- Concatenation: **O(n)**  
- **Total: O(n log n)**

---

## ▶ How to Run

Run either version from the terminal.

### Naive Version
```bash
python largest_concatenate.py
python largest_concatenate_fast.py





    
