# Essential unit Hall walls factor exactly after contraction

CMR727--CMR733 show that removing one essential returned target edge creates a
canonical Hall wall of deficiency exactly one. Every perfect matching uses the
essential edge, matches the remaining deficient-side sources exactly onto the
wall target set, and matches the complementary vertices independently. Thus an
essential return gives strict lower-dimensional factorisation rather than a new
terminal obstruction.

Fix a balanced bipartite host

\[
H=(L,R;E)
\]

of side `m` with essential edge

\[
e=(u,v).
\]

Put `G=H-e`. Let `X` be any Hall-deficient source set of `G`, and put

\[
Y=N_G(X).
\]

By CMR728,

\[
|Y|=|X|-1,
\qquad
u\in X,
\qquad
v\notin Y,
\qquad
N_H(X)=Y\cup\{v\}.
\]

Define

\[
H_A=H[X\setminus\{u\},Y],
\qquad
H_B=H[L\setminus X,\ R\setminus(Y\cup\{v\})],
\]

and write

\[
a=|X|-1=|Y|,
\qquad
b=m-|X|=|R\setminus(Y\cup\{v\})|.
\]

## 1. Every full matching restricts to the two wall factors

### Theorem CMR734 -- PROVED

Every perfect matching `M` of `H` has the unique decomposition

\[
\boxed{
M=\{e\}\sqcup M_A\sqcup M_B,
}
\]

where

\[
M_A\in\operatorname{PM}(H_A),
\qquad
M_B\in\operatorname{PM}(H_B).
\]

### Proof

Essentiality gives `e in M`. No edge of `G` leaves `X` for
`R\setminus Y`, and the only such edge of `H` is `e=(u,v)`. After removing `e`,
the `|X|-1` sources in `X\setminus\{u\}` must therefore be matched into `Y`,
which also has size `|X|-1`; they form a perfect matching of `H_A`. The remaining
sources and targets are exactly the vertex classes of `H_B`. Uniqueness follows
by restriction. ∎

Both factor hosts are matchable, with the empty matching allowed at side zero.

## 2. Exact Cartesian wall factorisation

### Theorem CMR735 -- PROVED

Restriction gives a bijection

\[
\boxed{
\operatorname{PM}(H)
\cong
\{e\}
\times
\operatorname{PM}(H_A)
\times
\operatorname{PM}(H_B).
}
\]

Consequently

\[
\boxed{
|\operatorname{PM}(H)|
=
|\operatorname{PM}(H_A)|
|\operatorname{PM}(H_B)|.
}
\]

### Proof

CMR734 gives restriction. Conversely, the union of `e` with arbitrary perfect
matchings of the two factors covers every source and target exactly once and
uses only host edges. ∎

Extra edges from complementary sources into `Y` do not spoil the product: every
perfect matching has already consumed all of `Y` inside the wall factor.

## 3. Strict side budget

### Theorem CMR736 -- PROVED

The factor sides satisfy

\[
\boxed{a+b=m-1.}
\]

Every positive factor has side at most `m-1`. If `|X|=1`, then `(a,b)=(0,m-1)`;
if `X=L`, then `(a,b)=(m-1,0)`; otherwise both sides lie in
`{1,...,m-2}`.

### Proof

Directly,

\[
a+b=(|X|-1)+(m-|X|)=m-1.
\]

The cases follow from the possible values of `|X|`. ∎

## 4. Targets containing the essential edge have rank at most two

Let `T` be a compatible collinear triple occurring in some perfect matching of
`H` and containing `e`. Put

\[
T_A=T\cap E(H_A),
\qquad
T_B=T\cap E(H_B).
\]

### Theorem CMR737 -- PROVED

The remaining two target edges lie in the factor hosts and satisfy

\[
\boxed{|T_A|+|T_B|=2.}
\]

Hence the factor-rank pattern is one of

\[
\boxed{(2,0),\quad(1,1),\quad(0,2).}
\]

Every nonempty local part is a compatible partial matching of rank at most two.

### Proof

Choose a perfect matching containing `T` and apply CMR734. Every edge other than
`e` lies in exactly one factor, and exactly two target edges remain. ∎

## 5. Exact occurrence rectangles after wall contraction

For a factor host `K` and compatible prescription `P`, write

\[
\operatorname{PM}(K;P)
=
\{M\in\operatorname{PM}(K):P\subseteq M\}.
\]

An empty prescription imposes no condition.

### Theorem CMR738 -- PROVED

The full perfect-matching family containing `T` is exactly

\[
\boxed{
\{e\}
\times
\operatorname{PM}(H_A;T_A)
\times
\operatorname{PM}(H_B;T_B).
}
\]

Thus `T` is active exactly when every nonempty local prescription extends in its
factor host.

### Proof

Apply the product CMR735. Containment of `T` is precisely the independent pair
of local containment conditions. ∎

## 6. Deletable local edge or forced wall certificate

### Theorem CMR739 -- PROVED

Let `T` be an active target containing `e`. Exactly one of the following holds.

1. **Forced wall certificate.** Every edge in every nonempty local prescription
   `T_A,T_B` is essential in its factor host. Then every perfect matching of `H`
   contains `T`.
2. **Matching-preserving deletion.** Some local target edge is nonessential in
   its factor. Deleting it preserves a nonempty factor matching family and hence
   a nonempty full product, while making `T` inactive.

Deleting factor edges cannot activate a prescription which was inactive before
the deletion.

### Proof

In the first branch, every factor matching contains its local prescription, so
CMR738 gives the whole product. In the second, a factor matching avoiding the
chosen edge survives deletion and combines with the other factor and `e`.
Passing to a subhost only removes perfect matchings. ∎

## 7. Unit-wall normalisation endpoint

At one fixed unit-wall owner, repeatedly choose the first active target
containing `e`. Stop if it is forced; otherwise perform the first deletion from
CMR739.

### Corollary CMR740 -- PROVED

The procedure preserves a nonempty matching family and terminates after at most

\[
\boxed{
|E(H_A)|+|E(H_B)|
\le a^2+b^2
\le(m-1)^2
}
\]

deletions. At termination, one of the following holds.

1. A forced target certificate containing `e` occurs in every matching and is
   converted to the target closure by CMR703.
2. No active target containing `e` remains.
3. The remaining obstruction is pure or mixed between the strict factors and
   enters CMR629--CMR683.
4. A factor essential edge contracts, or the execution descends to a strict child
   prefix factor.

Thus a persistent essential-return unit wall is an exact lower-dimensional
product interface, not an unbounded same-side recursion.

### Proof

Each nonterminal step deletes a distinct factor edge, and CMR739 prevents
reactivation. Apply the edge bounds, exact product, and cited factor recursions.
∎

No all-`n` theorem is claimed. Exact restriction, Cartesian factorisation,
target-rank patterns, occurrence rectangles, and deletion alternatives are
checked in
[`scripts/verify_prime_power_unit_wall_factorization.py`](../scripts/verify_prime_power_unit_wall_factorization.py).
