# 📅 Job Scheduling Profit Calculator

This project implements a simplified solution to the **Job Scheduling Problem** using Python.  
The program calculates the **maximum achievable profit** based on job deadlines and profits.

Jobs are first sorted by their deadlines using **Merge Sort**, and then the algorithm selects the most profitable job for each deadline group.

---

## 📌 Problem Description

Each job has:

- 🏷 **Job ID** – identifier of the job
- 💰 **Profit** – earned if the job is completed on time
- ⏰ **Deadline** – latest time slot in which the job can be completed

### Assumptions

- Each job takes **exactly one unit of time**.
- Only one job can be executed at a time.
- Jobs sharing the same deadline compete with each other.
- The algorithm selects the **highest-profit job per deadline**.

---

## ⚙️ How the Program Works

The program follows these steps:

1. **Sort jobs by deadline** using a custom Merge Sort implementation.
2. **Group jobs with identical deadlines**.
3. From each group, select the job with the **maximum profit**.
4. Sum the selected profits to compute the final result.

---

## How to run
python3 job_scheduling.py


