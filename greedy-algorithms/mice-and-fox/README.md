# 🐭🕳️ Mice and a Fox — Optimal Escape Strategy

This project implements a solution to the **Mice and a Fox Problem**, a classic greedy algorithm problem.

Given positions of mice and holes on a number line, the program computes an optimal assignment strategy that minimizes the **maximum distance** any mouse must travel to reach a hole.

---

## 📌 Problem Description

A group of mice spots a fox and must escape into nearby holes.

Each mouse:

- moves at the same speed,
- must enter exactly one hole,
- and each hole can hold only one mouse.

The goal is to assign mice to holes such that:

> the **longest distance traveled by any mouse** is as small as possible.

---

## 🎯 Objective

Minimize:
max |mouse_position − hole_position|


This represents minimizing the time required for the **last mouse** to reach safety.

---

## ⚙️ How the Program Works

The program follows these steps:

1. **Sort mouse positions** using Merge Sort.
2. **Sort hole positions** using Merge Sort.
3. Pair mice and holes in sorted order.
4. Compute distances between each matched pair.
5. Track the largest distance (escape time).

---

## How to run
python3 mice_and_fox.py


