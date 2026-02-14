# 🎁 Maximum Number of Prizes

This project contains a simple Python program that computes the **maximum number of distinct prizes** that can be distributed such that their sum equals a given number `n`.

The algorithm greedily builds a list of increasing natural numbers whose total equals `n`, ensuring all prizes are **distinct**.

---

## 📌 Problem Description

Given a positive integer `n`, the goal is to represent it as a sum of the **maximum number of distinct positive integers**.

### Example

For:

n = 39

One valid optimal solution is:

1 + 2 + 3 + 4 + 5 + 6 + 7 + 11 = 39

This uses the largest possible number of distinct prizes.

---

## ⚙️ How It Works

The program uses a **greedy algorithm**:

1. Start assigning prizes beginning from `1`.
2. Keep adding the next integer (`2`, `3`, `4`, …).
3. Only add a prize if the remaining value can still form a larger distinct prize.
4. Stop when the remaining value exactly matches the next prize.

This guarantees:
- All prizes are distinct.
- The number of prizes is maximized.

---

## How to run

python3 maximum_number_of_prizes.py



