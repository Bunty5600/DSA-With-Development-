# Notes — Best Time to Buy and Sell Stock

## First Thought

At first, I thought we needed to compare every buy day with every future sell day.

That approach worked logically, but it felt inefficient because the system repeatedly checked old prices again and again.

---

# Main Problem

The brute-force solution wastes time recomputing history.

For every current price, the algorithm rechecks previous prices repeatedly.

This creates unnecessary work.

---

# Optimization Insight

The important realization was:

```text id="z3fjlwm"
The system does not need all previous prices.

It only needs the minimum price seen so far.
```

Once the minimum value is preserved, profit can be calculated instantly during traversal.

---

# DSA Pattern

```text id="b9z3h4"
Running Minimum
```

The algorithm continuously carries forward the best minimum state while scanning the array once.

---

# Real Engineering Connection

This pattern appears in:

* stock monitoring systems
* live analytics dashboards
* streaming data pipelines
* real-time metrics aggregation

Real systems avoid recomputing full history repeatedly.

Instead, they preserve only the most useful state.

---

# Personal Learning

This problem changed how I think about optimization.

Optimization is often not about faster computation.

It is about avoiding unnecessary computation completely.

The biggest insight:

```text id="6r5byz"
History was compressed into one useful value.
```
