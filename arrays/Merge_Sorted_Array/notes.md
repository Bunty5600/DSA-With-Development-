Here's the notes.md:

---

# Notes — Merge Sorted Array

## First Thought

My first instinct was copy everything into nums1 and sort it.
It worked. But it felt wrong.
Both arrays were already sorted and I just threw that away.

---

## Main Problem

Brute force didn't respect what the input already gave me.
Sorting from scratch on already-sorted data is wasted effort.
In a real system doing this thousands of times per second — that waste adds up fast.

---

## Optimization Insight

Filling from the back was the shift.

The largest element belongs at the last position.
I already know that. Both arrays are sorted so I can find the largest instantly.
No re-sorting needed. Just compare the two ends and place backward.

The empty zeros weren't padding — they were the space I was supposed to use all along.

---

## DSA Pattern

```
Two Pointer — Backward In-Place Merge
```

Start from the end. Place largest first. Move inward.
Never overwrite what you haven't read yet.

---

## Real Engineering Connection

RocksDB does exactly this during compaction.
Sorted files get merged without re-sorting from scratch.
The entire performance model depends on respecting existing sorted order.
This problem is that — just smaller.

---

## Personal Learning

I realized I was reaching for general tools before asking what the input already gave me.
Both arrays being sorted was not just a constraint — it was the solution.
I didn't need to sort. I needed to merge. Those are different things.

---

**The realization: sorted input is not just a constraint — it's pre-completed work, and throwing it away is the mistake.**

---