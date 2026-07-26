# Primitive dilation structure of singleton-scope swap words

**Branch:** `research/sparse-algebraic-spread`

SAS5j leaves a free second and third scope column in every singleton-scope word.
They are not independent.  Once the fixed swapped column and the row triple are
specified, collinearity is one primitive two-gap Diophantine equation.  The two
remaining columns are a common integer dilation of the reduced row-gap vector.

Together with SAS5m--SAS5p, this gives an exact arithmetic model for every one of
the twelve destruction and repair words: double-scope words use a primitive line
progression, while singleton-scope words use a primitive two-arm dilation.

## Singleton notation

Fix rows

\[
r_1<r_2<r_3
\]

and one singleton-scope word whose fixed swapped column `x` occurs at position
`i`.  Let `j,k` be the other two positions in the fixed canonical order used by
the word.  Put

\[
A=r_j-r_i,
\qquad
B=r_k-r_i.
\]

Both gaps are nonzero and distinct.  Let the unknown columns at positions `j,k`
be `c_j,c_k`.  Collinearity with `(r_i,x)` is equivalent to

\[
A(c_k-x)=B(c_j-x).
\]

Define

\[
g=\gcd(|A|,|B|),
\qquad
A_0=A/g,
\qquad
B_0=B/g.
\]

Then `gcd(|A_0|,|B_0|)=1`.

## SAS5q -- exact primitive-dilation parameterization -- PROVED

The integer solutions of the singleton collinearity equation are exactly

\[
\boxed{
(c_j,c_k)
=
(x+A_0s,\ x+B_0s),
\qquad s\in\mathbb Z.
}
\]

For a valid three-distinct-column constraint, `s` is nonzero and both displayed
columns lie in the board range and differ from each other and from `x`.

### Proof

Write `u=c_j-x` and `v=c_k-x`.  The equation becomes

\[
A_0v=B_0u.
\]

Since `A_0` and `B_0` are coprime, `A_0` divides `u`; write `u=A_0s`.  Substitution
gives `v=B_0s`.  Conversely every such pair satisfies the equation.  Because
`A_0,B_0` are nonzero and distinct, nonzero `s` gives three distinct columns;
board validity is exactly the stated range condition. QED.

Thus the apparently free pair `(c_j,c_k)` has one integer degree of freedom.

## SAS5r -- finite primitive row-shape dictionary -- PROVED

For an `N`-row grid, the primitive singleton shape

\[
\boxed{(A_0,B_0)}
\]

belongs to a dictionary of size at most

\[
\boxed{4(N-1)^2.}
\]

The full exact row-triple address is reconstructed from

\[
\boxed{(i,j,k,A_0,B_0,g,r_i),}
\]

because

\[
r_j=r_i+gA_0,
\qquad
r_k=r_i+gB_0.
\]

For one fixed word, the position tuple `(i,j,k)` is already fixed.  The remaining
safe exact row-address stock is at most

\[
\boxed{4N(N-1)^3.}
\]

### Proof

Each oriented row gap lies in
`{-(N-1),..., -1,1,...,N-1}`, giving fewer than `2(N-1)` choices for each reduced
gap and hence at most `4(N-1)^2` ordered primitive pairs.  The scale `g` has at
most `N-1` choices and the base row at most `N`; multiplying gives the safe exact
row-address stock.  The reconstruction identities are the definitions of the
gaps. QED.

The stock is safe rather than sharp: row ordering and board range exclude many
addresses.

## SAS5s -- weighted localization to one primitive dilation family -- PROVED

Let a weighted family of valid constraints lie in one fixed singleton-scope word
and one fixed physical swapped column `x`.  If its total weight is `W`, then:

1. one primitive row-shape class carries weight at least
   
   \[
   \boxed{
   W/[4(N-1)^2];
   }
   \]
2. one exact row-triple address carries weight at least
   
   \[
   \boxed{
   W/[4N(N-1)^3].
   }
   \]

Inside the final class every constraint is determined by the single integer
dilation parameter `s` in SAS5q.

If the selected destruction or repair word in SAS5l is singleton-scope, its
retained weight is at least `D/12`; hence one primitive shape carries at least

\[
\boxed{
D/[48(N-1)^2]
}
\]

and one exact row-triple dilation family carries at least

\[
\boxed{
D/[48N(N-1)^3].
}
\]

### Proof

Apply weighted pigeonhole to the primitive-shape stock in SAS5r, then to the scale
and base-row choices inside the selected shape.  Substitute SAS5l's `D/12` lower
bound for the final two statements. QED.

The conclusion retains an entire one-parameter family rather than localizing to
one exact column pair.

## SAS5t -- corrected all-word arithmetic frontier -- PROVED

For one concentrated ordered word pair from SAS5l:

- every double-scope side has SAS5m--SAS5p's primitive parallel-line model;
- every singleton-scope side has SAS5q--SAS5s's primitive dilation model;
- every side retains a polynomially quantified primitive shape or direction
  class;
- after fixing its exact row or line address, only one integer parameter remains.

Therefore no destruction or repair word retains two independent free geometric
columns.  The unresolved SAS6 work is now:

1. batch compatible swaps inside one progression or dilation class;
2. compare the destruction and repair integer-parameter sets on the same fixed
   physical column swap;
3. prove improvement or classify a recurrent affine/divisor parameter set;
4. preserve balanced colour multiplicities and avoid cross-swap collateral.

### Proof

SAS5j partitions all records into singleton and double-scope words.  SAS5m--SAS5p
supply the double-scope model and SAS5q--SAS5s supply the singleton model.  These
cases are exhaustive. QED.

## Finite check

`scripts/verify_sparse_singleton_scope_dilations.py` exhausts standard grids
through order twelve, every ordered row triple, singleton position and fixed
column.  It checks all valid column pairs, the primitive-dilation equivalence,
exact row reconstruction and the displayed shape/address stocks.
