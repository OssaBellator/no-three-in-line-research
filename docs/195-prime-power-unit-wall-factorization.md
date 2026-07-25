# Essential unit Hall walls factor exactly after contraction

CMR727--CMR733 show that removing one essential returned target edge creates a
canonical Hall wall of deficiency exactly one. That wall has a stronger matching
normal form. Every perfect matching uses the essential edge, matches the
remaining deficient-side sources exactly onto the wall target set, and matches
the complementary vertices independently. Thus an essential return gives strict
lower-dimensional factorisation rather than a new terminal obstruction.

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
u:=u\in X,
\qquad
v\notin Y,
\qquad
N_H(X)=Y\cup\{v\}.
\]

Define the two induced factor hosts

\[
H_A=H[X\setminus\{u\},Y],
\]

and

\[
H_B=H[L\setminus X,\ R\setminus(Y\cup\{v\})].
\]

Write

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
which also has size `|X|-1`. They consume all of `Y` and form a perfect matching
of `H_A`. The remaining sources and targets are precisely the vertex classes of
`H_B`, so the remaining matching edges form a perfect matching there.
Uniqueness follows by restriction to the disjoint vertex classes. ∎

In particular, both factor hosts are matchable, allowing the empty matching when
a factor side is zero.

## 2. Exact Cartesian wall factorisation

### Theorem CMR735 -- PROVED

The restriction map of CMR734 is a bijection

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

CMR734 gives the restriction map. Conversely, the union of `e`, any perfect
matching of `H_A`, and any perfect matching of `H_B` covers every source and
target exactly once and uses only edges of `H`. The constructions are inverse.
∎

Extra host edges directed from the complementary source side into `Y` do not
spoil the product; no perfect matching can use them after the wall factor has
consumed all of `Y`.

## 3. Strict side budget

### Theorem CMR736 -- PROVED

The factor sides satisfy

\[
\boxed{a+b=m-1.}
\]

Every positive factor has side at most `m-1`. More precisely:

1. if `|X|=1`, then `a=0` and `b=m-1`;
2. if `X=L`, then `a=m-1` and `b=0`;
3. otherwise both factors have sides in `{1,...,m-2}`.

### Proof

By definition,

\[
a+b=(|X|-1)+(m-|X|)=m-1.
\]

The three cases follow from the possible values of `|X|`. ∎

Thus essential return always removes one matching pair and never produces a
factor of the original side.

## 4. Targets containing the essential edge have rank at most two

Let `T` be a compatible collinear triple which occurs in some perfect matching
of `H` and contains `e`. Put

\[
T_A=T\cap E(H_A),
\qquad
T_B=T\cap E(H_B).
\]

### Theorem CMR737 -- PROVED

The remaining two target edges lie in the two factor hosts and satisfy

\[
\boxed{|T_A|+|T_B|=2.}
\]

Hence the factor-rank pattern is exactly one of

\[
\boxed{(2,0),\quad(1,1),\quad(0,2).}
\]

Every nonempty local part is a compatible partial matching of rank at most two.

### Proof

Choose a perfect matching containing `T`. CMR734 says every edge other than `e`
lies in exactly one of `H_A` and `H_B`. Since `T` has three edges and contains
`e`, exactly two edges remain. Compatibility is inherited from `T`. ∎

The unit-wall contraction therefore creates no high-rank residual target.

## 5. Exact occurrence rectangles after wall contraction

For a factor host `K` and compatible prescription `P`, write

\[
\operatorname{PM}(K;P)
=
\{M\in\operatorname{PM}(K):P\subseteq M\}.
\]

An empty prescription imposes no condition.

### Theorem CMR738 -- PROVED

The complete perfect-matching family containing `T` is exactly

\[
\boxed{
\{e\}
\times
\operatorname{PM}(H_A;T_A)
\times
\operatorname{PM}(H_B;T_B).
}
\]

In particular, `T` is active if and only if every nonempty local prescription
extends in its factor host.

### Proof

Use the exact product CMR735. A product matching contains `T` precisely when its
`A` factor contains `T_A` and its `B` factor contains `T_B`. These conditions are
independent. ∎

This is the two-factor rectangle of CMR631 with the essential edge contracted as
a fixed factor.

## 6. Deletable local edge or forced wall certificate

### Theorem CMR739 -- PROVED

Let `T` be an active target containing `e`. Exactly one of the following holds.

1. **Forced wall certificate.** Every edge of every nonempty local prescription
   `T_A,T_B` is essential in its factor host. Then every perfect matching of `H`
   contains `T`.
2. **Matching-preserving deletion.** Some local target edge is nonessential in
   its factor host. Deleting that edge preserves a perfect matching of the factor,
   preserves a nonempty full product, and makes `T` inactive.

A factor-edge deletion cannot activate a target prescription which was inactive
before the deletion.

### Proof

In the first branch, every factor matching contains its complete local
prescription, so CMR738 gives the full product as the occurrence rectangle. In
the second branch, a factor perfect matching avoiding the chosen edge survives
its deletion; adjoining any matching of the other factor and `e` gives a full
matching. Every occurrence of `T` required the deleted edge. Finally, passing to
a subhost only removes perfect matchings and cannot make an unextendable
prescription extendable. ∎

Forced wall certificates enter CMR703, while the deletion branch is monotone.

## 7. Unit-wall normalisation endpoint

At one fixed unit-wall owner, repeatedly choose the first active target containing
`e`. Stop if it is forced; otherwise perform the first deletion supplied by
CMR739.

### Corollary CMR740 -- PROVED

The procedure preserves a nonempty matching family and terminates after at most

\[
\boxed{
|E(H_A)|+|E(H_B)|
\le
a^2+b^2
\le
(m-1)^2
}
\]

deletions. At termination, exactly one of the following holds.

1. A forced target certificate containing `e` is present in every full matching
   and is converted to the target closure by CMR703.
2. No active target containing `e` remains.
3. The remaining obstruction is pure or mixed between the strict factors
   `H_A,H_B` and enters the product-rectangle, essential-transfer, and pure-factor
   recursions CMR629--CMR683.
4. A factor becomes essential and contracts, or the execution descends to a
   strict child prefix factor.

Thus a persistent essential-return unit wall is an exact lower-dimensional
product interface. It introduces neither an anonymous Hall obstruction nor an
unbounded same-side recursion.

### Proof

Each nonterminal step deletes one distinct factor edge and CMR739 prevents
reactivation of an eliminated target. The edge-count bound follows from the
factor sides and CMR736. The exact product and target classification are
CMR735--CMR739; all remaining conflict classes are precisely those handled by
the cited product and child recursions. ∎

No all-`n` theorem is claimed. Exact wall restriction, Cartesian factorisation,
target-rank patterns, occurrence rectangles, and deletion alternatives are
checked in
[`scripts/verify_prime_power_unit_wall_factorization.py`](../scripts/verify_prime_power_unit_wall_factorization.py).
