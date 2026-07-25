# Actual base degree one and buffer-cycle terminal escape

PX315--PX340 reduce the abstract trajectory terminal branch to constant order for
fixed base degree.  In the product construction the base degree is smaller than
the abstract parameter suggests.  The current diagonal is recorded separately,
and the only nonhistorical ordinary forbidden positions are occupied by the
opposite permutation layer.  Thus the actual base graph has degree one.

Consequently every acyclic historical-union residual has order at most two.
Such a core can be escaped without releasing any ancestor constraint: borrow
two fresh endpoint labels from the ambient permutation layer and use a three-
or four-cycle avoiding every ordinary forbidden position.  Integer
factorization bounds allow the buffers to be chosen so that the inserted cells
contain no internal collinear triple.  The corrected external blocker forest
then gives the causal strict-sign-or-child interface.

## 1. The actual base degree

Work in one active permutation layer.  Let

\[
F^{\rm ord}=D\cup P\cup H_1\cup\cdots\cup H_d,
\]

where `D` is the current diagonal, `P` is the partial matching occupied by the
opposite permutation layer, and the `H_j` are pairwise edge-disjoint historical
position matchings.

### Theorem PX341 -- PROVED

In the decomposition of PX294 and PX315, the nonhistorical base graph is

\[
\boxed{F_0=P}
\]

and therefore

\[
\boxed{\Delta_0=1.}
\]

The complete ordinary forbidden graph has maximum row and column degree at most

\[
\boxed{\Delta_{\rm ord}=d+2.}
\]

Hence every trajectory child with acyclic releasable historical union has order

\[
\boxed{s\le2.}
\]

### Proof

The alternating neutralization bank forbids exactly the current position and
the cell occupied by the opposite permutation layer.  The former is `D`; the
latter is one partial matching `P`.  Every ancestor generation adds at most one
historical partial matching.  Apply PX316 with `Delta_0=1`. \(\square\)

Packet-complement constraints are event constraints, not additional ordinary
forbidden cells, and prescribed compatible centres are removed before the
residual matching problem is formed.

## 2. Divisor cap

Let the ambient layer have labels `[n]`, with selected points

\[
P_i=(x_i,y_i),
\]

where all `x_i` and all `y_i` are distinct integers in `[0,n-1]`.  Put

\[
\mathfrak d(n)
=
\max_{1\le m\le(n-1)^2}\tau(m).
\]

For a nonzero integer `p`, an equation

\[
(x_i-a)(y_i-b)=p
\]

has at most `2 mathfrak d(n)` solutions among the labels, because every
solution supplies a signed divisor pair of `p`.

## 3. One-core buffer cycle

### Theorem PX342 -- PROVED

Let `u` be one terminal core label.  Suppose

\[
\boxed{
n>2\Delta_{\rm ord}+2+2\mathfrak d(n).
}
\]

Then there are distinct buffer labels `a,b`, disjoint from `u`, such that

\[
\boxed{u\to a\to b\to u}
\]

is allowed by `F^ord`, and its three inserted cells are not collinear.

### Proof

Choose any allowed arc `u to a`.  The set

\[
N^+(a)\cap N^-(u)
\]

has at least `n-2Delta_ord` labels.  Exclude `u,a`.  The three new cells are

\[
(x_u,y_a),\qquad (x_a,y_b),\qquad (x_b,y_u).
\]

They are collinear exactly when

\[
\boxed{
(x_b-x_u)(y_b-y_a)
=
(x_a-x_u)(y_u-y_a).
}
\]

The right side is nonzero.  Thus at most `2 mathfrak d(n)` labels `b` are bad.
The displayed size hypothesis leaves an allowed choice. \(\square\)

## 4. Two-core buffer cycle

### Theorem PX343 -- PROVED

Let `u,v` be two terminal core labels.  Suppose

\[
\boxed{
n>2\Delta_{\rm ord}+5+4\mathfrak d(n).
}
\]

Then there are distinct buffers `a,b`, disjoint from `u,v`, such that

\[
\boxed{
u\to a\to v\to b\to u
}
\]

is allowed by `F^ord`, and no three of its four inserted cells are collinear.

### Proof

The intersection `N^+(u) cap N^-(v)` has at least
`n-2Delta_ord` labels, so choose `a` distinct from `u,v`.
Then choose `b` from `N^+(v) cap N^-(u)`, again of size at least
`n-2Delta_ord`.

Write the four inserted cells as

\[
F_1=(x_u,y_a),\quad
F_2=(x_a,y_v),\quad
F_3=(x_v,y_b),\quad
F_4=(x_b,y_u).
\]

Exclude `u,v,a`.  Collinearity of `F_1,F_2,F_3` determines at most one value
of `y_b`, and collinearity of `F_1,F_2,F_4` determines at most one value of
`x_b`.  The other two triples are collinear exactly when

\[
\boxed{
(x_b-x_u)(y_b-y_a)
=
(x_v-x_u)(y_u-y_a)
}
\]

or

\[
\boxed{
(x_b-x_a)(y_b-y_v)
=
(x_v-x_a)(y_u-y_v).
}
\]

Both right sides are nonzero, so each equation excludes at most
`2 mathfrak d(n)` labels.  At most `5+4 mathfrak d(n)` labels are excluded in
total, and the size hypothesis gives the required `b`. \(\square\)

## 5. Causal terminal escape

### Theorem PX344 -- PROVED REDUCTION

Assume every terminal core endpoint carries an injectively assigned designated
old certificate, as in PX288.  Under the size hypothesis of PX342 or PX343,
the corresponding buffer cycle:

1. moves every core endpoint;
2. avoids every ordinary ancestor position;
3. destroys at least `s` designated old certificates;
4. creates no internal support-three certificate.

Therefore

\[
\boxed{d_\sigma\ge s>c_3=0,}
\]

and PX326--PX327 give the strict-sign-or-child interface through finitely many
external support-one/two blocker children.

### Proof

Allowedness against `F^ord` includes the current diagonal, the opposite layer,
and every historical position.  Thus no paid ancestor certificate is recreated.
PX342 and PX343 eliminate every triple using three inserted cells.  Moving each
core endpoint destroys its assigned certificate.  Apply the corrected frozen-
switch blocker forest. \(\square\)

### Corollary PX345 -- PROVED REDUCTION

For the actual two-permutation-layer product construction, trajectory-saturated
terminal cores do not require composite ancestor release or an extreme-ray
census once the ambient layer satisfies the displayed divisor-size bounds.
Every such core is buffer-cycle executable and reduces to the already finite
external blocker forest.

The surviving terminal frontier consists only of geometrically realizable
support-one/two blocker children which remain nonimproving under the exact
constant-order optimizer, together with finite small-`n` base cases.

## 6. Verification

Run

```bash
python scripts/verify_product_buffer_cycle_terminal_escape.py
```

The verifier checks the determinant/product identities, signed-divisor
multiplicity, the forbidden-neighbour intersection bounds, and random
one-/two-core buffer searches.
