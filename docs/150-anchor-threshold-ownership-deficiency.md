# Anchor-threshold ownership deficiency

PP3of localizes every anchor-only ownership Hall set to a small label side or a
small complementary side.  This chapter converts that localization into a
quantitative maximum-matching statement.

Even when the anchor-acceptable ownership host has no balanced perfect matching,
its capacitated Hall deficiency is small.  A maximum acceptable assignment can
therefore be completed to a fully balanced ownership by using only a sublinear
number of threshold-violating macro--label pairs.  Those violations occupy only
a sublinear number of macros at any fixed positive local density.

## 1. General anchor-acceptable host

Let the movement-label set have size

\[
T=MW,
\]

and let every macro have ownership capacity \(W\).  Declare \(A\) acceptable for
macro \(i\) when

\[
U_i(A)\le u.
\]

Retain the total anchor mass

\[
\mathfrak U=\sum_{i,A}U_i(A).
\]

For a label set \(X\), write \(N(X)\) for its acceptable macro neighbourhood and
define its capacitated deficiency

\[
\operatorname{def}(X)
=
\bigl(|X|-W|N(X)|\bigr)_+.
\]

Assume

\[
S=rac{2W\mathfrak U}{uT}<\frac T2.
\]

The same definitions apply on the refill side with \(V_i(B)\).

## 2. Small-side Hall deficiencies

### Proposition PP3vg -- PROVED

Every deficient label set \(X\) satisfies

\[
\min\{|X|,T-|X|\}<S.
\]

#### Proof

PP3oe gives

\[
u|X|(T-|X|)<W\mathfrak U.
\]

If \(s=\min\{|X|,T-|X|\}\), then

\[
|X|(T-|X|)\ge\frac{sT}{2}.
\]

Substitution gives \(s<S\). ∎

This is the nonasymptotic form of PP3of.

## 3. Large Hall sets miss few macros

Suppose \(X\) is deficient and

\[
T-|X|<S.
\]

Put

\[
k=M-|N(X)|.
\]

Every one of those \(k\) macros rejects every label in \(X\).

### Proposition PP3vh -- PROVED

One has

\[
\boxed{
k<\frac{\mathfrak U}{u(T-S)}.}
\]

#### Proof

For each macro \(i\notin N(X)\), every \(A\in X\) has \(U_i(A)>u\).  Hence that
macro contributes more than \(u|X|>u(T-S)\) to the total anchor mass.  Sum over
the \(k\) macros and compare with \(\mathfrak U\). ∎

Thus the nearly-dead-macro alternative has an explicit global cardinality bound,
not only a per-macro acceptable-label bound.

## 4. Maximum capacitated deficiency

### Theorem PP3vi -- PROVED

The maximum Hall deficiency of the anchor-acceptable ownership host satisfies

\[
\boxed{
\max_X\operatorname{def}(X)
\le
D_{m anc},
}
\]

where

\[
D_{m anc}
=
\max\left\{
S,
\frac{W\mathfrak U}{u(T-S)}
\right\}.
\]

#### Proof

If \(|X|<S\), then

\[
\operatorname{def}(X)\le|X|<S.
\]

Otherwise PP3vg forces \(s=T-|X|<S\).  Write
\(|N(X)|=M-k\).  Since \(T=MW\),

\[
\operatorname{def}(X)
=
T-s-W(M-k)
=
kW-s
\le kW.
\]

Apply PP3vh. ∎

Since \(S=o(T)\), the second term is asymptotic to \(S/2\).  Thus
\(D_{\rm anc}=O(S)\).

## 5. Almost-acceptable balanced ownership

Expand every macro into \(W\) identical capacity clones.

### Theorem PP3vj -- PROVED

There is a matching of acceptable ownership pairs covering at least

\[
T-D_{m anc}
\]

movement labels and the same number of macro slots.

Consequently there is a fully balanced movement ownership in which at most

\[
D_{m anc}
\]

assigned macro--label pairs violate the anchor threshold \(u\).

#### Proof

The capacitated Hall deficiency theorem says that the number of unmatched left
vertices in a maximum matching is

\[
\max_X\operatorname{def}(X).
\]

Apply PP3vi.  The unmatched label set and unmatched macro-slot set have equal
size.  Pair them arbitrarily to complete the balanced ownership.  Only those
completion pairs can violate the threshold. ∎

The refill ownership host has the identical conclusion.

This theorem does not claim that the violating pairs have small anchor weight;
it controls their number exactly.

## 6. Exceptional-macro concentration

Fix \(0<\theta<1\).  Call a macro movement-exceptional when more than
\(	heta W\) of its owned labels violate the anchor threshold.

### Corollary PP3vk -- PROVED

Under the ownership supplied by PP3vj, the number of movement-exceptional macros
is at most

\[
\boxed{
\frac{D_{m anc}}{\theta W}.
}
\]

The same bound holds for refill-exceptional macros.  Hence the union of the two
exceptional macro sets has size at most

\[
\frac{2D_{m anc}}{\theta W}.
\]

#### Proof

Each exceptional macro contains more than \(	heta W\) violating assignments,
while their total number is at most \(D_{m anc}\).  Count incidences. ∎

Outside this union, both label sides have at least
\((1-\theta)W\) anchor-threshold-good owned labels.

## 7. Slab-optimal scale

Take the PP3of threshold

\[
u=m^{-1/40+\zeta}RT,
\qquad
0<\zeta<\frac1{40}.
\]

### Corollary PP3vl -- PROVED

At the slab-optimal scales,

\[
D_{m anc}
=
O(m^{1/2-\zeta+o(1)}),
\]

and therefore

\[
\frac{D_{m anc}}T
=
m^{-1/40-\zeta+o(1)}
=o(1).
\]

For every fixed \(	heta>0\), the number of exceptional macros on either label
side is

\[
O(m^{1/40-\zeta+o(1)})
=o(M).
\]

#### Proof

PP3od gives \(\mathfrak U=O(m^{2+o(1)})\).  Substitute

\[
W=m^{19/40+o(1)},
\quad
T=m^{21/40+o(1)},
\quad
u=m^{29/20+\zeta+o(1)}
\]

into PP3vi.  The first term is
\(O(m^{1/2-\zeta+o(1)})\), and the second has the same or smaller order because
\(T-S=(1-o(1))T\).  Divide by \(T\) and then by \(W\). ∎

Here the displayed exponent for \(u\) is

\[
-\frac1{40}+\zeta+\frac{19}{20}+\frac{21}{40}
=
\frac{29}{20}+\zeta.
\]

## 8. Revised direct anchor endpoint

### Corollary PP3vm -- PROVED

Same-slot anchor energy no longer forces a globally failed ownership problem.
There are balanced movement and refill ownerships with:

1. only \(o(T)\) threshold-violating assigned labels on each side;
2. only \(o(M)\) macros containing a fixed positive fraction of those violations;
3. at least \((1-\theta)W\) threshold-good labels on both sides of every other
   macro.

The remaining direct allocation obstruction is therefore local:

- complete the \(o(M)\) exceptional macros;
- absorb at most \(	heta W\) exceptional labels per ordinary macro;
- or convert the concentrated anchor weight carried by those assignments.

A diffuse or middle-density anchor ownership failure is no longer possible.