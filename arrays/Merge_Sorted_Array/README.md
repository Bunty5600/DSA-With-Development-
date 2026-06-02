Here's the README:

---

# Merge Sorted Array

## Problem

You are given two sorted arrays — `nums1` and `nums2`.

```python
nums1 = [1, 2, 3, 0, 0, 0]   # m = 3 real elements, rest are empty slots
nums2 = [2, 5, 6]             # n = 3 elements
```

The zeros at the end of `nums1` are not real values. They are reserved space.

Your job is to merge both arrays into `nums1` itself — sorted, in-place, without returning anything new.

Expected result inside `nums1`:

```python
[1, 2, 2, 3, 5, 6]
```

Simple to read. Surprisingly deep to optimize correctly.

---

## Real World Situation

Imagine you are building a **log aggregation system** for a distributed backend.

You have two servers. Each server produces logs continuously — and each server's logs are already sorted by timestamp.

```
Server A logs:  [10:01, 10:03, 10:07]
Server B logs:  [10:02, 10:05, 10:09]
```

Your system needs to merge these into a single sorted timeline — so monitoring dashboards, alerting systems, and debugging tools see one clean unified stream.

Now scale that up.

Thousands of servers. Millions of log entries per minute. Each batch already sorted internally.

If your merge operation is inefficient — sorting from scratch every time, allocating new memory for every merge — the system starts falling behind the live stream. Dashboards lag. Alerts fire late. Debugging becomes impossible.

This is exactly the engineering problem hiding inside this LeetCode problem.

The question is not just *"how do I merge two arrays?"*

The question is *"how do I merge two already-sorted arrays without wasting the structure they already have?"*

---

## Brute Force

The first instinct is straightforward.

Copy `nums2` into the empty slots at the end of `nums1`. Then sort the whole thing.

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
```

**What is happening internally:**

- Elements of `nums2` are placed into the tail of `nums1` starting at index `m`
- The entire array is then sorted using Python's built-in sort

**Does it work?** Yes. Completely correct output.

**Time Complexity: O((m+n) log(m+n))** — the sort step dominates everything.

**Space Complexity: O(1)** — no extra array allocated.

---

## Main Problem in Brute Force

Here is the real issue.

Both arrays came in already sorted. That is valuable structural information.

The brute force solution throws that away completely.

The `.sort()` call does not know or care that the data was already partially ordered. It treats the entire array as random and starts from scratch. All the work that went into sorting these arrays originally — wasted.

In a real system, this compounds fast.

If you are merging sorted log batches from 500 servers every second, and every merge triggers a full re-sort, your pipeline is doing an enormous amount of repeated, unnecessary computation — work that could be avoided entirely if you respected the structure that already existed.

The brute force works on small inputs. It breaks down at scale.

---

## Better Question

Instead of asking:

> *"How do I sort this merged array?"*

Ask:

> *"Both arrays are already sorted. What can I use from that?"*

The largest element in the final merged result belongs at the last position.

The second largest belongs at the second last position.

And so on.

You already know where things should end up. You just need to figure out which element is the largest at each step — and both arrays are sorted, so comparing the last elements of each gives you that answer immediately.

This one question changes the entire strategy.

---

## Optimization Insight — Fill From the Back

Use three pointers:

```
p1  →  last real element in nums1   (index m - 1)
p2  →  last element in nums2        (index n - 1)
p   →  last position in nums1       (index m + n - 1)
```

At every step:

- Compare `nums1[p1]` and `nums2[p2]`
- Place the larger one at `nums1[p]`
- Move that pointer one step left
- Move `p` one step left

Repeat until `nums2` is fully merged.

Why fill from the back?

Because `nums1` already has reserved space at the tail. If you tried to fill from the front, you would overwrite real elements in `nums1` before you had a chance to read them. Filling from the back uses the empty space that was always there — without touching anything that hasn't been placed yet.

No extra memory. No overwriting conflicts. No wasted comparisons.

The reserved zeros were not useless padding. They were the solution space the whole time.

---

## Optimized Solution

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
```

**Internal movement:**

- `p1` moves left through real elements of `nums1`
- `p2` moves left through `nums2`
- `p` moves left filling positions from the end
- Loop ends when `nums2` is exhausted — anything remaining in `nums1` is already in place

---

## Walkthrough

```python
nums1 = [1, 2, 3, 0, 0, 0]    m = 3
nums2 = [2, 5, 6]              n = 3
```


p1 = 2 (value 3)   p2 = 2 (value 6)   p = 5
→ 6 > 3 → place 6 at index 5
→ nums1 = [1, 2, 3, 0, 0, 6]

p1 = 2 (value 3)   p2 = 1 (value 5)   p = 4
→ 5 > 3 → place 5 at index 4
→ nums1 = [1, 2, 3, 0, 5, 6]

p1 = 2 (value 3)   p2 = 0 (value 2)   p = 3
→ 3 > 2 → place 3 at index 3
→ nums1 = [1, 2, 3, 3, 5, 6]

p1 = 1 (value 2)   p2 = 0 (value 2)   p = 2
→ equal → place nums2's 2 at index 2
→ nums1 = [1, 2, 2, 3, 5, 6]

p2 < 0 → loop ends
```

**Final result: `[1, 2, 2, 3, 5, 6]`** ✓

One pass. No sort. No extra memory.

---

## Complexity

| What | Brute Force | Optimized |
|------|-------------|-----------|
| Time | O((m+n) log(m+n)) | O(m+n) |
| Space | O(1) | O(1) |

The optimized solution visits every element exactly once. No element is compared more than necessary. The sorted structure of both arrays is fully respected and used.

---

## Where This Pattern Appears

This two-pointer backward merge pattern is not just a LeetCode trick. It shows up in serious engineering contexts:

- **Log aggregation pipelines** — merging sorted log streams from multiple servers into a unified timeline
- **Database merge operations** — merging sorted index segments during compaction in systems like LevelDB and RocksDB
- **External sorting** — merging pre-sorted chunks back together during large-scale data processing
- **Time-series databases** — merging sorted metric batches from distributed collectors
- **Search engine index merging** — combining sorted posting lists during index updates
- **Memory-constrained embedded systems** — anywhere heap allocation is expensive or forbidden

The pattern is always the same: two sorted sources, one destination, use the structure that already exists.

---

## Real Backend Engineering Example

**RocksDB — LSM Tree Compaction**

RocksDB is the storage engine used inside systems like Cassandra, MySQL, and dozens of other production databases.

It uses a structure called an LSM Tree — Log Structured Merge Tree.

When data is written, it goes into small sorted files called SSTables. Over time, multiple SSTables accumulate. To keep reads fast, RocksDB periodically merges these sorted files together into larger sorted files — a process called compaction.

That merge is essentially this exact algorithm running at massive scale.

During compaction, RocksDB does not re-sort from scratch. It walks through multiple sorted files simultaneously using pointer-based traversal, picking the smallest element at each step and writing it forward.

If it sorted from scratch every time, compaction would be catastrophically slow. The entire performance model of LSM-based storage depends on respecting existing sorted order and merging efficiently.

What you just solved is the conceptual foundation of how production storage engines work internally.

---

## Engineering Perspective

This problem teaches something that goes beyond arrays.

When a system receives already-structured data and destroys that structure to recompute it from scratch — that is waste. Pure waste. And in high-throughput systems, waste compounds until the system can no longer keep up.

The brute force solution is not wrong. It is just unaware.

It does not ask what it already knows. It does not look at the input and recognize that half the work has already been done. It reaches for a general tool — `.sort()` — when a specific, more efficient tool was available.

The optimized solution asks a better question first.

> *"What structure already exists here, and how can I use it?"*

That question — asked before writing a single line of code — is the difference between a system that handles 10,000 requests per second and one that handles 10.

Scalable systems are not built by working harder. They are built by recognizing what work can be avoided entirely.

---

## DSA Pattern

```
Two Pointer — Backward In-Place Merge
```

When merging two sorted sequences into pre-allocated space, traverse from the end. Use the largest unplaced elements first. Avoid overwriting unread data by moving into empty space before touching real elements.

Core properties of this pattern:
- Requires pre-allocated destination space
- Both input sequences must be sorted
- Single pass, O(m+n) time
- Zero extra memory

---

## Takeaway

This problem is not really about merging arrays.

It is about learning to read the structure of your input before deciding how to process it.

Both arrays were sorted. That was a gift. The brute force solution ignored it. The optimized solution built everything on top of it.

The biggest realization:

> **The empty space at the end of nums1 was never padding. It was the answer. The sorted order was never a constraint. It was the optimization.**

That is how scalable systems think. Not "how do I solve this?" but "what do I already have, and how far can it take me?"

---