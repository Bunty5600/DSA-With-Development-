# Notes — Product of Array Except Self

## First Thought

At first, I tried multiplying every element except the current one using nested loops.

The logic worked, but the same multiplication was happening repeatedly.

---

# Main Problem

The brute-force solution recomputed products again and again.

Example:

```text id="jlwp01"
3 × 4
```

could be recalculated multiple times for different indexes.

This created unnecessary repeated work.

---

# Optimization Insight

The major realization was:

```text id="jlwp02"
The system can preserve reusable multiplication state.
```

Instead of recalculating everything repeatedly:

* store left-side multiplication
* store right-side multiplication
* combine both

This transformed the solution from repeated computation into reusable computation.

---

# DSA Pattern

```text id="jlwp03"
Prefix / Suffix Computation
```

The algorithm splits the problem into:

* prefix products
* suffix products

Then combines them efficiently.

---

# Real Engineering Connection

This pattern appears in:

* analytics pipelines
* cumulative metrics systems
* distributed processing
* database indexing
* caching systems
* precomputed query engines

Efficient systems avoid recomputing expensive operations repeatedly.

Instead, they preserve reusable state.

---

# Personal Learning

This problem changed how I think about optimization.

The biggest realization was:

```text id="jlwp04"
Direction of traversal matters.
```

Left traversal naturally builds prefix information.

Backward traversal naturally builds suffix information.

The algorithm became fast because it reused stored computation instead of rebuilding it repeatedly.

---

# Final Realization

```text id="jlwp05"
Fast systems are often fast because they remember useful work.
```
