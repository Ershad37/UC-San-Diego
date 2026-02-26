# Counting Sort (Python)

A simple Python implementation of the **Counting Sort** algorithm.

This program demonstrates how counting sort works by sorting a list of
non-negative integers using frequency counting instead of comparisons.

---

## 📌 Overview

Counting Sort is a non-comparison sorting algorithm that works by:

1. Counting how many times each value appears.
2. Reconstructing the sorted array using those counts.

It is efficient when the range of input values is not significantly larger
than the number of elements.

---

## ⚙️ How It Works

The program:

- Creates a counting array
- Counts occurrences of each number
- Rebuilds a sorted list based on those counts
- Prints the sorted result

Example input:
[2,3,1,3,4,2,2,5,6,2,1,2,3,4,3,2,1]

Example output:
[1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6]

## How to run

python3 count_sort.py
