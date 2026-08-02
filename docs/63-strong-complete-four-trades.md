# Four-cell trades in strong complete mappings

PX96 reduces one protected nonlinear coset to a strong complete mapping problem.
For the two diagonal colourings, a local permutation `f` must satisfy

\[
f,
\qquad x\mapsto x-f(x),
\qquad x\mapsto x+f(x)
\]

all being permutations of the prime field.  This chapter gives an exact
four-row switching which preserves all three permutations and studies its first
non-affine switching graph.

All arithmetic in the trade formulas is modulo an odd prime `p`.

## 1. The parallelogram four-trade

Choose parameters

\[
a,A,r,s\in\mathbb F_p
\]

with

\[
r,s,r-s,r+s\ne0.
\]

Suppose a strong complete mapping `f` has the four values

\[
\begin{array}{c|c}
\text{row}&f(\text{row})\\
\hline
 a&A\\
 a+r&A+s\\
 a-s&A+r\\
 a-s+r&A+r+s.
\end{array}
\]

Define `f'` by changing only these four rows:

\[
\begin{array}{c|c}
\text{row}&f'(\text{row})\\
\hline
 a&A+r+s\\
 a+r&A+r\\
 a-s&A+s\\
 a-s+r&A.
\end{array}
\]

## Theorem PX98 -- PROVED

The map `f'` is again a strong complete mapping.  More precisely, the trade
preserves each of the following multisets exactly:

\[
\{f(x):x\in\mathbb F_p\},
\]

\[
\{x-f(x):x\in\mathbb F_p\},
\]

\[
\{x+f(x):x\in\mathbb F_p\}.
\]

The four old cells and four new cells are pairwise distinct.

### Proof

The image values before and after the trade are the same four-element set

\[
\{A,A+s,A+r,A+r+s\}.
\]

Write `B=a-A`.  On the four affected rows, the old difference residues are

\[
B,
\quad B+r-s,
\quad B-r-s,
\quad B-2s,
\]

whereas the new difference residues are

\[
B-r-s,
\quad B,
\quad B-2s,
\quad B+r-s.
\]

Thus the difference multiset is unchanged.

Similarly, writing `C=a+A`, the old sum residues are

\[
C,
\quad C+r+s,
\quad C+r-s,
\quad C+2r,
\]

and the new sum residues are

\[
C+r+s,
\quad C+2r,
\quad C,
\quad C+r-s.
\]

Thus the sum multiset is unchanged.  Outside the four rows nothing changes.
Since the three old maps are permutations, the three new maps are permutations.
The nonzero conditions on `r,s,r-s,r+s` give four distinct rows, four distinct
columns, and ensure that no new cell equals the old cell in its row. \(\square\)

This is a genuine nonlinear trade.  It is not a transposition of two images;
two-image swaps cannot preserve both diagonal permutations.

## 2. Exact switching graph at order thirteen

Let `S_p` be the set of all strong complete mappings of `F_p`.  Join two maps
when one is obtained from the other by one PX98 trade.  Multiple parameter
representations of the same trade give one graph edge.

For `p=5,7,11`, every strong complete mapping is affine and

\[
|S_5|=10,
\qquad
|S_7|=28,
\qquad
|S_{11}|=88.
\]

At `p=13`, nonlinear mappings first appear in this sequence.

## Theorem PX99 -- PROVED FINITE

The exact order-thirteen strong-complete switching census is:

\[
|S_{13}|=4524.
\]

The PX98 switching-degree distribution is

| Degree | Mappings |
|---:|---:|
| 0 | 1,456 |
| 2 | 2,028 |
| 7 | 1,014 |
| 39 | 26 |

The graph has one nontrivial connected component of size `3,068` and `1,456`
isolated vertices.  It has exactly `6,084` edges.

The 26 degree-39 vertices are precisely the affine maps whose slope is one of
the two square roots of `-1`; each of the 39 adjacent maps has four parameter
representations of the same PX98 trade.

### Proof

Enumerate permutations row by row while tracking used image, difference, and sum
residues.  For every completed strong mapping, enumerate all triples `(a,r,s)`
and apply the displayed identities.  Deduplicate the resulting neighbours.
Breadth-first search gives the component data, and direct affine recognition
gives the final classification.  Every operation is exact finite-field
arithmetic. \(\square\)

## 3. Exact low-rank spread at order thirteen

Choose a strong complete mapping uniformly from all `4,524` maps.  For a
prescribed matching cylinder of `k` distinct row-image pairs, let `P_k` be the
maximum probability over all such cylinders.

## Corollary PX99a -- PROVED FINITE

At order thirteen,

\[
P_1=\frac1{13},
\]

\[
P_2=\frac1{78}=\frac2{(13)_2},
\]

and

\[
P_3=\frac5{1131}
=\frac{220/29}{(13)_3}
<\frac8{(13)_3}.
\]

Thus the uniform order-thirteen strong-complete measure is rank-three spread
with absolute constant eight.

### Proof

The maximum numbers of strong mappings containing one, two, and three prescribed
edges are respectively

\[
348,
\qquad
58,
\qquad
20.
\]

Divide by `4524` and multiply by the corresponding falling factorials. \(\square\)

The same exact calculation for orders `5,7,11` gives rank-three normalized
constants `6`, `15/2`, and `45/4`, respectively.  Those small solution spaces
are affine and display the rank-two freezing described in PX95.  The nonlinear
order-thirteen space improves the constant to below eight.

## 4. General-proof significance

PX98 supplies the missing local move inside the first-stage simultaneous-rainbow
space.  PX99 shows that, once nonlinear strong complete mappings appear, the
four-trade graph has a large connected component and the full uniform solution
space already has the rank-three cylinder scale required by PX97.

The next theorem is now a switching-expansion statement:

> for all sufficiently large admissible prime orders, construct a probability
> measure on strong complete mappings, supported on large PX98 switching
> components or a controlled union of components, with cylinder probabilities
> `O((p)_k^{-1})` for `k<=3`.

A proof could use canonical-path comparison, switch-count ratios between
cylinder classes, or a random-walk measure corrected by component weights.
The order-thirteen census shows that the target is numerically plausible but is
not an asymptotic proof.

## 5. Verification

Run

```bash
python scripts/verify_product_strong_complete_four_trades.py
```

The verifier enumerates the strong complete mappings at orders `5,7,11,13`,
checks every four-trade identity, constructs the exact order-thirteen switching
graph, and reproduces all cylinder maxima.