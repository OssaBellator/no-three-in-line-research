# Zero-energy companion coordinates for complete sparse blocks

SAS5c expresses every internal compatible triple in \(R\times C\) as an
overlap between the one-dimensional shape histograms of \(R\) and \(C\).
That overlap can be eliminated completely: there is no universal
internal-triple obstruction for arbitrarily embedded complete blocks.

For a finite ordered set \(R\), retain

\[
A_R(\lambda)
=
\#\left\{
r_1<r_2<r_3\in R:
\frac{r_2-r_1}{r_3-r_1}=\lambda
\right\}.
\]

Put

\[
\mathcal S_R
=
\operatorname{supp}A_R
\cup
\{1-\lambda:\lambda\in\operatorname{supp}A_R\}.
\]

## SAS5d -- zero-energy companion construction

### Theorem SAS5d -- PROVED

For every real \(d\)-element row set \(R\), \(d\ge3\), there is an
integer \(d\)-element column set \(C\) such that

\[
\boxed{
T_{\rm int}(R,C)=0.
}
\]

One may choose

\[
C\subseteq
\left[
0,\
d-1+|\mathcal S_R|\binom d3
\right]
\subseteq
\left[
0,\
d-1+2\binom d3^2
\right].
\]

Thus the required coordinate range is effective and polynomial in
\(d\).

### Greedy construction

Start with \(C_2=\{0,1\}\). Suppose

\[
C_n=\{c_1<\cdots<c_n\}
\]

has been chosen with no three-term shape in \(\mathcal S_R\). For each
\(a<b\) in \(C_n\) and \(\lambda\in\mathcal S_R\), forbid the one value

\[
x=a+\frac{b-a}{\lambda}.
\]

Choose \(c_{n+1}\) to be the first integer larger than \(c_n\) which is
not forbidden.

### Proof

Every new triple created at step \(n+1\) has the form

\[
a<b<c_{n+1}
\]

with \(a,b\in C_n\). Its shape is

\[
\frac{b-a}{c_{n+1}-a}.
\]

It belongs to \(\mathcal S_R\) exactly when \(c_{n+1}\) equals one of the
forbidden values. The greedy rule therefore preserves

\[
\operatorname{supp}A_C\cap\mathcal S_R=\varnothing.
\]

There are at most
\(\binom n2|\mathcal S_R|\) forbidden values at step \(n\). Among the
next \(\binom n2|\mathcal S_R|+1\) integers, at least one is available,
so

\[
c_{n+1}-c_n
\le
\binom n2|\mathcal S_R|+1.
\]

Summing from \(n=2\) to \(d-1\) and using

\[
\sum_{n=2}^{d-1}\binom n2=\binom d3
\]

gives

\[
\max C
\le
d-1+|\mathcal S_R|\binom d3.
\]

Since
\(|\mathcal S_R|\le2\binom d3\), the second coordinate bound follows.

Finally, for every \(\lambda\in\operatorname{supp}A_R\), both
\(\lambda\) and \(1-\lambda\) lie in \(\mathcal S_R\). Hence

\[
A_C(\lambda)=A_C(1-\lambda)=0.
\]

The SAS5c energy identity now gives \(T_{\rm int}(R,C)=0\). \(\square\)

## Consequence for SAS5

The affine-shape obstruction SAS5b--SAS5c is a restriction on aligned
embeddings, not on the abstract complete-block host. Every individual
block can be embedded with zero internal compatible triples in a
polynomial coordinate range.

This does not complete SAS5. A saturated host uses many row and column
blocks inside one common \(N\times N\) grid, and triples meeting two or
three blocks may dominate. The remaining geometric task is now exactly
to coordinate the companion constructions across blocks while keeping
the global coordinate budget and cross-block triple mass below the
SAS5a threshold.

`scripts/verify_sparse_zero_energy.py` runs the greedy construction for
all small integer row sets and checks the coordinate bound and exact
zero affine-shape energy.
