# Two-point absorber order is unbounded

PX152 identifies the first two-point lattice leftover whose minimum absorber
order is four. PX153--PX154 show that order three is not universally sufficient.
This chapter proves the stronger structural conclusion: **no fixed absorber
order is universally sufficient.**

The proof does not require an exhaustive template-rank census. It uses only two
facts.

1. A fixed combinatorial absorber template has a linear feasibility system in
   its internal edge coordinates and the three leftover parameters.
2. Every feasible leftover lies on the nondegenerate lattice quadric from
   PX144.

A finite collection of affine lines cannot cover a quadratic surface containing
quadratically many field points.

## 1. General fixed-order templates

Fix an absorber order \(k\ge0\). An absorber consists of a \(k\)-edge matching
\(M_0\) and a \((k+2)\)-edge matching \(M_1\) with

\[
V(M_1)=V(M_0)\mathbin{\dot\cup}(R_0\cup C_0\cup D_0\cup S_0),
\]

where the normalized leftover is

\[
R_0=\{\pm1\},
\qquad
C_0=\{\pm b\},
\qquad
D_0=\{\pm u\},
\qquad
S_0=\{\pm v\}.
\]

Label the edges of \(M_0\) by row and column variables

\[
A_1,\ldots,A_k,
\qquad
B_1,\ldots,B_k.
\]

The labels available to \(M_1\) are

\[
\begin{aligned}
R&:\quad 1,-1,A_1,\ldots,A_k,\\
C&:\quad b,-b,B_1,\ldots,B_k,\\
D&:\quad u,-u,A_1-B_1,\ldots,A_k-B_k,\\
S&:\quad v,-v,A_1+B_1,\ldots,A_k+B_k.
\end{aligned}
\]

After fixing the row order, a labelled combinatorial template is specified by
three permutations assigning the column, difference and sum labels to the
\(k+2\) rows. Thus there are at most

\[
\boxed{T_k=((k+2)!)^3}
\]

templates of order \(k\).

For a fixed template, each prospective edge contributes the two equations

\[
r-c-d=0,
\qquad
r+c-s=0.
\]

These are linear equations in the \(2k\) internal variables and the external
coordinates

\[
1,b,u,v.
\]

## Lemma PX155 -- PROVED

For every odd prime \(p\), the set of parameter triples

\[
(b,u,v)\in\mathbb F_p^3
\]

realised by one fixed order-\(k\) absorber template is either empty or an affine
subspace of dimension at most one. In particular, one template realises at
most

\[
\boxed p
\]

parameter triples.

### Proof

The solution set of the template equations in the internal variables and
\((b,u,v)\) is affine linear. Its projection onto the external coordinates is
therefore an affine subspace \(L_T\subseteq\mathbb F_p^3\).

Whenever the template is feasible, the difference of the incidence vectors of
\(M_1\) and \(M_0\) is exactly the leftover incidence vector. It therefore lies
in the integer edge lattice. PX144 gives the necessary lattice equation

\[
\boxed{u^2+v^2=2(1+b^2).}
\]

Consequently

\[
L_T\subseteq Q_p,
\qquad
Q_p=\{(b,u,v):u^2+v^2-2b^2=2\}.
\]

The homogeneous quadratic form

\[
q(b,u,v)=u^2+v^2-2b^2
\]

is nondegenerate in odd characteristic: its matrix is

\[
\operatorname{diag}(-2,1,1)
\]

and has nonzero determinant. A two-dimensional affine subspace contained in
\(Q_p\) would have a two-dimensional direction space on which the quadratic
part and its polar form both vanish. That would be a two-dimensional totally
isotropic subspace of a nondegenerate three-dimensional quadratic space, which
is impossible. Equivalently, a nondegenerate quadratic polynomial in three
variables has no affine-plane component.

Thus \(L_T\) has dimension at most one and contains at most \(p\) field points.
\(\square\)

PX153 is the exact order-three refinement of this lemma: every order-three
template actually has codimension exactly two in parameter space.

## 2. Quadratically many lattice-circle types

We next recall the elementary count used in PX154.

For every nonzero \(b\) with \(1+b^2\ne0\), the equation

\[
u^2+v^2=2(1+b^2)
\]

has

\[
p-\chi(-1)\ge p-1
\]

ordered solutions \((u,v)\in\mathbb F_p^2\). Removing solutions with \(u=0\) or
\(v=0\) deletes at most four pairs, and at most two nonzero values of \(b\)
satisfy \(1+b^2=0\). Therefore there are at least

\[
(p-3)(p-5)
\]

signed nonzero lattice-admissible triples.

Direct completion requires

\[
\{u^2,v^2\}
=
\{(1-b)^2,(1+b)^2\}.
\]

For one \(b\), this gives at most eight signed ordered pairs \((u,v)\). Hence the
number of signed lattice-admissible, directly noncompletable triples is at least

\[
\boxed{p^2-16p+23.}
\]

Every normalized leftover set has at most eight signed representations, so the
number of distinct directly noncompletable normalized leftovers is at least

\[
\boxed{
\frac{p^2-16p+23}{8}.
}
\]

## Theorem PX156 -- PROVED

For every fixed integer \(K\ge0\), define

\[
C_K=\sum_{k=0}^K((k+2)!)^3.
\]

For every prime satisfying

\[
\boxed{p>8C_K+16,}
\]

there is a lattice-admissible two-point leftover in the strong-complete host
which has no absorber of order at most \(K\).

Consequently the minimum absorber order of two-point lattice leftovers is
unbounded as the prime varies. In particular, the bounded two-point absorber
conjecture stated after PX147 is false.

### Proof

By PX155, each order-\(k\) template realises at most \(p\) parameter triples and
there are at most \(((k+2)!)^3\) templates. Therefore all templates of order at
most \(K\) realise at most

\[
C_Kp
\]

normalized leftover sets.

On the other hand, the number of distinct lattice-admissible, directly
noncompletable normalized leftovers is at least

\[
\frac{p^2-16p+23}{8}.
\]

If \(p>8C_K+16\), then

\[
\frac{p^2-16p+23}{8}>C_Kp.
\]

Some directly noncompletable leftover is therefore not realised by any absorber
template of order at most \(K\). \(\square\)

For example,

\[
C_3=2!^3+3!^3+4!^3+5!^3=1,742,048,
\]

so the general argument already proves the order-three obstruction for

\[
p>13,936,400.
\]

This improves the deliberately crude determinant threshold in PX154. The exact
prime-23 obstruction from PX152 is far stronger at small order.

## 3. Finite evidence for order four

The unboundedness theorem is asymptotic and does not predict the first prime at
which each absorber order fails. Exact searches immediately beyond PX152 give
the following evidence.

## Theorem PX157 -- PROVED FINITE

At prime order twenty-nine:

- there are seventy-two directly noncompletable normalized types;
- thirty-two have no order-two absorber;
- eight have no order-three absorber;
- every one of those eight has an order-four absorber.

At prime order thirty-one:

- there are eighty-five directly noncompletable normalized types;
- forty-one have no order-two absorber;
- thirteen have no order-three absorber;
- every one of those thirteen has an order-four absorber.

Thus order four is sufficient for every normalized two-point type through prime
order thirty-one, even though PX156 proves that no fixed order, including four,
can remain sufficient for all primes.

The order-three exception lists are:

\[
\begin{aligned}
p=29:\quad
&(1,11,12),(1,12,11),(9,13,13),(12,3,7),\\
&(12,7,3),(12,8,9),(12,9,8),(13,5,5),
\end{aligned}
\]

and

\[
\begin{aligned}
p=31:\quad
&(1,8,8),(1,10,11),(1,11,10),(2,6,6),\\
&(5,8,9),(5,9,8),(6,8,14),(6,14,8),\\
&(11,5,8),(11,8,5),(14,8,12),(14,12,8),(15,3,3).
\end{aligned}
\]

The exact order-four witnesses are generated and checked by the finite census
harness used for PX152; they should be moved into a dedicated compact verifier
before treating PX157 as part of a long-term regression suite.

## 4. Consequence for exact completion

PX156 closes one of the previous research directions negatively. A completion
proof for the pseudorandom almost-matching from PX141 cannot rely on a fixed
finite menu of bounded-order absorbers for individual two-point packets.

The remaining viable mechanisms are qualitatively different.

1. **Growing-order absorbers.** Allow the absorber order to increase with the
   prime while proving that the added secant and triangle loads remain small.
2. **Collective absorption.** Absorb many two-point circle packets in one trade,
   using cancellation among their three lattice moments.
3. **Exact covering with conflicts.** Complete the entire leftover at once by a
   covering theorem which incorporates the repeated-shape conflict system.
4. **Iterated pseudorandom matching.** Reduce the leftover to bounded size while
   preserving its moment structure, then use an order depending only on that
   final size rather than a universal two-point gadget.

The collective and exact-cover routes are now the more natural targets. The
individual bounded-absorber conjecture is decisively refuted.
