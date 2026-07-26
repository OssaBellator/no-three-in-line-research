# Finite word classification of concentrated balanced-swap certificates

**Branch:** `research/sparse-algebraic-spread`

SAS5i reduces every positive swap-local minimum to one cross-label column pair
incident with many destroyed current conflicts and at least as many repairable
near-conflicts.  The remaining certificate is not an arbitrary three-literal
pattern.  Relative to the two swapped columns it has exactly twelve destruction
words and twelve repair words, and every word using both swapped columns has a
unique rational third-column address for each row triple.

This is a finite reduction for SAS6.  It does not yet batch several swaps or prove
that one word pair admits an improving simultaneous exchange.

## Swap and constraint notation

Fix a balanced column colouring `kappa` and a cross-label swap

\[
\omega=\{x,y\},
\qquad
\kappa(x)=a,
\quad
\kappa(y)=b,
\quad
a\ne b.
\]

A constraint record is an ordered triple of distinct columns

\[
Q=(q_1,q_2,q_3;\ell_1,\ell_2,\ell_3),
\]

where `ell_i` is the required row-block label at `q_i`.  The record is satisfied
when `kappa(q_i)=ell_i` for all `i`.

For `i in {1,2,3}`, write:

- `X_i` when `x=q_i` and `y` is outside the scope;
- `Y_i` when `y=q_i` and `x` is outside the scope.

For ordered distinct positions `i,j`, write `XY_{ij}` when

\[
x=q_i,
\qquad
y=q_j.
\]

There are six singleton-scope words and six double-scope words.

## SAS5j -- exact twelve-word swap partition -- PROVED

Every constraint destroyed by `omega` belongs to exactly one of the twelve words

\[
\boxed{
\mathcal W_{\mathrm{des}}
=
\{X_i,Y_i:1\le i\le3\}
\cup
\{XY_{ij}:1\le i\ne j\le3\}.
}
\]

Its required labels on the swapped scope are forced:

- in a destruction word `X_i`, the required label at `x` is `a`;
- in a destruction word `Y_i`, the required label at `y` is `b`;
- in a destruction word `XY_{ij}`, the required labels at `(x,y)` are `(a,b)`.

Every constraint repaired by `omega` belongs to exactly one of the analogous twelve
words

\[
\boxed{
\mathcal W_{\mathrm{rep}}
=
\{X_i,Y_i:1\le i\le3\}
\cup
\{XY_{ij}:1\le i\ne j\le3\}.
}
\]

Its required labels on the swapped scope are forced in the opposite orientation:

- in a repair word `X_i`, the required label at `x` is `b`;
- in a repair word `Y_i`, the required label at `y` is `a`;
- in a repair word `XY_{ij}`, the required labels at `(x,y)` are `(b,a)`.

The singleton repair words have exactly one mismatch before the swap and the
double-scope repair words have exactly two mismatches before the swap.

### Proof

A swap changes only the labels at `x` and `y`.  Therefore a destroyed or repaired
constraint must contain at least one of those columns.  Since the three scope
columns are distinct, its intersection with `{x,y}` has size one or two.

If the intersection is `{x}`, the position of `x` is one of the three `X_i`
words; similarly `{y}` gives one `Y_i`.  If both columns occur, their ordered
positions are one of the six pairs `i!=j`, giving `XY_{ij}`.  These alternatives
are disjoint and exhaustive.

A destroyed constraint is satisfied before the swap, so its required labels at
`x,y` equal their current labels `a,b`.  A repaired constraint is satisfied after
the swap, when the labels at `x,y` are `b,a`.  In a singleton repair word the one
swapped scope column is the unique mismatch before the swap; in a double-scope
repair word both swapped columns are mismatched. QED.

## SAS5k -- two-scope words have a unique rational third-column address -- PROVED

Fix distinct rows

\[
r_1<r_2<r_3
\]

and distinct positions `i,j,k={1,2,3}`.  If the columns at positions `i,j` are
fixed as `c_i,c_j`, then there is at most one rational value of the third column
`c_k` for which the three cells are collinear.  It is

\[
\boxed{
c_k
=
c_i+
\frac{r_k-r_i}{r_j-r_i}(c_j-c_i).
}
\]

Consequently, for a fixed row triple and a fixed double-scope word `XY_{ij}`, the
third column of every destroyed or repaired constraint is uniquely determined by
`x,y`.  A standard-grid constraint exists only when the displayed rational value
is an integer in the column range and distinct from `x,y`.

### Proof

The line through `(r_i,c_i)` and `(r_j,c_j)` has affine interpolation formula

\[
c(r)=c_i+\frac{r-r_i}{r_j-r_i}(c_j-c_i).
\]

Evaluating at `r_k` gives the display.  Two distinct points determine one rational
line, so no second value is possible.  Integrality, range and distinctness are
exactly the conditions for the resulting record to be a valid standard-grid
constraint. QED.

Thus all double-scope words are indexed by an ordered position pair and a row
triple, with no free third-column choice.

## SAS5l -- concentrated word-pair certificate -- PROVED

Let `kappa` be a positive swap-local minimum satisfying the hypotheses of SAS5i.
Choose the cross-label swap `omega` supplied there, and write

\[
D=D(\omega),
\qquad
R=R(\omega).
\]

Then `R>=D>0`, and there exist one destruction word
`w_des in W_des` and one repair word `w_rep in W_rep` such that

\[
\boxed{
D_{w_{\rm des}}(\omega)\ge D/12,
\qquad
R_{w_{\rm rep}}(\omega)\ge R/12\ge D/12.
}
\]

Equivalently, one of the `12^2=144` ordered word pairs carries simultaneous
current-conflict and repair weight at least `D/12` on each side of the same fixed
column swap.

Combining with SAS5i gives

\[
\boxed{
D_{w_{\rm des}}(\omega),
R_{w_{\rm rep}}(\omega)
\ge
\frac{(3(N-d)-3)T(G_\kappa)}{12|\Omega_\kappa|}
=
\frac{(3(N-d)-3)T(G_\kappa)}{6N(N-d)}.
}
\]

### Proof

SAS5j partitions the `D` destroyed constraints into twelve disjoint classes, so
one class has size at least `D/12`.  It also partitions the `R` repaired
constraints into twelve disjoint classes, so one has size at least `R/12`.
SAS5i gives `R>=D` and

\[
D\ge\frac{(3(N-d)-3)T(G_\kappa)}{|\Omega_\kappa|}.
\]

Substitute `|Omega_kappa|=N(N-d)/2`. QED.

The two selected words need not be equal, and a singleton word still has a free
second scope column.  The theorem's gain is that SAS6 may now branch over a fixed
finite word pair.  If either selected word is double-scope, SAS5k additionally
replaces its third column by an exact rational row-triple address.

## Corrected SAS6 frontier

After SAS5l, a recurrent positive local minimum exposes:

1. one ordered current colour pair `(a,b)`;
2. one physical column pair `(x,y)`;
3. one of twelve destruction words and one of twelve repair words;
4. in every double-scope class, a uniquely reconstructed rational third-column
   address for each row triple;
5. current and repair multiplicities at the explicit SAS5l scale.

The remaining arithmetic task is to batch compatible swaps inside one such word
pair or prove that repeated row-triple addresses force an affine/divisor structure.
No mixture of arbitrary mismatch patterns remains.

## Finite check

`scripts/verify_sparse_swap_words.py` exhausts all balanced and unbalanced
three-colour assignments on five columns, every cross-label swap, every ordered
three-column scope and every required-label word.  It checks that all destroyed and
repaired records enter exactly one of the twelve classes with the forced labels and
mismatch counts stated in SAS5j.
