# Finite rigidity census for complete low-height slope families

PX176 gives a universal affine-rigidity threshold when more than half of the
finite slopes are protected.  Exact-cover search shows that the structured
height families can force affine rigidity substantially below that threshold.

For a prime \(p\) and height \(H\), put

\[
R_H=\{\pm ba^{-1}:1\le a,b\le H,\ \gcd(a,b)=1\}\subseteq\mathbb F_p^*.
\]

A permutation \(f\) protects the complete signed height-\(H\) family exactly
when every map

\[
x\longmapsto f(x)-rx,\qquad r\in R_H,
\]

is a permutation.

## Theorem PX177 -- PROVED FINITE

The complete exact census has no nonlinear protected permutation in the
following cases:

| Prime \(p\) | Height \(H\) | \(|R_H|\) | Unprotected nonzero slopes |
|---:|---:|---:|---:|
| 37 | 3 | 14 | 22 |
| 41 | 3 | 14 | 26 |
| 43 | 3 | 14 | 28 |
| 47 | 3 | 14 | 32 |
| 53 | 4 | 22 | 30 |

Every solution is affine,

\[
f(x)=gx+b,\qquad g
otin R_H.
\]

Thus the finite structured family is more rigid than the general
Rédei--Megyesi counting threshold in these cases.  In particular, the
\(p=47,H=3\) census is not implied merely by the inequality in PX176.

### Proof

Affine translation and common scalar dilation preserve all graph secant
slopes.  Given any two graph points of a solution, normalize them to

\[
(0,0),\qquad(1,g),
\]

where \(g
otin R_H\).  It is therefore enough to exhaust, for every allowed
\(g\), the simultaneous exact-cover problem with

\[
f(0)=0,\qquad f(1)=g.
\]

The search tracks one used-value mask for \(f\) and one mask for every protected
permutation \(f-rx\).  At each step it chooses an unassigned row with the
fewest legal images.  Every completed mapping is tested against the normalized
affine map \(f(x)=gx\).

The deterministic search exhausts every allowed normalized slope in each table
row and finds no nonlinear completion.  Undoing the normalization gives the
stated affine classification. \(\square\)

## Significance

PX177 is finite evidence, not an asymptotic strengthening of PX176.  It shows
that the main growing-uniformity question has an additional arithmetic aspect:

- cardinality alone leaves a nominal nonlinear window;
- the interval-ratio slope family \(R_H\) may become rigid well before the
  half-direction threshold;
- a general proof must either construct nonlinear simultaneous-rainbow maps for
  a growing sequence of \((p,H)\), or avoid complete low-height slope protection
  altogether.

The next computational target is the first prime and height at which a
nonlinear protected permutation exists beyond the fixed-family cases already
covered by PX173.  The next theoretical target is a structural description of
permutation graphs whose missing direction set contains \(R_H\).

## Verification

Run

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_height_family_rigidity.cpp \
  -o /tmp/verify_height_rigidity
/tmp/verify_height_rigidity
```

The search is exact and uses 64-bit masks, so the recorded range is limited to
prime order at most 63.
