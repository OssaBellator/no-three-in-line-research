# Every compatible paid pair has an exact line-clean derangement cylinder

CMR487--CMR491 identify the final mixed-cycle branches as repeated-cell secant
stars and compatible rank-two paid-pair cylinders. The line-clean construction
of CMR330 was introduced for ratio-line pairs, but its exact derangement argument
uses only compatibility of the two fixed cells and nonaxiality of their joining
line. This chapter records that provenance-free form and applies it to both
remaining branches.

Work in a full inherited parent block with `m` source rows and `m` target
columns. Let

\[
Z=\{z_1,z_2\}
\]

be two compatible cells: they use distinct source rows and distinct target
columns. Let `L` be their unique real joining line. Compatibility implies that
`L` is nonaxis. Delete the two used rows and two used columns and put

\[
n=m-2.
\]

The other parent-block cells on `L` form a partial matching in the residual
`K_{n,n}`. Extend that partial matching to a perfect matching `F_L` of the
residual complete bipartite graph. Let

\[
\mathcal D(Z,L)
=
\{\delta\in\operatorname{PM}(K_{n,n}):\delta\cap F_L=\varnothing\}.
\]

## 1. Universal compatible-pair cylinder

### Theorem CMR492 — PROVED

For every compatible pair `Z`,

\[
\boxed{|\mathcal D(Z,L)|=D_n,}
\]

where `D_n` is the derangement number. Every completed parent state

\[
Z\cup\delta,
\qquad
\delta\in\mathcal D(Z,L),
\]

contains the fixed pair and no other parent-block cell of `L`.

For `n\ge2`, the cylinder is nonempty.

### Proof

A nonaxis line meets each source row and each target column in at most one grid
cell. After deleting the endpoints of `Z`, its remaining cells therefore form a
partial matching and may be extended to a residual perfect matching `F_L`.
Relabel `F_L` as the identity. Residual perfect matchings avoiding it are exactly
derangements, giving `D_n` states.

Every remaining parent-block cell of `L` belongs to `F_L`, so every derangement
completion avoids it. The fixed pair is inserted separately. Finally,
`D_n>0` for `n\ge2`. ∎

This is the exact CMR330 cylinder without the ratio-line or old-target
provenance.

## 2. Rank-two-on-the-paid-line elimination

### Corollary CMR493 — PROVED

No candidate-only collinear triple in a completed state from CMR492 contains
both cells of `Z`.

More generally, relative to the paid pair, every candidate-only triple in the
completion has rank zero or rank one. Under the uniform law on
`\mathcal D(Z,L)`, the same derangement atom bounds as CMR332 apply, and the
expected number of candidate-only triples is bounded by the CMR333
rank-zero/rank-one expression with residual side `n`.

### Proof

Any third point collinear with both cells of `Z` lies on their unique joining
line `L`, and CMR492 forbids every other cell of that line. The residual law is
the uniform derangement law after relabelling `F_L`, exactly as in
CMR332--CMR333. ∎

Thus every compatible pair has a completion bank with no rank-two collateral on
its own paid line.

## 3. One rooted secant-star arm is line-cleanable

Let

\[
C=\{a,p_x,p_y\}\in\mathcal R_a
\]

be one boundary-rooted triple from CMR487.

### Theorem CMR494 — PROVED

The pairs

\[
\{a,p_x\}
\qquad\text{and}\qquad
\{a,p_y\}
\]

are compatible. Fix either outside endpoint, say `p_x`, and apply CMR492 on the
rooted line. Every resulting completion

1. contains `a` and `p_x`;
2. omits `p_y` and every other cell on the rooted line;
3. destroys the rooted conflict `C`;
4. creates no candidate-only triple containing both paid cells `a,p_x`.

### Proof

The rooted conflict lies on a candidate-only nonaxis line. Hence its distinct
cells use distinct source rows and distinct target columns, so either displayed
pair is compatible. CMR492 forbids every unprescribed cell of that line,
including `p_y`, and CMR493 eliminates rank-two-on-the-line collateral. ∎

A rooted arm is therefore not merely recognizable as a secant-star arm: it has
an exact line-clean paid-pair bank centered at the same boundary cell.

## 4. Equal-size rooted-arm bank

### Corollary CMR495 — PROVED

Let

\[
A=|\mathcal R_a|.
\]

Choose one outside endpoint from each rooted arm. The resulting family of
line-clean cylinders is an equal-size multiset bank with exactly

\[
\boxed{A D_{m-2}}
\]

state occurrences. Every occurrence destroys its designated rooted arm while
retaining the common boundary cell `a` and eliminating rank-two collateral on
the designated rooted line.

The cylinders need not be disjoint; the statement is an exact equal-weight
multiset bank.

### Proof

CMR487 makes the arms well-defined and outside-pair disjoint. Apply CMR494 to one
chosen endpoint of every arm. CMR492 gives exactly `D_{m-2}` completions for
each choice. Summing cylinder sizes with multiplicity gives the formula. ∎

This is sufficient for averaging arguments: every rooted arm receives the same
completion weight.

## 5. The two-edge bottleneck has the same bank

### Corollary CMR496 — PROVED

Let `Z=\{b_1,b_2\}` be the compatible fixed pair supplied by CMR490 from a
two-edge mixed-cycle bottleneck. Its unique joining line is nonaxis, and CMR492
supplies an exact line-clean cylinder of size

\[
\boxed{D_{m-2}.}
\]

Every completion contains the bottleneck pair, avoids every other cell on its
joining line, and has only rank-zero/rank-one collateral relative to the pair.

This cylinder is an inherited-parent expansion bank. Executing it inside a
restricted tight or residual host still requires the existing reserve,
rollback, or envelope mechanism to make the residual derangement edges
available.

### Proof

Compatibility is CMR490. Apply CMR492--CMR493. The final qualification records
that CMR492 uses the full inherited residual `K_{m-2,m-2}`, not an arbitrary
restricted subhost. ∎

## 6. Revised frontier

The structural splice requested after CMR491 is now exact.

- Every rooted secant-star arm has an equal-size line-clean paid-pair cylinder.
- Every two-edge bottleneck pair has the same universal cylinder.
- Rank-two collateral on the paid line is absent in both cases.
- The only remaining issue is **availability and payment**: lift one of these
  full-parent derangement cylinders through the current envelope or reserve
  without recreating more target load than it destroys.

The next theorem should combine the CMR334 frozen-bank averaging with the
rollback/private-edge ledgers. A successful completion must yield a strict
potential decrease, protected-reserve depletion, a heavy prefix or carry
signature, lower-dimensional host factorization, or envelope expansion.

No all-`n` theorem is claimed. Universal cylinder size, line avoidance, rooted-
arm cleaning, and bottleneck-pair compatibility are checked in
[`scripts/verify_prime_power_universal_compatible_pair_line_clean.py`](../scripts/verify_prime_power_universal_compatible_pair_line_clean.py).
