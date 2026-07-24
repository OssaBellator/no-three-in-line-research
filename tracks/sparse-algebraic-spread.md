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

## Completion criterion

This branch is complete when SAS1–SAS2 and the remaining host-specific
parts of SAS3–SAS5 are proved for at least one algebraic host rich enough
to support exact degree-two saturation and all collinearity constraints.
