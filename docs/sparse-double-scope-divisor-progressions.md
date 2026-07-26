# Divisor and primitive-progression structure of double-scope swap words

**Branch:** `research/sparse-algebraic-spread`

SAS5k reconstructs the third column of a double-scope swap certificate as a
rational affine interpolation.  The remaining integrality condition has an exact
number-theoretic form: after dividing the row and column displacement by their
gcd, the reduced row displacement must divide the third-row displacement.  Every
valid third cell therefore lies on one primitive lattice progression.

For a fixed double-scope word and fixed swapped columns, only `N-1` oriented row
gaps and at most `N` parallel offsets occur.  This reduces the double-scope part of
SAS6 from arbitrary row triples to a polynomial dictionary of primitive parallel
lines.  Singleton-scope words remain separate because their second scope column
is still free.

## Double-scope notation

Fix an ordered row triple

\[
r_1<r_2<r_3
\]

and distinct positions `i,j,k={1,2,3}`.  In one fixed double-scope word, the
columns `c_i,c_j` are the two fixed swapped columns in the orientation prescribed
by the word.  Put

\[
A=r_j-r_i,
\qquad
D=c_j-c_i,
\qquad
H=r_k-r_i.
\]

Both `A` and `D` are nonzero.  SAS5k gives the unique rational third column

\[
c_k=c_i+\frac{H}{A}D.
\]

Define

\[
g=\gcd(|A|,|D|),
\qquad
A_0=A/g,
\qquad
D_0=D/g.
\]

Then

\[
\gcd(|A_0|,|D_0|)=1.
\]

## SAS5m -- exact reduced-denominator integrality criterion -- PROVED

The reconstructed third column is an integer if and only if

\[
\boxed{A_0\mid H.}
\]

When this holds, there is one integer

\[
s=H/A_0
\]

and the third cell is

\[
\boxed{
(r_k,c_k)
=
(r_i,c_i)+s(A_0,D_0).
}
\]

Thus the valid lattice points on the witness line are exactly the primitive
progression through `(r_i,c_i)` with direction `(A_0,D_0)`, subject only to the
row-order, distinctness and board-range restrictions.

### Proof

The column is integral exactly when `A` divides `HD`.  Substituting
`A=gA_0` and `D=gD_0` gives

\[
A_0\mid HD_0.
\]

Because `A_0` and `D_0` are coprime, Euclid's lemma gives `A_0|H`.  Writing
`H=A_0s` in the interpolation formula yields `c_k=c_i+sD_0`, which is the boxed
vector identity.  Conversely that identity is integral and collinear. QED.

This is an exact arithmetic criterion; no probabilistic or asymptotic estimate is
used.

## SAS5n -- canonical divisor-direction address -- PROVED

For one fixed double-scope word and one fixed ordered swapped column pair, the
sign of `A=r_j-r_i` is fixed by the positions `i,j`.  Hence `A` has at most
`N-1` possible values on an `N`-row grid.

The data

\[
\boxed{(A,g,A_0,D_0)}
\]

are canonically reconstructed from the row gap and fixed column displacement.
Equivalently one may use the divisor address

\[
\boxed{(\operatorname{sgn}A,g,q,D_0),
\qquad q=|A_0|,}
\]

where

\[
g\mid |D|,
\qquad
|A|=gq,
\qquad
\gcd(q,|D_0|)=1.
\]

The primitive-direction stock inside one fixed word and column pair is therefore
at most

\[
\boxed{N-1.}
\]

### Proof

The word fixes whether `j` lies before or after `i` in the increasing row order,
so the sign of `A` is fixed and its magnitude lies in `{1,...,N-1}`.  The gcd and
reduced displacements are deterministic functions of `A,D`.  The displayed
divisor relations are their definitions, and `(A_0,D_0)` is primitive by SAS5m.
QED.

The bound is deliberately by oriented row gap, which is no larger than a cruder
divisor-count dictionary.

## Parallel-line offsets

For one primitive direction `(A_0,D_0)`, define the affine offset

\[
\Omega
=
D_0r-A_0c.
\]

It is constant along every progression step `(A_0,D_0)`.

## SAS5o -- fixed directions form an injectively row-addressed parallel family -- PROVED

Fix the double-scope word, swapped columns and oriented row gap `A`.  Then every
valid certificate lies on the line

\[
\boxed{
D_0r-A_0c
=
\Omega_i,
\qquad
\Omega_i=D_0r_i-A_0c_i.
}
\]

Distinct values of the base row `r_i` give distinct offsets `Omega_i` because
`D_0` is nonzero.  Consequently:

1. the witness lines in one direction class are parallel;
2. there are at most `N` exact affine offsets;
3. the pair `(A,Omega_i)` reconstructs the primitive witness line;
4. the integer parameter `s` reconstructs the third cell on that line.

### Proof

The offset is invariant under a progression step because

\[
D_0(r+A_0s)-A_0(c+D_0s)=D_0r-A_0c.
\]

The fixed word fixes `c_i` as one of the two swapped columns.  If two base rows
gave the same offset, then `D_0(r_i-r_i')=0`; since `D_0` is nonzero, the rows
would agree.  The remaining statements follow from SAS5m. QED.

## SAS5p -- weighted localization to one primitive direction and line -- PROVED

Let a weighted family of valid certificates lie in one fixed double-scope word
and one fixed physical swapped column pair.  If its total weight is `W`, then:

1. one oriented row-gap and primitive-direction class carries weight at least
   
   \[
   \boxed{W/(N-1)};
   \]
2. inside that class, one exact parallel-line offset carries weight at least
   
   \[
   \boxed{W/[N(N-1)]}.
   \]

Every certificate in the final class lies on one exact primitive lattice
progression and differs only by its integer parameter `s` and any already retained
label data.

If the selected destruction or repair word of SAS5l is double-scope, its retained
weight is at least `D/12`; hence one exact primitive line class on that side has
weight at least

\[
\boxed{
\frac{D}{12N(N-1)}.
}
\]

### Proof

There are at most `N-1` oriented row gaps by SAS5n, so weighted pigeonhole gives
the first bound.  SAS5o gives at most `N` offsets in the selected direction class,
so a second weighted pigeonhole gives the second.  Substitute SAS5l's `D/12`
weight for the final statement. QED.

The localization is polynomial rather than constant-factor.  Its purpose is to
replace arbitrary rational row-triple addresses by one explicit primitive affine
progression which can be batched or classified arithmetically.

## Corrected SAS6 frontier

After SAS5m--SAS5p, every recurrent double-scope destruction or repair class has:

- one fixed word and physical swapped column pair;
- one oriented row gap `A`;
- one primitive direction `(A_0,D_0)` and reduced denominator `|A_0|`;
- one exact affine offset `Omega`;
- one integer progression parameter `s` for each certificate.

Thus the double-scope branch of SAS6 is reduced to batching compatible swaps on
parallel primitive progressions or classifying repeated progression parameters.
The remaining unmatched cases are singleton-scope words, interactions between the
destruction and repair progression classes, and the conversion of a concentrated
progression into a globally improving balanced batch.

## Finite check

`scripts/verify_sparse_double_scope_progressions.py` exhausts standard grids
through order twelve, every ordered row triple, every ordered position pair and
every pair of distinct fixed columns.  It checks the integrality equivalence,
primitive progression formula, divisor address reconstruction, offset invariance
and the `N-1` direction and `N` offset stocks.
