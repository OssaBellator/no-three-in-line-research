# Residue-corrected marker-flow schedules

`docs/501` gives an exact Euler circuit when the requested marker flow has a
common rational period. `docs/507` quantizes mixtures of several marker cycles.
A finite construction must also handle lengths that are not multiples of the
chosen period. This chapter reduces every such length to a finite table of
residue correctors.

Let `G` be a finite directed marker-state graph with a distinguished base state
`o`. Every edge has a rational output vector `v_e` and a rational scalar cost
`c_e`. Let `W` be a based closed walk of length `P`, total vector `v(W)`, and
mean `mu=v(W)/P`.

## 1. Finite residue correction

### Theorem PP3cjr -- PROVED / RESIDUE-CORRECTED PERIODIC REALIZATION

Suppose that for every attainable residue `r mod P` there is a based closed walk
`R_r` whose length `ell_r` is congruent to `r mod P`. Then every sufficiently
large attainable length `N` has the deterministic realization

```text
R_r W^q,   q=(N-ell_r)/P.
```

Its average output obeys

```text
average(R_r W^q)-mu = [v(R_r)-ell_r mu]/N.
```

Thus one finite residue table gives an explicit `O(1/N)` error bound in every
protected coordinate.

#### Proof

Choose `r=N mod P`. Once `N>=ell_r`, the integer `q` is nonnegative. Both
`R_r` and `W` start and end at `o`, so they concatenate. Subtracting `N mu`
from the total vector cancels the `q` copies of `W` and leaves exactly the
displayed residue excess. ∎

## 2. Exact minimum-cost residue table

### Theorem PP3cjs -- PROVED / REDUCED-COST RESIDUE ORACLE

Assume that `W` has minimum scalar mean `gamma=c(W)/P`. Give every edge reduced
cost

```text
c'_e = c_e-gamma.
```

The minimum reduced cost of a based closed walk in each residue class is an
ordinary shortest-path problem on the finite expanded graph

```text
V(G) x Z/PZ.
```

If `R_r` is a minimum reduced-cost corrector for residue `r`, then for every
sufficiently large `N congruent r mod P`, the walk `R_r W^q` is a minimum-cost
based closed walk of length `N`.

#### Proof

Minimum cycle mean implies that the expanded graph has no negative reduced-cost
cycle. Hence a shortest based return to `(o,r)` exists and may be chosen after
deleting nonnegative repeated cycles. Any length-`N` closed walk has residue
`r` and reduced cost at least that of `R_r`. Adding copies of `W` changes length
by `P` and reduced cost by zero, so the lower bound is attained for all large
enough lengths. ∎

## 3. Stored exact fixture

### Theorem PP3cjt -- PROVED / THREE-RESIDUE MARKER AUDIT

The audit `scripts/check_marker_residue_correctors.py` uses a critical
three-edge marker cycle `ABC`, each edge of scalar cost one, and a based
one-edge correction loop `D` of scalar cost two. For

```text
N=3q+r,  r in {0,1,2},
```

the exact optimum is

```text
D^r (ABC)^q,
```

with total cost `N+r`, residue costs `(0,2,4)`, and action-rate error at most
`2/N`. Exhaustive integer decomposition verifies every length through 120.

## 4. Prime-patching consequence

A periodic marker controller no longer requires a divisibility assumption on
the ambient patch length. One finite residue graph supplies deterministic
all-length schedules, exact scalar optimality, and explicit vanishing output
error.
