# Notes — Two Sum

---

### First Thought

Check every possible pair using nested loops. Works correctly. Easy to understand.

---

### Main Problem

Brute force keeps searching repeatedly.

| Scale      | Result |
|------------|--------|
| Small      | Fine   |
| Large      | Breaks |

At large scale it causes unnecessary CPU work, slower response, and poor scalability.

---

### Optimization Insight

Instead of scanning again and again — store previously seen values and look them up instantly.

```
Repeated Searching  →  Fast Lookup
```

---

### DSA Pattern

**HashMap**

Reach for a HashMap when you see:

- Pair finding
- Repeated searching
- Fast lookup requirement
- Storing previously processed values

---

### Real Engineering Connection

| System                | Why it matters                        |
|-----------------------|---------------------------------------|
| Redis cache           | Retrieve without recalculating        |
| Database indexes      | Skip full table scans                 |
| Authentication        | Fast session and token lookup         |
| Shopping carts        | Instant product matching              |
| Recommendation engine | Quickly match related items           |

---

### Personal Learning

> Optimizations are not about working harder.  
> They are about avoiding unnecessary work completely.

---

### Quick Revision

| Problem  | Pattern | Complexity |
|----------|---------|------------|
| Two Sum  | HashMap | O(n)       |

| Approach    | Time  | Space |
|-------------|-------|-------|
| Brute Force | O(n²) | O(1)  |
| HashMap     | O(n)  | O(n)  |

**Core idea:** Same principle behind backend caching, database indexing, and every high-performance lookup system.