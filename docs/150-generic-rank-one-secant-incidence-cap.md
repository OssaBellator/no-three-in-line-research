# Generic rank-one buffer returns have a secant-incidence cap

PX370 removes repeated support pairs from the coordinate rank-one sector by
turning them into loaded coordinate lines.  The remaining quadratic generic
rank-one sector has candidate centres across the full two-buffer field.  Its
blocker mass is a weighted incidence count between those candidate centres and
secant lines of the fixed selected background.

When every selected line has occupancy at most `K`, one secant line carries
weight at most `binom(K,2)`.  Szemeredi--Trotter then bounds the total generic
rank-one blocker mass by `O(K^2 n^(8/3))`.  Consequently a weighted terminal
core of destruction larger than `K^2 n^(2/3)` cannot return through generic
rank one unless a loaded selected line has already appeared.

## 1. Secant-line decomposition

Let `Z` be the fixed selected background, with

\[
|Z|\le2n.
\]

Let `F` be one exact generic two-variable candidate-cell field from PX352, so

\[
|F|\le n^2.
\]

For every real line `ell`, put

\[
r_\ell=|Z\cap\ell|,
\qquad
k_\ell=|F\cap\ell|.
\]

A rank-one blocker consists of one candidate centre `f in F` and one unordered
pair of fixed selected points on the same line.

### Theorem PX381 -- PROVED

The total generic rank-one blocker multiplicity is exactly

\[
\boxed{
M_{\rm gen}
=
\sum_{\ell:r_\ell\ge2}
k_\ell\binom{r_\ell}{2}.
}
\]

### Proof

Every blocker determines its unique real line.  On a fixed line `ell`, choose
one of its `k_ell` candidate centres and one of the `binom(r_ell,2)` selected
pairs.  Distinct choices give distinct geometric blocker certificates.
\(\square\)

## 2. Bounded occupancy gives an incidence estimate

Assume

\[
\max_\ell r_\ell\le K.
\]

Let `L_Z` be the set of distinct lines containing at least two points of `Z`.
Then

\[
|L_Z|\le\binom{2n}{2}<2n^2.
\]

### Theorem PX382 -- PROVED USING SZEMEREDI--TROTTER

Under the occupancy cap,

\[
\boxed{
M_{\rm gen}=O(K^2n^{8/3}).
}
\]

The implicit constant is absolute.

### Proof

PX381 gives

\[
M_{\rm gen}
\le
\binom K2
\sum_{\ell\in L_Z}k_\ell
\le
K^2 I(F,L_Z),
\]

where `I(F,L_Z)` is the number of point--line incidences.  The incidence bound
is

\[
I(F,L_Z)
=
O(|F|^{2/3}|L_Z|^{2/3}+|F|+|L_Z|).
\]

Substitute `|F|<=n^2` and `|L_Z|<2n^2`.  Every term is
`O(n^(8/3))` or smaller. \(\square\)

### Corollary PX383 -- PROVED REDUCTION

If the weighted two-variable outcome of PX357 is generic rank one for a bank
of designated destruction `D`, then either some selected line contains more
than `K` points, or

\[
\boxed{
D=O(K^2n^{2/3}).
}
\]

### Proof

PX357 gives

\[
M_{\rm gen}\ge\frac{Dn^2}{32}.
\]

Combine with PX382 and divide by `n^2`. \(\square\)

Thus generic rank one is asymptotically weaker than the trivial `D=O(n)` cap
whenever `K=n^{o(1)}`.

## 3. Consequence after a mixed return

PX369 shows that an original mixed cross-buffer outcome produces a weighted
one-point child with

\[
D_1\ge n/64.
\]

### Corollary PX384 -- PROVED REDUCTION

Assume the selected-line occupancy satisfies

\[
K=n^{o(1)}.
\]

For all sufficiently large `n`, the next nonimproving terminal cover of the
mixed-return child cannot be:

1. another mixed cross-buffer type, by PX368; or
2. a generic rank-one two-variable type without producing a loaded selected
   line, by PX383.

### Proof

The mixed type would require `D_1<=64`, contrary to `D_1>=n/64` for large
`n`.  Generic rank one without a loaded line would require

\[
D_1=O(K^2n^{2/3})=n^{2/3+o(1)},
\]

while `D_1>=n/64`. \(\square\)

### Corollary PX385 -- PROVED REDUCTION

After one mixed return, every further nonimproving cover produces one of:

1. a loaded selected line;
2. a nondegenerate coordinate rank-one family;
3. a directed-path family, which is possible only while
   `D=O(n^(1/3))` by PX366.

Since the mixed-return child has `D>=n/64`, the directed-path alternative is
also excluded for large `n`.  Therefore the persistent branch after a mixed
return is reduced to loaded-line or nondegenerate coordinate rank-one
geometry.

The loaded-line outcome has cubic old destruction by PX241--PX244.  The only
remaining repeated return type after PX385 is nondegenerate coordinate rank
one, already compressed onto a weighted selected-point cover by PX371--PX380.

## 4. Verification

Run

```bash
python scripts/verify_product_generic_rank_one_cap.py
```

The verifier checks the secant-line decomposition on finite integer examples,
validates the exact line-weight sum, and checks all exponent and threshold
comparisons used in PX382--PX385.