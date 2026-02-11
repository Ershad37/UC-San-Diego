# ⛽ Minimum Fueling Stops

A simple Python program that calculates the **minimum number of refueling stops** required to reach a destination.

---

## 📌 Problem Description

Given:

- `d` — total distance to the destination  
- `m` — maximum distance the car can travel on a full tank  
- `stops` — list of gas station distances from the starting point  

The program returns:

- The **minimum number of refills** needed to reach the destination  
- `-1` if the destination cannot be reached  

---

## 🧠 Algorithm

The solution uses a **greedy approach**:

1. Start at position `0`.
2. Always move to the farthest reachable gas station within range `m`.
3. Refill only when necessary.
4. If no further station is reachable, return `-1`.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

---

## ▶️ Usage

### Input Format (from standard input)

d m n stop1 stop2 ... stopn

## How to run
python3 car_fueling.py
