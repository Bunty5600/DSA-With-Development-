# Best Time to Buy and Sell Stock

## Problem

You are given an array where each element represents the stock price on a specific day.

You must choose:

* one day to buy
* one later day to sell

Return the maximum possible profit.

If no profit is possible, return `0`.

---

# Real Situation

Imagine a real-time stock analytics system.

Prices continuously arrive like this:

```python
[7,1,5,3,6,4]
```

A naive system might compare:

```text
every buy day
with
every future sell day
```

That works for small inputs.

      

But in real systems:

* stock exchanges
* crypto markets
* trading dashboards
* financial analytics engines

millions of price updates arrive continuously.

Rechecking all previous prices repeatedly becomes expensive.

---

# Brute Force

The first idea is usually:

```text
Try every possible pair.
```

Example:

```python
buy at 1 → sell at 5
buy at 1 → sell at 6
buy at 3 → sell at 6
```

This creates nested traversal.

```python
def maxProfit(self, prices):
    n=len(prices)
    max_profit=0
    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
             profit=prices[j]-prices[i]
             max_profit=max(max_profit,profit)
    return max_profit
```      

Time Complexity:

```text
O(n²)
```

Problem:

The system repeatedly recomputes old comparisons.

---

# Better Question

Instead of asking:

```text
"What is the best pair?"
```

Ask:

```text
"What is the cheapest price seen so far?"
```

That changes the entire optimization strategy.

---

# Optimization Insight — Running Minimum

While traversing the array:

* keep track of the minimum price seen
* calculate current possible profit instantly

Formula:

```text
current profit = current price - minimum seen so far
```

This removes unnecessary repeated comparisons.

---

# Optimized Solution

```python
class Solution:
    def maxProfit(self, prices):

        max_profit = 0
        min_price = float("inf")

        n = len(prices)

        for i in range(0, n):

            min_price = min(min_price, prices[i])

            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit
```

---

# Walkthrough

Input:

```python
prices = [7,1,5,3,6,4]
```

Traversal:

| Current Price | Minimum Seen | Profit |
| ------------- | ------------ | ------ |
| 7             | 7            | 0      |
| 1             | 1            | 0      |
| 5             | 1            | 4      |
| 3             | 1            | 2      |
| 6             | 1            | 5      |
| 4             | 1            | 3      |

Maximum profit becomes:

```python
5
```

---

# Complexity

## Time Complexity

```text
O(n)
```

Only one traversal is needed.

---

## Space Complexity

```text
O(1)
```

Only a few variables are stored.

---

# Where This Pattern Shows Up

This optimization pattern appears in:

* stock analytics systems
* streaming dashboards
* metrics aggregation
* monitoring systems
* real-time financial pipelines
* sensor analytics

The core idea is:

```text
Preserve useful state instead of recomputing history.
```

---

# Engineering Perspective

This problem demonstrates an important systems principle:

```text
Fast systems are not fast because they compute more.

They are fast because they avoid unnecessary work.
```

The algorithm succeeds because:

* old prices are not recomputed
* only the most useful historical information is preserved
* the traversal becomes linear

This is how scalable systems think internally.

---

# DSA Pattern

```text
Running Minimum
```

The algorithm continuously tracks the best minimum value while scanning the array once.

---

# Takeaway

This problem is not really about stocks.

It is about learning how systems optimize repeated computation.

The biggest realization:

```text
The full history was never necessary.

Only the most useful state mattered.
```
