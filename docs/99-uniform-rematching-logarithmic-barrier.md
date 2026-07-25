# Uniform neutralization banks have logarithmic internal collateral

PX74, PX77, and PX80 neutralize every first-generation endpoint of the
rectangle transposition decoder.  All three use the same replacement measure:
a uniformly random perfect matching in a \(t\times t\) bipartite graph obtained
by deleting a forbidden-position set of row and column degree at most two.

This chapter proves that such a uniform bank has an intrinsic logarithmic
rank-three cost on arithmetic row and column sets.  Consequently the
first-generation expectation argument cannot by itself close the repair route
when the destroyed mass is only linear in \(t\).

The result is a barrier to the **uniform rematching measure**, not an
impossibility theorem for every biased or structured rematching family.

Let

\[
R=C=\{0,1,\ldots,t-1\}
\]

and let \(F\subseteq R\times C\) have row and column degree at most two.  Put

\[
G=(R\times C)\setminus F.
\]

A compatible triple means three cells of \(G\) with distinct rows and distinct
columns.

## Theorem PX183 -- PROVED

For all sufficiently large \(t\), the graph \(G\) contains at least

\[
\boxed{c\,t^4\log t}
\]

compatible collinear triples, where \(c>0\) is an absolute constant.

Thus the rank-three certificate count \(T_3\) in each of PX74, PX77, and PX80
can have order \(t^4\log t\) even after both forbidden partial matchings are
removed.

### Proof

First count triples in the complete grid.  For every positive primitive
direction

\[
(a,b),
\qquad
1\le a,b\le t/16,
\]

and positive integers \(r,s\), use triples

\[
x,
\qquad
x+r(a,b),
\qquad
x+(r+s)(a,b).
\]

Restrict to

\[
r+s\le\frac{t}{4h},
\qquad
h=\max(a,b).
\]

Every such choice has at least \(t^2/4\) valid starting points.  The number of
positive pairs \((r,s)\) in the range is

\[
\Omega\left(\frac{t^2}{h^2}\right).
\]

Hence one primitive direction of height \(h\) contributes

\[
\Omega\left(\frac{t^4}{h^2}\right)
\]

triples.  There are \(2\varphi(h)\) positive primitive directions of height
\(h>1\).  The standard totient estimate

\[
\sum_{h\le H}\frac{\varphi(h)}{h^2}
=\frac6{\pi^2}\log H+O(1)
\]

therefore gives

\[
\Omega(t^4\log t)
\]

compatible collinear triples in the full grid.  The use of positive nonaxis
directions guarantees distinct rows and columns.

It remains to bound the triples removed by \(F\).  Fix one grid cell.  For a
primitive direction of height \(h\), its line contains \(O(t/h)\) grid points,
so the number of triples on that line containing the fixed cell is

\[
O(t^2/h^2).
\]

There are \(O(h)\) primitive directions of height \(h\), giving

\[
O\left(t^2\sum_{h\le t}\frac1h\right)
=O(t^2\log t)
\]

collinear triples through one cell.  Since

\[
|F|\le2t,
\]

all forbidden cells together meet only

\[
O(t^3\log t)
\]

triples.  This is lower order than the complete-grid count, proving the
claim. \(\square\)

## 2. Every candidate triple has nonnegligible bank probability

Let \(\Omega_F\) be the set of perfect matchings of \(G\), and choose a matching
uniformly.  The AN1 counting theorem used in PX73 and PX76 gives

\[
|\Omega_F|\ge\frac{t!}{128}
\]

when \(t\ge7\).

## Theorem PX184 -- PROVED

Assume \(t\ge10\).  Every compatible nonforbidden partial matching \(E\) of
three cells satisfies

\[
\boxed{
\Pr_{M\in\Omega_F}(E\subseteq M)
\ge
\frac1{128(t)_3}.
}
\]

Consequently the expected number of internally collinear triples in the uniform
replacement matching obeys

\[
\boxed{
\mathbb E\,\Phi_{\rm internal}(M)
\ge c' t\log t
}
\]

for an absolute \(c'>0\) and all sufficiently large \(t\).

### Proof

Fix \(E\).  Delete its three source rows and three target columns.  The inherited
forbidden-position set still has row and column degree at most two.  Since the
remaining order is \(t-3\ge7\), AN1 supplies at least

\[
\frac{(t-3)!}{128}
\]

allowed completions containing \(E\).

The total number of allowed matchings is at most \(t!\).  Therefore

\[
\Pr(E\subseteq M)
\ge
\frac{(t-3)!/128}{t!}
=
\frac1{128(t)_3}.
\]

Sum this lower bound over the \(\Omega(t^4\log t)\) candidate triples from
PX183. \(\square\)

## 3. Consequence for first-generation neutralization

For the clean-star and moderate radial-core banks, the guaranteed destroyed
mass can be only

\[
D_*=\Theta(t).
\]

The loaded-line bank can also have linear destroyed mass when the loaded line
has bounded occupancy per moved endpoint.  PX184 shows that the same uniform
replacement bank may create

\[
\Omega(t\log t)
\]

internal triples on arithmetic row and column sets.

Therefore no proof which uses only

1. the uniform degree-two-forbidden matching measure;
2. the linear first-generation destruction estimate; and
3. first-moment comparison of the ordinary triple count

can establish universal improvement.

A successful second-generation theorem must add at least one genuinely new
ingredient:

- a nonuniform rematching distribution suppressing arithmetic collinear
  triples;
- a multiscale potential which discounts diffuse high-direction collateral;
- a batch neutralizing \(\Omega(t\log t)\) old mass at once; or
- a recursive repair process applied inside the replacement matching.

This explains why the exact subpower strong-complete seeds PX169--PX170 do not
automatically close PX74/PX77/PX80: those seeds live on a globally affine field
coordinate system, whereas the movable row and column sets in a decoder
endpoint are arbitrary subsets of the scalar grid.

## Verification

Run

```bash
python scripts/verify_product_uniform_rematching_log_barrier.py
```

For the canonical forbidden set consisting of the identity and cyclic-shift
partial matchings, the verifier computes exact uniform-bank expectations through
\(t=12\).  The ratio

\[
\frac{\mathbb E\Phi_{\rm internal}}{t\log t}
\]

increases from approximately \(0.115\) at \(t=8\) to \(0.130\) at \(t=12\).
It also checks the logarithmic primitive-direction sum numerically.
