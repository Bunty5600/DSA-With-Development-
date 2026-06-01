# Two Sum — Fast Lookup in Modern Systems

> How a simple array problem maps to real backend engineering decisions.

---

## Table of Contents

- [Problem](#problem)
- [Brute Force](#brute-force)
- [Why It Fails at Scale](#why-it-fails-at-scale)
- [Optimized Approach](#optimized-approach)
- [Walkthrough](#walkthrough)
- [Complexity](#complexity)
- [Real World Connection](#real-world-connection)
- [Key Takeaway](#key-takeaway)

---

## Problem

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

Find the indices of two numbers that add up to the target.

---

## Brute Force

Check every possible pair until a match is found.

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

**Time:** O(n²) &nbsp;|&nbsp; **Space:** O(1)

Works correctly. But every new element means scanning all previous elements again.

---

## Why It Fails at Scale

Consider an e-commerce platform suggesting product bundles in real time.

At small scale — fine. But at production scale:

- Millions of products in the catalog
- Thousands of requests per second
- Every request triggers another full scan

The system is doing work it already did. That is the problem.

---

## Optimized Approach

Instead of re-scanning, store each value as you go and check against it instantly.

**The idea:**

For each number, calculate what complement is needed to reach the target.
Then check if that complement was already seen — in O(1) time using a HashMap.

```
current = 7
target  = 9
need    = 9 - 7 = 2  →  already in map? yes → done
```

```python
class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mp:
                return [mp[need], i]
            mp[nums[i]] = i
        return []
```

**Time:** O(n) &nbsp;|&nbsp; **Space:** O(n)

One pass through the array. No repeated scanning.

---

## Walkthrough

```
nums = [2, 7, 11, 15]   target = 9
```

| Step | Current | Need | HashMap State | Action             |
|------|---------|------|---------------|--------------------|
| 1    | 2       | 7    | `{}`          | 7 not found. Store 2 → `{2: 0}` |
| 2    | 7       | 2    | `{2: 0}`      | 2 found at index 0. Return `[0, 1]` ✓ |

---

## Complexity

| Approach    | Time  | Space |
|-------------|-------|-------|
| Brute Force | O(n²) | O(1)  |
| HashMap     | O(n)  | O(n)  |

---

## Real World Connection

This exact pattern — store what you have seen, look it up instantly later — shows up across backend systems:

| System                | Application                              |
|-----------------------|------------------------------------------|
| Database indexes      | Avoid full table scans on every query    |
| Redis / Memcached     | Retrieve computed results without recalculating |
| Auth systems          | Fast token and session lookup            |
| Recommendation engines | Match related items without re-processing |
| Search engines        | Inverted index for instant keyword hits  |

All of them trade a little memory to eliminate redundant computation.

---

## Key Takeaway

The optimization is not about doing the same work faster.  
It is about **not repeating work you already did**.

Whenever you see:

- pair finding
- repeated searching through the same data
- need for fast retrieval of previously processed values

reach for a **HashMap**.

---

## Pattern

```
Repeated Search  →  Store Once, Look Up Instantly  →  HashMap  →  O(n)
```