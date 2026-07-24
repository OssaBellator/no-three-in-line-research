# The nonlinear switching layer around affine strong mappings

PX101 shows that a shallow perturbation of an affine strong mapping cannot by
itself have rank-three spread.  Nevertheless the affine roots supply a large,
explicit first layer of the PX98 switching graph at every prime admitting a
square root of `-1`.

Let

\[
p\equiv1\pmod4
\]

be prime, choose `i in F_p` with

\[
i^2=-1,
\]

and put

\[
f_{i,b}(x)=ix+b.
\]

Since `i`, `1-i`, and `1+i` are nonzero, each `f_(i,b)` is a strong complete
mapping.

## Theorem PX103 -- PROVED

Every affine root `f_(i,b)` has exactly

\[
\boxed{
\frac{p(p-1)}4
}
\]

distinct PX98 neighbours.

They are obtained by choosing

\[
a\in\mathbb F_p,
\qquad
r\in\mathbb F_p^*,
\qquad
s=ir.
\]

Each neighbour is represented by exactly four ordered pairs `(a,r)`,
corresponding to the four cyclic choices of a corner of the same affine square.

### Proof

For the affine map, put `A=ia+b` and choose `s=ir`.  Then

\[
f(a+r)=A+ir=A+s,
\]

\[
f(a-s)=A-is=A-i^2r=A+r,
\]

and

\[
f(a-s+r)=A+i(r-s)=A+r+s.
\]

Thus every `(a,r)` gives a PX98 trade.  The conditions
`r,s,r-s,r+s nonzero` follow from `r nonzero` and `i notin {0,1,-1}`.

The support rows are

\[
a+r\{0,1,-i,1-i\}.
\]

Choosing any one of these four rows as the distinguished corner `a'` and
rotating the ordered edge increments gives another parameter representation of
the same old and new four-cell sets.  Conversely, a representation is determined
by its distinguished old cell, so there are exactly four.  The `p(p-1)` ordered
parameter pairs therefore give `p(p-1)/4` distinct neighbours. \(\square\)

## Corollary PX103a -- PROVED

For every prime `p>=7` with `p congruent to 1 mod 4`, the union of the one-trade
neighbourhoods of all affine roots contains exactly

\[
\boxed{
\frac{p^2(p-1)}2
}
\]

distinct nonlinear strong complete mappings.

### Proof

There are two choices of `i` and `p` choices of `b`, hence `2p` affine roots.
Every one-trade neighbour differs from its root on exactly four rows and agrees
on `p-4>=3` rows.

Two distinct affine maps agree on at most one row.  Therefore no one-trade
neighbour can belong to two different affine-root neighbourhoods.  Multiply
`2p` by the degree from PX103.  The neighbour is not affine because it differs
from its unique affine root on four but not all rows. \(square\)

At `p=13` the formula gives

\[
26\cdot39=1014
\]

nonlinear mappings, exactly the degree-seven layer in PX99.

## 2. Switching interpretation

The affine root and one-trade layer form a biregular first shell at order
thirteen: every root has degree `39`, and every shell vertex has exactly one
affine-root neighbour.  At general primes, PX103 gives the root-side degree
exactly; controlling the shell-side reverse degree and expansion into deeper
layers is the next step toward the flow criterion PX100.

PX101 shows why the process cannot stop at this cubic layer.  A one-trade
neighbour retains `p-4` affine rows and therefore has rank-three spread constant
at least

\[
\frac3p\binom{p-4}{3}=\Omega(p^2).
\]

Many successive trades, or another global mixing operation, must move through
the deeper nonlinear switching graph.

## Verification

Run

```bash
python scripts/verify_product_affine_root_switching_layer.py
```

The verifier checks the formulas through prime order 29, deduplicates every
one-trade neighbourhood, and confirms the exact order-thirteen shell.