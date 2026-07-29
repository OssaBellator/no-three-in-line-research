# Edge-colored private-petal banks inside Hall rectangles

`docs/436` extracts one residual matching after conditioning on a common Hall
target core.  This chapter decomposes the entire residual incidence graph into
private-marker banks.  The key input is the exact edge-coloring theorem for
bipartite graphs.

## 1. Residual graph after a common core

Let `F` be a source family sharing a target core `C`.  Delete the core edges and
write `G_R` for the residual bipartite graph.  Put

```text
Delta_R=max(max_x d_R(x), max_y m_R(y)).
```

Every residual edge is a candidate private marker action attached to the common
core.

### Theorem PP3cbm -- PROVED / BIPARTITE PRIVATE-PETAL COLORING

The residual edge set decomposes into at most `Delta_R` matchings.
Equivalently, all core-plus-marker actions split into `Delta_R` banks in which
both sources and private targets are pairwise distinct.

#### Proof

Add dummy vertices and dummy edges until the bipartite graph is
`Delta_R`-regular.  Hall's theorem gives a perfect matching.  Remove it and
repeat; regularity drops by one at every step.  After `Delta_R` steps all edges
have been partitioned into matchings.  Deleting dummy edges gives the desired
coloring of the original residual graph. ∎

## 2. A large private-marker bank

### Corollary PP3cbn -- PROVED / FULL-EDGE BANK PIGEONHOLE

If `E_R` is the number of residual edges, one private-marker bank contains at
least

```text
ceil(E_R/Delta_R)
```

core-plus-marker actions.

More generally, for nonnegative residual edge weights of total mass `W_R`, one
bank has weight at least `W_R/Delta_R`.

#### Proof

Apply the pigeonhole principle to the `Delta_R` color classes from `PP3cbm`. ∎

This improves the one-shot greedy denominator `D+Delta-1` from `docs/436` to the
sharp bipartite degree denominator `Delta_R`, while simultaneously scheduling
every residual action.

## 3. Kernel interface

Assume every colored edge has at least `q` clean local continuations, each final
target identifies its edge color, and within one color a target has predecessor
multiplicity at most `h`.

### Theorem PP3cbo -- PROVED / COLORED CORE-PETAL KERNEL

The union of all colored core-plus-petal banks has reverse load at most

```text
h/q.
```

If the color is not intrinsically retained and one final target is compatible
with at most `g` colors, the bound becomes `gh/q`.

#### Proof

Within one color, matching disjointness and the assumed continuation bounds give
load `h/q`.  Intrinsic color recovery makes the target supports disjoint across
colors.  Without recovery, at most `g` color loads can add at one target. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_hall_core_petal_edge_coloring.py
```

The script exhausts every `3 x 4` residual rectangle in which each source has at
least two residual neighbors, constructs an exact `Delta_R`-edge-coloring, and
checks the complete partition and largest-bank bound.

The next theorem identifier after this chapter is `PP3cbp`.
