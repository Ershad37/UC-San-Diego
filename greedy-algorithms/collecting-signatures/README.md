# Collecting Signatures

A simple Python program that finds the **minimum number of points** needed so that each given segment contains at least one selected point.

## How It Works

1. Segments are sorted by their end coordinate using a custom **merge sort**.
2. The algorithm repeatedly selects the end of the earliest finishing segment.
3. All overlapping segments are skipped.
4. The process continues until all segments are covered.

This is a **greedy algorithm** with optimal results.

## Example

Input:
```python
segments = [[1,3], [2,5], [3,6]]
Output:
1
3


 Time Complexity

O(n log n) due to merge sort.

Linear scan after sorting.
