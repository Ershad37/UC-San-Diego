# 💰 Money Change (Greedy Algorithm)

A simple Python program that calculates the **minimum number of coins** needed to make change for a given amount of money.

The available coin denominations are:

- `10`
- `5`
- `1`

---

## 📌 Problem Description

Given an integer amount of money, determine the minimum number of coins required to represent that amount using coins of denominations `10`, `5`, and `1`.

---

## 🧠 Algorithm

The solution uses a **greedy approach**:

1. Use as many `10`-value coins as possible.
2. Then use as many `5`-value coins as possible.
3. Use `1`-value coins for the remaining amount.

Because the coin system `{10, 5, 1}` is canonical, the greedy strategy always produces the optimal solution.

---

## ⏱ Complexity

- **Time Complexity:** `O(1)`  
- **Space Complexity:** `O(1)`

---

## ▶️ Example

```python
money = 105
Step-by-step:
105 → 10×10 coins (100)
Remaining: 5 → 1×5 coin
Total coins used: 11
Output:
11
