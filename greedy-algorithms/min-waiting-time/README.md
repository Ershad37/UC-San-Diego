# Minimum Waiting Time Algorithm

This project implements and compares two approaches for solving the **Minimum Waiting Time** problem:

- A **fast** version using **Merge Sort**
- A **naive** version using repeated minimum selection

The goal is to schedule jobs (or tasks) in an order that minimizes the total waiting time.

---

## 🧠 Problem Definition

Given a list of task durations, the objective is to arrange them in an order that minimizes the **total waiting time**.

For a sorted list of task times  
`t₁, t₂, t₃, ..., tₙ`  

The total waiting time is computed as:

\[
t_1(n-1) + t_2(n-2) + ... + t_{n-1}(1) + t_n(0)
\]

The optimal strategy is to process the **shortest tasks first**.

---

## 📁 Project Structure

├── fast.py # Optimized implementation using Merge Sort
└── naive.py # Brute-force implementation


---

## ⚡ Fast Version (Merge Sort)

This implementation sorts the task times using **Merge Sort** and then computes the waiting time efficiently.

### Key Idea
Sort the tasks first, then compute:
    (n - i - 1) × t[i]
for each position `i`.

### Time Complexity
- Merge Sort: **O(n log n)**
- Waiting time calculation: **O(n)**
- **Total: O(n log n)**

---

## 🐢 Naive Version

This implementation repeatedly selects the smallest untreated task and accumulates its waiting time.

### Key Idea
Simulate selection sort:
- Each round finds the smallest remaining task
- Marks it as processed
- Adds its contribution to total waiting time

### Time Complexity
- Nested loops → **O(n²)**

---

## ▶ How to Run

Both programs can be run directly.

### Fast Version
```bash
python min_waiting_time.py
python min_waiting_time_fast.py
