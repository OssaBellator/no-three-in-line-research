# Component-local recleaning for sparse parity cores

`docs/331` verifies bounded owner-sign changes for direct repair through `m=10`,
while the asymptotic `O(log m)` frustration core remains open.  This chapter
gives an exact deterministic reduction for the sign coordinate after one
three-owner rotation.  It does not prove that a useful rotation always exists,
or that owner-Hamming width is uniformly bounded.

## 1. The target boundary system

Let `H=(V,E,sigma)` be a satisfiable signed parity graph, where a clean
orientation `e'` satisfies

```text
e'_u xor e'_v = sigma(uv)
```

on every edge.  Fix a source triple `T` and an orientation vector `e` that
satisfies every edge of the induced graph `H-T`.

Let `C_1,...,C_b` be the connected components of `H-T` having at least one edge
to `T`.  On a connected component `C_j`, every satisfying assignment is either
`e` restricted to `C_j` or its global complement.  Introduce a component-flip
variable `x_j`.  For `t in T`, introduce the owner-flip variable

```text
y_t=e'_t xor e_t.
```

For an edge `tu` with `u in C_j`, impose

```text
y_t xor x_j = sigma(tu) xor e_t xor e_u.
```

For an edge `tt'` inside `T`, impose

```text
y_t xor y_t' = sigma(tt') xor e_t xor e_t'.
```

Call this affine XOR system `B(H,T,e)`.

### Theorem PP3bpr -- PROVED / EXACT COMPONENT-LOCAL RECLEANING

The solutions of `B(H,T,e)` are in bijection with clean orientations of `H`
that agree with `e` on every component of `H-T` not adjacent to `T`.

For a solution `(x,y)`, the corresponding orientation is obtained by:

1. flipping all owner signs in `C_j` when `x_j=1`;
2. flipping the sign of `t in T` when `y_t=1`;
3. leaving every other owner unchanged.

Because `H` is satisfiable, the boundary system is feasible.

#### Proof

The vector `e` satisfies every internal edge of each component of `H-T`.
Connectedness implies that another satisfying assignment on that component is
uniquely either `e` or its complement, giving the variable `x_j`.  Components
not adjacent to `T` have no remaining constraint coupling them to changed
owners, so they may be fixed to `e`.

After this substitution, every unsolved target constraint is either between
`T` and one boundary component or internal to `T`.  Its clean parity equation is
exactly the displayed affine equation.  Thus every boundary-system solution
extends to one clean orientation, and every clean orientation agreeing on the
remote components restricts to one boundary-system solution.

Finally, take any clean orientation of the satisfiable graph `H`.  Its
restriction to each `H-T` component is `e` or its complement, so it supplies a
solution after remote components are normalized to `e`. ∎

## 2. Exact criterion for changing only the rotated owners

### Corollary PP3bps -- PROVED / `T`-ONLY SIGN-REPAIR CRITERION

There is a clean target orientation agreeing with `e` outside `T` if and only if
`B(H,T,e)` remains feasible after fixing

```text
x_1=...=x_b=0.
```

When this holds, the minimum owner-Hamming sign change is at most three and is
the minimum Hamming weight of the three variables `y_t` over that reduced
system.

#### Proof

Fixing every component flip to zero is exactly the requirement that all owners
outside `T` retain their signs.  PP3bpr then gives the equivalence. ∎

This is the structural condition verified exhaustively at `m=10` in `docs/331`
for a suitable direct clean rotation, where at most two of the three `y_t`
variables are needed.

## 3. Connection to a successor rotation

Suppose `e` is an orientation of a source parity graph and a successor rotation
changes targets only on `T`.  By owner-support locality in `docs/338`, every
parity edge disjoint from `T` is unchanged.

### Corollary PP3bpt -- PROVED / COVERED-VIOLATION RECLEANING

If every parity edge violated by `e` in the source graph meets `T`, and the
target parity graph `H` is satisfiable, then `e` satisfies `H-T`.  Therefore the
complete target recleaning problem is exactly `B(H,T,e)`.

#### Proof

Every source edge disjoint from `T` is satisfied by the hypothesis.  Such an
edge and its signed predicate are unchanged by the rotation, so it remains
satisfied in the target.  Apply PP3bpr. ∎

Thus a three-owner vertex cover of the current violated-edge set is sufficient
to reduce the entire sign update to the boundary system.  The result does not
assert that every sparse frustration core has such a cover.

## 4. Polynomial recleaning for logarithmic parity graphs

Let `q=|E(H)|`.  The number `b` of boundary components is at most the number of
edges from `T` to `V\T`, hence at most `q`.

### Theorem PP3bpu -- PROVED / SPARSE-CORE EXACT ALGORITHM

Under the hypotheses of PP3bpr, a minimum owner-Hamming clean target can be
found by enumerating at most

```text
2^(|T|+b) <= 2^(3+q)
```

boundary assignments.  The exact cost of a solution is

```text
sum_(j:x_j=1) |C_j| + sum_(t in T) y_t.
```

In particular, when `q=O(log m)`, exact component-local recleaning is computable
in polynomial time.

#### Proof

PP3bpr reduces every admissible clean target to `|T|+b` binary variables with
explicit affine constraints.  Enumerate all assignments, reject those violating
an equation, and minimize the displayed owner-Hamming cost.  Since `|T|=3` and
`b<=q`, the stated bound follows.  If `q<=C log_2 m`, the enumeration has at most
`8m^C` assignments. ∎

The same enumeration can minimize component-root flips instead of owner Hamming,
or sample exactly from any prescribed weight on feasible boundary solutions.

## 5. Revised local-sign frontier

The sign-coordinate problem now separates into two questions.

1. **Existence of a useful cycle move:** find a pair-safe or clean successor
   rotation whose source triple covers the relevant violated edges, or otherwise
   arrange a sequence with controlled uncovered residue.
2. **Recleaning after that move:** solve the exact boundary XOR system.  For an
   `O(log m)` parity graph this step is already polynomial and changes no remote
   component.

A bounded number of owner-sign changes requires more than sparsity: one must
show that the reduced system has a low-cost solution, ideally with every
`x_j=0`.  Large boundary components are the remaining possible Hamming
obstruction.  Nevertheless the recleaning search itself no longer requires a
global `2^m` orientation optimization.

The next theorem identifier after this chapter is `PP3bpv`.
