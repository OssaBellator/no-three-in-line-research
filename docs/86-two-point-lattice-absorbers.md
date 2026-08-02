# Bounded absorbers for two-point lattice leftovers

PX144 classifies a balanced leftover with two vertices in every part. After
translation and scaling it has the normal form

\[
R_0=\{\pm1\},
\qquad
C_0=\{\pm b\},
\qquad
D_0=\{\pm u\},
\qquad
S_0=\{\pm v\},
\]

where

\[
u^2+v^2=2(1+b^2).
\]

It is directly completable exactly when

\[
\{u^2,v^2\}=\{(1-b)^2,(1+b)^2\}.
\]

This chapter studies the remaining circle rotations.

An absorber of order \(k\) consists of two matchings \(M_0,M_1\) such that

\[
|M_0|=k,
\qquad
|M_1|=k+2,
\]

and

\[
V(M_1)=V(M_0)\mathbin{\dot\cup}
(R_0\cup C_0\cup D_0\cup S_0).
\]

Thus a matching which currently uses \(M_0\) can be completed across the
leftover by replacing it with \(M_1\).

## Lemma PX145 -- PROVED

Every two-point leftover over an odd prime is equivalent to the displayed
normal form under a host automorphism.

### Proof

If the four part centres are \(r,c,r-c,r+c\), translate the row and column
coordinates by \(-r,-c\). This induces translations by \(-r+c\) and \(-r-c\)
in the difference and sum parts and preserves every host edge. Then multiply
all four parts by the inverse of the nonzero row half-gap \(a\). The row gap
becomes one and the other gaps become \(b/a,u/a,v/a\). Replacing a gap by its
negative does not change its two-point set. \(\square\)

## Theorem PX146 -- PROVED FINITE

For the prime orders

\[
p=7,11,13,
\]

every lattice-admissible but directly noncompletable two-point leftover has an
absorber of order two.

The exact numbers of normalised noncompletable types are

\[
1,\qquad4,\qquad8,
\]

respectively.

## Theorem PX147 -- PROVED FINITE

At orders \(17\) and \(19\), every lattice-admissible but directly
noncompletable two-point leftover has an absorber of order at most three.

The exact normalised populations are:

| Prime | Noncompletable types | Order-two absorbed | Order-three exceptions |
|---:|---:|---:|---:|
| 17 | 19 | 16 | 3 |
| 19 | 24 | 20 | 4 |

The order-two exceptions are exactly

\[
( b,u,v)=(1,6,6),(4,6,7),(4,7,6)
\]

at order 17, and

\[
(1,4,8),(1,8,4),(2,9,9),(9,5,5)
\]

at order 19.

Each of these seven types has an explicit order-three absorber recorded in the
verification harness.

### Proof of PX146--PX147

Enumerate the unsigned gap representatives

\[
1\le b,u,v\le\frac{p-1}{2}.
\]

Retain precisely the triples satisfying the circle equation and reject the
direct-completion criterion from PX144. For one retained type, enumerate every
matching \(M_0\) of two host edges disjoint from the leftover. The union of its
vertices with the leftover has four vertices in each part; enumerate all
\(4!\) row-column bijections and test the difference and sum sets. This is a
complete order-two absorber search.

The resulting exceptional lists are exactly those displayed. For each listed
exception, the harness checks a recorded three-edge matching \(M_0\) and a
five-edge matching \(M_1\), verifies both are matchings, and verifies the exact
vertex-set identity defining an absorber. PX145 transports the normalised
certificates to every unnormalised leftover. \(\square\)

## 2. Significance

The absorber order is not uniformly two: the first counterexamples occur at
order 17. Nevertheless all exact circle types through order 19 have absorber
order at most three. This supports the bounded two-point absorber conjecture:

> There is an absolute constant \(K\) such that every lattice-admissible
> two-point leftover in the strong-complete host has an absorber of order at
> most \(K\).

A proof would supply the first local building block for completing the
pseudorandom almost-perfect matching from PX141. Larger leftovers would still
require decomposition into two-point lattice packets or a higher-rank absorber.

## Verification

Run

```bash
python scripts/verify_product_two_point_absorbers.py
```

The wrapper compiles the exact C++ census, reproduces every population and
exception list, and verifies all seven order-three certificates.
