# Balanced-colour energy for standard-grid block compression

SAS5e embeds the complete sparse block host with zero compatible triples
when its \(N\) column vertices may use a polynomially expanded coordinate
range.  Compressing to the standard \(N\) column coordinates is
equivalent to assigning those coordinates to the \(b\) block labels,
with exactly \(d\) coordinates of each label.  The resulting conflict
count has an exact balanced-colouring energy.

Let \(N=bd\).  Fix a row-block map

\[
\beta:[N]\to[b],
\qquad |\beta^{-1}(\ell)|=d,
\]

and let

\[
\kappa:[N]\to[b],
\qquad |\kappa^{-1}(\ell)|=d,
\]

be a balanced column-block map.  The embedded host is

\[
G_\kappa
=
\{(r,c):\beta(r)=\kappa(c)\}.
\]

For \(r_1<r_2<r_3\), let \(\mathcal L(r_1,r_2,r_3)\) be the ordered
triples of distinct columns \((c_1,c_2,c_3)\) satisfying

\[
(r_2-r_1)(c_3-c_1)
=
(r_3-r_1)(c_2-c_1).
\]

## SAS5f -- balanced compression energy

### Theorem SAS5f -- PROVED

The number of compatible collinear host triples is exactly

\[
\boxed{
T(G_\kappa)
=
\sum_{r_1<r_2<r_3}
\ \sum_{(c_1,c_2,c_3)\in\mathcal L(r_1,r_2,r_3)}
\prod_{i=1}^3
\mathbf1_{\kappa(c_i)=\beta(r_i)}.
}
\]

Let \(A_3,A_{21},A_{111}\) count the pairs

\[
\bigl((r_1,r_2,r_3),(c_1,c_2,c_3)\bigr)
\]

in the display according as the row-block label multiplicities are
\(3\), \(2+1\), or \(1+1+1\).  If \(\kappa\) is uniformly random among
balanced column maps, then

\[
\boxed{
\mathbb E_\kappa T(G_\kappa)
=
\frac{
A_3(d)_3
+
A_{21}(d)_2d
+
A_{111}d^3
}{(N)_3}.
}
\]

Consequently some balanced standard-grid embedding satisfies

\[
\boxed{
T(G_\kappa)
\leq
\frac{
A_3(d)_3
+
A_{21}(d)_2d
+
A_{111}d^3
}{(N)_3},
}
\]

and one can find such a map by conditional expectation.

### Proof

Every compatible geometric triple has three distinct rows, which have a
unique increasing order.  Listing its columns in the corresponding row
order gives one element of
\(\mathcal L(r_1,r_2,r_3)\).  Its three cells lie in \(G_\kappa\)
exactly when all three block-label indicators in the first display are
one.  This proves the exact energy identity without overcounting.

For a fixed ordered column triple and prescribed row-label vector, let
\(m_\ell\) be the multiplicity of label \(\ell\).  Sampling a uniformly
balanced map is sampling without replacement from \(d\) copies of every
label, so

\[
\Pr\bigl(\kappa(c_i)=\beta(r_i)\ \forall i\bigr)
=
\frac{\prod_\ell(d)_{m_\ell}}{(N)_3}.
\]

The three multiplicity patterns give respectively
\((d)_3\), \((d)_2d\), and \(d^3\).  Summing the indicator expectations
proves the second box.  At least one map is no larger than the average.
Sequentially assign column labels while retaining a completion of the
required multiplicities and choose a label of minimum conditional
expectation at each step to make the construction deterministic.
\(\square\)

## Checkable SAS5 endpoint

For the block-host spread constant \(C=9\) from SAS4b, SAS5a applies
whenever

\[
\boxed{
\frac{
A_3(d)_3
+
A_{21}(d)_2d
+
A_{111}d^3
}{(N)_3}
<
\frac{d^3}{18^3}.
}
\]

Thus standard-grid coordinate compression is now a finite weighted
balanced \(3\)-CSP with an exact first-moment benchmark.  A successful
compression theorem must either prove the displayed profile count is
small for a chosen row partition or beat this balanced-random baseline
using arithmetic structure.

The identity also exposes a limitation: balancing alone need not make
the expectation \(O(d^3)\), because the full grid has many affine
three-term shapes.  SAS5 still needs a structured low-energy colouring,
not merely an arbitrary relabelling of the expanded SAS5e columns.

`scripts/verify_sparse_balanced_compression.py` enumerates every balanced
colouring for small consecutive and interlaced row partitions and checks
both the exact energy and its average profile formula.
