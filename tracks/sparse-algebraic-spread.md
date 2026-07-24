# Sparse algebraic perfect-matching spread

**Branch:** `research/sparse-algebraic-spread`

This independent track seeks an `O(1/d)`-spread perfect-matching measure in sparse algebraic candidate hosts of degree `d=o(N)`. It is separate from dense superregular resampling because the switching geometry and mixing scale are different.

## Motivation and proved baseline

In a dense superregular graph, six-cycle switching gives `O(1/N)` cylinder probabilities. A bounded-hyperbola or algebraic candidate universe may have local degree `d` much smaller than `N`. The desired analogue is

\[
\Pr(F\subseteq M)\le\left(\frac Kd\right)^{|F|}
\]

for every compatible partial matching `F`.

Spread alone will provide a global conflict-mass endpoint; an additional resampling theorem would be needed for a local-load endpoint.

## SAS1 — Sparse host hypotheses

### Target statement

Identify explicit, checkable hypotheses on a balanced bipartite graph `G` of degree about `d` that are satisfied by the intended algebraic hosts and exclude forced edge correlations. Candidate hypotheses should include:

1. minimum degree at least `(1-epsilon)d`;
2. Hall expansion for all sets up to size `N/2`;
3. bounded pair codegree and bounded short-cycle concentration;
4. robust alternating-path expansion after deleting `O(1)` vertices and edges;
5. at least `c d^{2l-1}` alternating cycles of one bounded odd half-length `l` through every matching edge, with controlled reverse multiplicity.

The hypotheses must be strong enough to imply a perfect matching and stable under deleting one previously sampled perfect matching.

### Explicit sparse block host

[`sparse-block-host-spread.md`](sparse-block-host-spread.md) proves SAS1a
and SAS4b for

\[
G_{b,d}=\bigsqcup_{\ell=1}^b K_{d,d}.
\]

Independent uniform block permutations have all-rank \((3/d)\)-spread.
After deleting the first matching, independent uniform derangements have
conditional all-rank \((9/d)\)-spread, so the two-layer union is a simple
saturated 2-factor with \((18/d)\)-spread. This resolves the measure and
deletion-stability parts of SAS1--SAS4 for a concrete \(d=o(N)\) host
family. It does not supply the SAS5 geometric triple count.

### Checkable sufficient switching hypothesis

[`sparse-four-cycle-switching.md`](sparse-four-cycle-switching.md)
identifies one explicit sufficient condition: every matching containing an
edge `e` has at least `L=Omega(d)` alternating four-cycle switches removing
`e`, uniformly after the required bounded vertex deletions. This condition
is not necessary—high-girth hosts require the longer-cycle alternative in
the original SAS1 docket.

## SAS2 — Sparse switching ratio

### Target statement

For a uniform or explicitly weighted perfect matching `M` of `G`, and any edge `e`, construct alternating-cycle switchings with

\[
\frac{\#\{\text{forward switches removing }e\}}
{\max_{M'\not\ni e}\#\{\text{reverse descriptions into }M'\}}
\ge c d.
\]

Consequently

\[
\Pr(e\in M)\le\frac C d.
\]

The proof may use longer alternating cycles, expansion of a matching-switch chain, or permanent ratios.

### Four-cycle case proved

The switching note proves SAS2a: the four-cycle forward descriptions have
reverse multiplicity at most one, so a uniform lower bound `L` gives
`Pr(e in M)<=1/(L+1)`. In particular `L+1>=cd` gives the requested
`O(1/d)` estimate. Longer-cycle hosts remain open.

[`sparse-general-switching-ratio.md`](sparse-general-switching-ratio.md)
proves SAS2b for arbitrary labelled alternating-cycle descriptions. If
every matching containing \(e\) has at least \(L\) forward descriptions
and every avoiding matching has at most \(R\) reverse descriptions, then
\(\Pr(e\in M)\leq R/(L+R)\). The conditioned SAS3c version is identical
on the residual matching space. Thus longer-cycle hosts now require only
the host-specific ratio \(L/R=\Omega(d)\), including deletion stability;
injective reverse switching is not required.

## SAS3 — Fixed-rank and all-rank spread

### Target statement

For every fixed `s`, conditioning on a prescribed matching of at most `s-1` edges preserves the hypotheses of SAS1 with controlled loss. Hence

\[
\Pr(F\subseteq M)\le(C/d)^{|F|}
\]

for `|F|<=s`.

The stronger target is an all-rank distribution satisfying the same bound for every matching `F`.

Rank three is sufficient for duplicate-cell and collinear-triple conflicts; all-rank spread is useful for containers and robust thresholds.

SAS3b proves the same edge bound after conditioning on a partial matching
whenever the residual graph retains the four-cycle hypothesis. Combined
with SAS3a, bounded-rank spread is therefore complete for this host class.
SAS3c gives the corresponding conclusion for any labelled longer-cycle
family whose forward/reverse ratio survives the same deletion.

### Proved composition component

[`sparse-spread-composition.md`](sparse-spread-composition.md) proves SAS3a:
the required conditional one-edge estimate through rank `s-1` implies
rank-`s` spread by the chain rule. The remaining task is to derive that
conditional estimate from SAS1 after the prescribed vertices and edges are
deleted.

## SAS4 — Two-layer sparse spread

### Target statement

After sampling `M_1`, prove that `G-M_1` retains the sparse-host hypotheses and sample `M_2` with conditional `O(1/d)` spread. Then for every edge set `F`,

\[
\Pr(F\subseteq M_1\cup M_2)\le(2C/d)^{|F|}.
\]

The union is a simple 2-factor with exact row and column degree two.

### Spread conclusion proved

The composition note proves the displayed `(2C/d)^|F|` inequality for
every edge set and the exact simple-2-factor conclusion, assuming the
second layer has conditional `C/d` spread after `M_1`. Thus the sole
remaining SAS4 issue is the host-stability/measure construction needed to
supply that conditional hypothesis.

SAS4b supplies that construction explicitly for the sparse block host,
using the exact derangement space after the first matching is deleted.

## SAS5 — Geometric conflict endpoint

### Target statement

For a sparse algebraic candidate host `G`, prove either:

\[
\sum_{C\in\mathcal C}(2C/d)^{|C|}<1,
\]

or an appropriate local-load/resampling upgrade. Deduce a saturated no-three-in-line selection in `G`.

The global triple criterion is

\[
T(G)<c d^3.
\]

A successful host must therefore combine sparse spread with a genuinely small geometric triple count.

### Abstract endpoint proved

The composition note proves the conflict-family union-bound theorem and
the explicit triple threshold

`T(G) < d^3/(2C)^3`.

SAS5 remains open only in its host-specific part: constructing an intended
algebraic host satisfying this count (or proving a local resampling
upgrade).

The consecutive sparse block host cannot supply that missing part.
[`sparse-block-host-geometric-obstruction.md`](sparse-block-host-geometric-obstruction.md)
proves

\[
T(G_{b,d})\geq \frac{N(d-1)(d-2)}6=\omega(d^3)
\]

when \(d=o(N)\). Thus SAS1a/SAS4b remain useful matching-measure models,
but the global SAS5 endpoint requires a different embedding, a different
host, or a local-load theorem.

[`sparse-block-affine-energy.md`](sparse-block-affine-energy.md) proves
SAS5c, the exact internal triple formula for an arbitrary complete block
\(R\times C\):

\[
T_{\rm int}(R,C)
=
\sum_\lambda A_R(\lambda)
\bigl(A_C(\lambda)+A_C(1-\lambda)\bigr).
\]

This turns the internal part of SAS5 into a checkable one-dimensional
shape-energy condition. It also extends the obstruction: if the row and
column sets of each block are affine images of one another, every block
contains at least \(\binom d3\) compatible triples, so the same
\(N(d-1)(d-2)/6\) lower bound holds. A viable block embedding must use
shape-incompatible row and column sets in almost all blocks and must
separately control triples meeting multiple blocks.

[`sparse-zero-energy-blocks.md`](sparse-zero-energy-blocks.md) proves
SAS5d, showing that the internal obstruction can be eliminated rather
than merely reduced. For every \(d\)-element row set \(R\), a greedy
integer column set \(C\) in a coordinate interval of length \(O(d^6)\)
satisfies

\[
T_{\rm int}(R,C)=0.
\]

It avoids every row shape and its reflection in the column shape
histogram. Thus the remaining block-host geometry is entirely the common
coordinate budget and the triples meeting multiple blocks.

[`sparse-expanded-grid-zero-conflict.md`](sparse-expanded-grid-zero-conflict.md)
proves SAS5e by coordinating all block columns at once. A greedy
construction places the \(N\) column vertices in an interval of length
\(O(d^3N^3)\) so that the whole block host, including cross-block
interactions, has no compatible collinear triple. Combined with
SAS1a/SAS4b this is a deterministic no-conflict endpoint in the expanded
rectangular embedding. The remaining block-host obstruction is now
exactly coordinate compression into the standard \(N\)-column interval;
arbitrary relabelling would not preserve collinearity.

[`sparse-balanced-compression-energy.md`](sparse-balanced-compression-energy.md)
proves SAS5f, an exact standard-grid formulation. Assigning the \(N\)
column coordinates to \(b\) labels with multiplicity \(d\) each gives a
balanced \(3\)-CSP whose energy is exactly \(T(G)\). If
\(A_3,A_{21},A_{111}\) count full-grid affine triples by row-block
multiplicity, a uniformly balanced assignment has mean

\[
\frac{A_3(d)_3+A_{21}(d)_2d+A_{111}d^3}{(N)_3}.
\]

This gives a deterministic conditional-expectation embedding at most
that mean and a checkable sufficient condition for the SAS5a threshold.
It also shows that the remaining compression step needs structured
arithmetic colouring when the balanced-random benchmark is too large.

The same note proves SAS5g and makes that deterministic claim fully
explicit. For every partial balanced assignment, the conditional
potential is a sum of multivariate hypergeometric terms
\(\prod_\ell(r_\ell)_{u_\ell}/(R)_u\). Its remaining-capacity-weighted
average over the next label equals the current potential. Greedy
minimization therefore constructs a balanced map attaining the SAS5f
mean bound, and an initial potential below one yields zero conflicts
exactly. The remaining arithmetic frontier is to choose a row partition
whose initial benchmark already meets the endpoint, or to introduce a
stronger structured potential.

SAS5h adds a balance-preserving local decoder after that construction.
An improving cross-label column swap lowers the exact energy. If no such
swap exists, every surviving conflict forces enough one- or two-literal
near-conflicts to satisfy
\[
dN_1+N_2\geq(3(N-d)-3)T(G_\kappa).
\]
Thus a nonzero local minimum returns a quantified correction bank rather
than an unclassified colouring. The remaining arithmetic task is to
batch those corrections or classify their repeated column/label
patterns.

SAS5i concentrates that correction bank. At a positive swap-local
minimum, some cross-label column pair destroys at least
\[
\frac{2(3(N-d)-3)T(G_\kappa)}{N(N-d)}
\]
current conflicts, and local minimality forces the same swap to create
at least as many from repairable near-conflicts. The residual
classification may therefore target high-load two-column/label
patterns, rather than a diffuse global near-conflict count.

## Intended host families

- bounded unions of modular-hyperbola orbit states;
- subgroup-coset absorber universes;
- algebraic candidate graphs generated by a bounded set of rational maps;
- pseudorandom restrictions of a dense superregular host.

## Falsification programme

- enumerate sparse regular bipartite graphs with forced opposite edges;
- test whether bounded codegree alone fails SAS2;
- measure alternating-cycle counts through edges in the algebraic hosts;
- compute exact permanent ratios for small primes;
- test stability after deleting one perfect matching.

`scripts/verify_sparse_switching.py` retains both the exact complete-host
ratio and the degree-two cycle with no four-cycle switch.
`scripts/verify_general_switching_ratio.py` exhaustively checks the
labelled forward/reverse theorem, including parallel descriptions.
`scripts/verify_sparse_block_host.py` checks all complete-block and
derangement cylinders through block size six. The consecutive-embedding
triple obstruction is checked by
`scripts/verify_sparse_block_geometry.py`. The arbitrary-coordinate
shape formula is checked by direct determinant enumeration in
`scripts/verify_sparse_block_affine_energy.py`. Zero-energy companion
coordinates are checked by `scripts/verify_sparse_zero_energy.py`. The
global expanded-grid construction is checked by
`scripts/verify_sparse_expanded_grid.py`. The exact standard-grid
balanced-colour energy is checked by
`scripts/verify_sparse_balanced_compression.py`.

## Completion criterion

This branch is complete when SAS1–SAS2 and the remaining host-specific
parts of SAS3–SAS5 are proved for at least one algebraic host rich enough
to support exact degree-two saturation and all collinearity constraints.
