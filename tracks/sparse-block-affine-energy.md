# Exact affine-shape energy inside a complete sparse block

SAS5b counts one diagonal family in consecutively embedded complete
blocks. The obstruction is not tied to consecutive coordinates. For an
arbitrary complete block, all internal compatible collinear triples are
given by an exact one-dimensional shape energy.

Let \(R,C\subset\mathbb R\) be finite sets with
\(|R|=|C|=d\ge3\). For \(0<\lambda<1\), define

\[
A_R(\lambda)
=
\#\left\{
(r_1,r_2,r_3)\in R^3:
r_1<r_2<r_3,\
\frac{r_2-r_1}{r_3-r_1}=\lambda
\right\},
\]

and define \(A_C(\lambda)\) analogously. Only finitely many rational
values occur when the coordinates are integral.

## SAS5c -- complete-block affine-shape formula

### Theorem SAS5c -- PROVED

The number \(T_{\rm int}(R,C)\) of unordered collinear triples in
\(R\times C\) using three distinct rows and three distinct columns is

\[
\boxed{
T_{\rm int}(R,C)
=
\sum_{0<\lambda<1}
A_R(\lambda)
\bigl(A_C(\lambda)+A_C(1-\lambda)\bigr).
}
\]

The first term counts positive-slope triples and the second counts
negative-slope triples. Consequently:

1. the internal geometric contribution of an arbitrary complete block
   is exactly checkable from two one-dimensional shape histograms;
2. if \(C=aR+b\) for some \(a\ne0\), then
   \[
   T_{\rm int}(R,C)\ge {d\choose3};
   \]
3. if \(C=aR+b\) with \(a>0\), then the positive-slope contribution is
   \[
   \sum_\lambda A_R(\lambda)^2
   \ge
   \frac{\binom d3^2}{|\operatorname{supp}A_R|}.
   \]

### Proof

Sort the rows of a compatible triple as \(r_1<r_2<r_3\), and put

\[
\lambda=\frac{r_2-r_1}{r_3-r_1}.
\]

Its columns are distinct. If they increase as \(c_1<c_2<c_3\),
collinearity is equivalent to

\[
\frac{c_2-c_1}{c_3-c_1}=\lambda.
\]

Choosing one row triple and one column triple of shape \(\lambda\), then
pairing them in increasing order, gives one positive-slope triple.
This correspondence is bijective, so the positive contribution is
\(\sum_\lambda A_R(\lambda)A_C(\lambda)\).

For negative slope, write the columns along increasing rows as
\(c_1>c_2>c_3\). In increasing column order the triple is
\(c_3<c_2<c_1\), whose shape is

\[
\frac{c_2-c_3}{c_1-c_3}=1-\lambda.
\]

Pairing an increasing row triple of shape \(\lambda\) with the reverse
of an increasing column triple of shape \(1-\lambda\) is again a
bijection. This gives
\(\sum_\lambda A_R(\lambda)A_C(1-\lambda)\) and proves the formula.

If \(C=aR+b\), the \(d\) cells

\[
\{(r,ar+b):r\in R\}
\]

belong to the block and lie on one line. Their three-element subsets
give the second assertion. For \(a>0\), affine maps preserve the shape
histogram, so \(A_C=A_R\). Cauchy--Schwarz on the nonzero histogram
entries proves the last assertion. \(\square\)

## Block-host consequence

Suppose a sparse block host is embedded as

\[
G=\bigsqcup_{\ell=1}^b (R_\ell\times C_\ell),
\]

with the row sets pairwise disjoint and the column sets pairwise
disjoint. Its total compatible triple count decomposes exactly as

\[
T(G)
=
\sum_{\ell=1}^b T_{\rm int}(R_\ell,C_\ell)
+T_{\rm cross}(G),
\]

where \(T_{\rm cross}\) counts triples meeting at least two blocks.
Therefore the SAS5a global endpoint requires both

\[
\sum_{\ell,\lambda}
A_{R_\ell}(\lambda)
\bigl(A_{C_\ell}(\lambda)+A_{C_\ell}(1-\lambda)\bigr)
<
\frac{d^3}{(2C_0)^3}
\]

and a compatible residual budget for \(T_{\rm cross}\), where \(C_0\)
is the spread constant in SAS5a.

In particular, if every \(C_\ell\) is an affine image of
\(R_\ell\), the internal contribution alone is at least

\[
b{d\choose3}
=
\frac{N(d-1)(d-2)}6.
\]

Thus SAS5b extends from consecutive blocks to every block embedding
whose row and column coordinates have the same affine shape. Escaping
the obstruction requires deliberately shape-incompatible coordinate
sets in almost all blocks, or abandoning the global union-bound
endpoint; cross-block triples must still be controlled separately.

`scripts/verify_sparse_block_affine_energy.py` compares the exact formula
with direct determinant enumeration for all row and column subsets of
sizes three through five in a seven-point integer interval.
