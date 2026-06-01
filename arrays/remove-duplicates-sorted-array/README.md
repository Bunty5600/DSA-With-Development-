# Remove Duplicates from Sorted Array

### How In-Place Data Optimization Works Inside Large Systems

---

## Problem

Given a sorted array:

```python
[1,1,2,2,3,4,4]
```

remove duplicates in-place such that each unique element appears only once.

Return the number of unique elements.

---

## A Real Situation

Imagine a backend analytics system collecting millions of logs every hour.

Because of:

* retries
* duplicate events
* sync issues

repeated records often appear:

```text
[login, login, purchase, purchase, logout]
```

Keeping duplicate data:

* wastes memory
* increases storage cost
* slows down processing

Modern systems constantly clean and compact data before storing or analyzing it.

The engineering question becomes:

> How can systems remove duplicate data efficiently without creating another large array in memory?

---

## Brute Force

The simplest idea:

* create another array
* manually store unique values

```python
class Solution:
    def removeDuplicates(self, nums):

        temp = [0] * len(nums)

        temp[0] = nums[0]

        j = 1

        for i in range(1, len(nums)):

            found = False

            for k in range(j):

                if temp[k] == nums[i]:
                    found = True
                    break

            if not found:

                temp[j] = nums[i]

                j += 1

        for i in range(j):

            nums[i] = temp[i]

        return j
```

Correct.

But this approach:

* creates extra memory
* copies data again
* becomes inefficient for massive datasets

---

## The Better Question

The array is already sorted:

```python
[1,1,2,2,3,4,4]
```

This means duplicates are always adjacent.

Instead of creating another array,
can the system overwrite duplicates directly inside the same memory space?

This is where:

# Two Pointers

becomes useful.

One pointer reads values.

Another pointer writes only unique values.

This creates:

```text
In-Place Optimization
```

with constant extra memory.

---

## Optimized Solution

```python
class Solution:
    def removeDuplicates(self, nums):

        if len(nums) == 0:
            return 0

        write = 1

        for read in range(1, len(nums)):

            if nums[read] != nums[read - 1]:

                nums[write] = nums[read]

                write += 1

        return write
```

### Walkthrough — `[1,1,2,2,3,4,4]`

| Read | Current | Action             | Array             |
| ---- | ------- | ------------------ | ----------------- |
| 1    | 1       | Duplicate → Skip   | `[1,1,2,2,3,4,4]` |
| 2    | 2       | Write unique value | `[1,2,2,2,3,4,4]` |
| 3    | 2       | Duplicate → Skip   | `[1,2,2,2,3,4,4]` |
| 4    | 3       | Write unique value | `[1,2,3,2,3,4,4]` |

---

## Complexity

| Approach     | Time  | Space |
| ------------ | ----- | ----- |
| Extra Array  | O(n²) | O(n)  |
| Two Pointers | O(n)  | O(1)  |

---

## Where This Pattern Shows Up

| System                 | Why It Matters           |
| ---------------------- | ------------------------ |
| Log processing systems | Remove duplicate logs    |
| Analytics pipelines    | Reduce repeated events   |
| Database cleanup       | Compact repeated records |
| Cache optimization     | Avoid redundant storage  |
| Streaming systems      | Efficient memory usage   |

---

## Takeaway

The optimization here is not about making loops faster.

It is about reducing unnecessary memory usage.

Modern systems scale by:

* reusing memory efficiently
* compacting useful data
* avoiding redundant storage

When a problem involves:

* sorted arrays
* duplicate removal
* in-place modification

think:

# Two Pointers
