# Notes — Remove Duplicates from Sorted Array

---

## First Thought

My first idea was:

* create another array
* manually copy only unique values

Simple and easy to understand.

---

## Main Problem

The brute-force solution:

* creates extra memory
* copies values again
* stores temporary duplicate data

At scale, this increases:

* memory usage
* storage overhead
* processing cost

---

## Optimization Insight

The array is already sorted.

That means duplicates are always adjacent:

```text id="5x5u67"
[1,1,2,2,3,4,4]
```

Instead of creating another array:

* overwrite duplicates directly
* reuse existing memory space

This becomes:

```text id="axl7wn"
In-Place Optimization
```

---

## DSA Pattern

Two Pointers

### Pattern Clues

* sorted array
* duplicate removal
* in-place modification
* constant memory requirement

---

## Real Engineering Connection

This same idea appears in:

* database cleanup
* analytics preprocessing
* log compaction
* cache optimization
* streaming systems

---

## Personal Learning

Not all optimizations focus on speed.

Some optimizations mainly focus on:

* reducing memory usage
* avoiding redundant storage
* reusing existing memory efficiently
