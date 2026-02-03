# 👶 Minimum Number of Groups (Greedy Algorithm)

This program groups children by age so that the **difference between the youngest and oldest child in each group is at most 2 years**, while using the **minimum number of groups**.

---

## 📌 Problem

Given a list of children’s ages, split them into groups such that:
max_age_in_group − min_age_in_group ≤ 2

and the total number of groups is minimized.

---

## 🧠 Greedy Strategy

The algorithm follows this rule:

> Always start a new group with the **youngest ungrouped child** and include as many children as possible whose ages are within 2 years of that child.

This works because:
- The youngest child must be placed somewhere.
- Including as many compatible children as possible reduces the total number of groups.

---

## 🧪 Example

Input:
```python
children = [2,2,3,4,4,5,6,6,6,7,8,9]
The algorithm builds groups like this:
| Group | Start Age | Allowed Range | Children Included |
| ----- | --------- | ------------- | ----------------- |
| 1     | 2         | 2 – 4         | 2, 2, 3, 4, 4     |
| 2     | 5         | 5 – 7         | 5, 6, 6, 6, 7     |
| 3     | 8         | 8 – 10        | 8, 9              |
output:
[(2, 4), (5, 7), (8, 10)]
So only 3 groups are needed.
