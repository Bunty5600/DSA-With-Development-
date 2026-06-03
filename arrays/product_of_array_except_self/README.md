# Product of Array Except Self

## Problem

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i]
```

contains the product of all elements in `nums` except `nums[i]`.

You must solve it:

* without using division
* in O(n) time

---

# Real World Situation

Imagine a class where every student contributes marks to a group activity.

Now for every student, the teacher wants:

```text
total contribution of all OTHER students
```

A slow method would repeatedly calculate everyone's marks again and again for every student.

Efficient systems instead:

* preserve useful computation
* reuse previously calculated information
* avoid repeated work

That is exactly what this problem teaches.

---

# Brute Force

The first approach is:

```text
For every index,
multiply all other elements.
```

## Brute Force Code

```python
class Solution:

    def productExceptSelf(self, nums):

        n = len(nums)

        result = [0] * n

        for i in range(0, n):

            prod = 1

            for j in range(0, n):

                if i != j:

                    prod *= nums[j]

            result[i] = prod

        return result
```

---

# Main Problem in Brute Force

The same multiplication gets recalculated repeatedly.

Example:

```text
3 × 4
```

may be recomputed many times for different indexes.

This creates unnecessary repeated work.

Time complexity becomes:

```text
O(n²)
```

which becomes expensive for large inputs.

---

# Better Question

Instead of asking:

```text
How do we multiply everything repeatedly?
```

Ask:

```text
How can we preserve reusable multiplication information?
```

That changes the entire optimization strategy.

---

# Optimization Insight

For every index:

```text
answer =
(product before current index)
×
(product after current index)
```

This splits the problem into:

* prefix multiplication
* suffix multiplication

Instead of recalculating everything repeatedly, the algorithm preserves reusable computation.

---

# Prefix Traversal Explanation

Prefix means:

```text
product of elements BEFORE current index
```

Input:

```python
nums = [1,2,3,4]
```

Prefix products become:

| Index | Prefix Product |
| ----- | -------------- |
| 0     | 1              |
| 1     | 1              |
| 2     | 2              |
| 3     | 6              |

Explanation:

* before index 0 → nothing exists → 1
* before index 1 → 1
* before index 2 → 1×2 = 2
* before index 3 → 1×2×3 = 6

These values are stored during left-to-right traversal.

---

# Suffix Traversal Explanation

Suffix means:

```text
product of elements AFTER current index
```

Suffix products:

| Index | Suffix Product |
| ----- | -------------- |
| 0     | 24             |
| 1     | 12             |
| 2     | 4              |
| 3     | 1              |

The important realization:

```text
Backward traversal transforms future values
into already-known accumulated computation.
```

While moving from right to left:

* right-side multiplication is already known
* reusable multiplication state is preserved
* repeated computation is avoided

This is why suffix traversal happens backward.

---

# Optimized Solution

```python
class Solution:

    def productExceptSelf(self, nums):

        n = len(nums)

        result = [1] * n

        prefix = 1

        # Prefix traversal
        for i in range(0, n):

            result[i] = prefix

            prefix *= nums[i]

        suffix = 1

        # Suffix traversal
        for i in range(n - 1, -1, -1):

            result[i] *= suffix

            suffix *= nums[i]

        return result
```

---

# Walkthrough

Input:

```python
nums = [1,2,3,4]
```

---

## Prefix Pass

Initially:

```python
result = [1,1,1,1]
```

After prefix traversal:

```python
[1,1,2,6]
```

Each index now stores:

```text
product of left-side elements
```

---

## Suffix Pass

Backward traversal multiplies:

```text
right-side products
```

Final:

```python
[24,12,8,6]
```

---

# Complexity

## Time Complexity

```text
O(n)
```

Two linear traversals only.

---

## Space Complexity

```text
O(1)
```

excluding output array.

No extra prefix/suffix arrays are used.

---

# Where This Pattern Appears

This optimization pattern appears in:

* cumulative calculations
* analytics systems
* report generation
* rolling metrics
* running totals
* precomputed query systems

---

# Real Backend Engineering Example

Imagine an online class leaderboard system.

For every student, the platform wants:

```text
combined score of all OTHER students
```

A slow system would recalculate all scores repeatedly for every student.

Efficient systems instead:

* preserve previous calculations
* reuse cumulative information
* avoid recomputation

This is exactly what prefix and suffix traversal do internally.

---

# Engineering Perspective

This problem teaches an important systems principle:

```text
Fast systems are fast because
they avoid unnecessary repeated work.
```

The optimized solution succeeds because:

* reusable multiplication is preserved
* traversal direction is chosen carefully
* repeated computation is eliminated

This is how scalable systems optimize internally.

---

# DSA Pattern

```text
Prefix / Suffix Computation
```

The algorithm:

* accumulates left-side state
* accumulates right-side state
* combines both efficiently

---

# Takeaway

This problem is not really about multiplication.

It is about:

* reusable computation
* preserved state
* traversal optimization
* scalable system thinking

The biggest realization:

```text
Fast systems often remember useful work
instead of rebuilding it repeatedly.
```
