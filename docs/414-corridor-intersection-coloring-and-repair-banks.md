# Corridor intersection coloring and repair banks

`docs/408` localizes every fixed dyadic support-chord type to a short union of
two Hamilton-cycle arcs and gives a hub-or-disjoint-bank alternative.  This
chapter colors the entire corridor intersection graph.  A bounded cycle-vertex
load decomposes all states, not merely one extracted subfamily, into a bounded
number of vertex-disjoint banks.

The statements are combinatorial.  They do not construct the repair word used
inside one bank.

## 1. Corridor intersection degree

Let `C_1,...,C_N` be nonempty subsets of a cycle vertex set.  Assume

```text
|C_i|<=s
```

and define the maximum vertex load

```text
Delta=max_v #{i:v in C_i}.
```

Let `G_C` be the graph on the corridors, joining two corridors when they share a
cycle vertex.

### Theorem PP3byf -- PROVED / CORRIDOR INTERSECTION DEGREE BOUND

Every corridor vertex of `G_C` has degree at most

```text
s(Delta-1).
```

Consequently

```text
chi(G_C)<=s(Delta-1)+1.
```

#### Proof

Fix a corridor `C_i`.  For each of its at most `s` cycle vertices, at most
`Delta-1` other corridors contain that vertex.  Summing these incidences gives
at most `s(Delta-1)` intersecting corridors; duplicates only reduce the number
of distinct neighbours.  Greedy coloring then uses at most one more color than
the maximum degree. ∎

Each color class is a bank of pairwise vertex-disjoint corridors.

## 2. Weighted bank decomposition

Give corridor `C_i` a nonnegative weight `w_i` and let

```text
W=sum_i w_i.
```

### Theorem PP3byg -- PROVED / COMPLETE WEIGHTED CORRIDOR-BANK PARTITION

The corridor family can be partitioned into at most

```text
s(Delta-1)+1
```

pairwise vertex-disjoint banks.  One bank has total weight at least

```text
W/[s(Delta-1)+1].
```

For the unweighted family, one bank has size at least

```text
ceil(N/[s(Delta-1)+1]).
```

#### Proof

Use the coloring from `PP3byf`.  The color classes partition the corridors and
therefore their total weights sum to `W`.  Pigeonhole the largest class. ∎

Unlike a one-shot greedy extraction, this retains every corridor and assigns it
to a reusable disjoint bank.

## 3. Dyadic support-chord specialization

For one dyadic support-chord type with indices `j_A,j_B`, `docs/408` gives
corridors of size at most

```text
s_tau=2^(j_A+1)+2^(j_B+1).
```

### Corollary PP3byh -- PROVED / DYADIC TYPE BANK NUMBER

If the maximum cycle-vertex load inside this type is `Delta_tau`, then all
states of the type split into at most

```text
s_tau(Delta_tau-1)+1
```

vertex-disjoint corridor banks.

Hence one weighted bank carries at least the reciprocal fraction

```text
1/[s_tau(Delta_tau-1)+1]
```

of the total type weight.

#### Proof

Insert the dyadic corridor-size bound into `PP3byg`. ∎

This supplies a direct interface to the typed-kernel calculus.  Each bank may be
assigned a petal- or corridor-marked target reservoir; the number of banks is
controlled by local cycle load rather than by the total number of support
states.

## 4. Finite diagnostic

Run

```bash
python scripts/check_corridor_intersection_coloring.py
```

The checker constructs every dyadic support-chord corridor through cycle length
twelve, greedily colors each type, and verifies the degree, color-count,
weighted-bank, and unweighted-bank bounds.

The next theorem identifier after this chapter is `PP3byi`.
