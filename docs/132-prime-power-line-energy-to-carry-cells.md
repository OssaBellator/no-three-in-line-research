# From line-clean energy to prime-power carry cells

CMR354 forces many distinct real lines in one primitive-height band.  This
chapter converts those lines into the same prefix objects that drive the
prime-power repair theory.  A family of lines either concentrates at one
matching vertex, or it contains many pairwise matching-compatible secants.
The latter family has a common first-separation depth and projective direction,
and then either one full prefix cell is heavy or many full prefix cells are
occupied.

Let the inherited parent size be

\[
t=p^h.
\]

Fix a family `\mathfrak M` of `J` distinct nonaxis real lines.  On every line
choose one compatible candidate triple and then choose one of its three
compatible pairs.  A pair uses two source vertices and two target vertices.
Distinct chosen pairs determine distinct real lines, except that the same four
matching vertices can support the two crossed pairings; this harmless
multiplicity is absorbed in the degree count below.

## 1. Matching-vertex star or compatible pair matching

### Theorem CMR355 — PROVED

Let `Delta` be the largest number of chosen line pairs incident with one source
or target matching vertex.  Then at least one of the following holds.

1. **Matching-vertex fan.**  One source column or one target row is incident
   with `Delta` chosen line pairs.
2. **Compatible pair matching.**  There is a subfamily of at least
   \[
   \boxed{
   \left\lceil\frac{J}{4\Delta}\right\rceil
   }
   \]
   chosen pairs whose endpoint cells use pairwise distinct source and target
   vertices.

In particular, with

\[
A=\left\lceil\sqrt J\right\rceil,
\]

either one matching vertex is incident with at least `A` lines, or there is a
matching-compatible pair family of size at least

\[
\boxed{
\left\lfloor\frac{J}{4A}\right\rfloor.
}
\]

### Proof

Greedily choose one pair and delete every remaining pair sharing one of its
four matching vertices.  At most `4Delta` pair occurrences are removed at one
step.  The greedy process therefore selects at least `ceil(J/(4Delta))`
pairs.  If `Delta>=A`, the fan alternative holds.  Otherwise use
`Delta<A` and weaken the greedy bound to the displayed floor. ∎

A matching-vertex fan is already a localized source-row or target-column wall,
feeding the existing anchored and Hall-wall continuation machinery.  Continue
with the compatible-pair alternative.

## 2. First-separation extraction

Orient every compatible pair lexicographically and write its endpoint
difference as

\[
(\Delta x,\Delta y).
\]

Both coordinates are nonzero.  Put

\[
b=\min\{v_p(\Delta x),v_p(\Delta y)\},
\]

and let

\[
\theta=
[\Delta x/p^b:\Delta y/p^b]
\in\mathbb P^1(\mathbb F_p).
\]

### Theorem CMR356 — PROVED

Every matching-compatible family of `R` pairs contains a subfamily of size at
least

\[
\boxed{
\left\lceil\frac{R}{h(p+1)}\right\rceil
}
\]

with one common first-separation depth `b` and one common projective direction
`theta`.

### Proof

A distinct compatible pair has `0<=b<h`.  The projective line over
`F_p` has `p+1` directions.  Partition into the `h(p+1)` possible signatures
and pigeonhole. ∎

## 3. Full prefix-cell capacity

Fix a common-signature family `\mathcal E` of size `M`.  For its oriented first
endpoint `(x,y)`, record the full depth-`b` prefix cell

\[
(a,c)=(x\bmod p^b,y\bmod p^b).
\]

The second endpoint belongs to the same prefix cell because both coordinate
differences are divisible by `p^b`.

### Theorem CMR357 — PROVED

For every full prefix cell,

\[
\boxed{
\#\{e\in\mathcal E:\text{first endpoint of }e\text{ lies in the cell}\}
\le
\frac{t}{p^b}.
}
\]

Consequently

\[
\boxed{
\text{occupied cells}
\ge
\operatorname{ceil}\left(\frac{Mp^b}{t}\right)
}
\]

and some cell has load at least

\[
\boxed{
\operatorname{ceil}\left(\frac{M}{p^{2b}}\right).
}
\]

### Proof

The matching-compatible family uses distinct source and target vertices across
all endpoint cells.  A depth-`b` prefix cell contains only `t/p^b` source
columns, so it can contain at most that many oriented first endpoints.  This
gives the support bound.  There are `p^{2b}` full prefix cells, giving the
maximum-load bound. ∎

### Corollary CMR358 — PROVED

At least one of the following holds.

1. **Heavy full prefix cell.**  One cell contains at least
   \[
   \boxed{
   \operatorname{ceil}\left(\frac{M}{t^{2/3}}\right)
   }
   \]
   common-signature line pairs.
2. **Full-cell dispersion.**  The family occupies more than
   \[
   \boxed{
   \frac{M}{t^{2/3}}
   }
   \]
   distinct full prefix cells.

Every pair retains the same projective direction `theta`.

### Proof

If `p^b<=t^{1/3}`, CMR357 gives a cell of load at least

\[
M/p^{2b}\ge M/t^{2/3}.
\]

If `p^b>t^{1/3}`, the support bound gives more than

\[
Mp^b/t>M/t^{2/3}
\]

occupied cells. ∎

Every event in the heavy-cell alternative lies wholly in one depth-`b` prefix
block.  Its third collinear witness is routed by CMR340--CMR342 to the same
block, to a strictly deeper closest-pair block, or to the equilateral block.
Thus the heavy alternative is executable.  The dispersed alternative feeds the
absolute token ledger CMR344--CMR346.

## 4. Applying the conversion to the line-energy band

### Corollary CMR359 — PROVED

Assume the hypotheses of CMR354.  In the dyadic band supplied there, put

\[
J_0=
\left\lceil
\frac{11H^3}{90\lceil\log_2t\rceil}
\right\rceil,
\qquad
A_0=\left\lceil\sqrt{J_0}\right\rceil,
\]

\[
R_0=\left\lfloor\frac{J_0}{4A_0}\right\rfloor,
\qquad
M_0=\left\lfloor\frac{R_0}{h(p+1)}\right\rfloor.
\]

At least one of the following holds.

1. one matching vertex is incident with at least `A_0` distinct replacement
   lines in the band;
2. one full prefix cell carries at least
   \[
   \operatorname{ceil}\left(\frac{M_0}{t^{2/3}}\right)
   \]
   common-signature line pairs;
3. more than
   \[
   \frac{M_0}{t^{2/3}}
   \]
   full prefix cells are occupied by common-signature line pairs.

Ignoring floors and fixed-prime constants, the heavy or dispersed population
has size

\[
\boxed{
\Omega_p\left(
\frac{H^{3/2}}
{t^{2/3}(\log t)^{3/2}}
\right).
}
\]

### Proof

CMR354 gives at least `J_0` lines.  Apply CMR355 with threshold `A_0`.  In the
nonfan case retain at least `R_0` matching-compatible pairs.  CMR356 leaves at
least `M_0` pairs with common `(b,theta)`, and CMR358 gives the final two
alternatives.  The asymptotic form uses `h=log_p t`. ∎

This conversion closes the generic matching-space part of the intermediate
band.  A frozen line-clean bank can no longer end at an anonymous collection
of replacement triples: it exposes a matching-vertex wall, an executable heavy
prefix block, or a quantitatively dispersed family of absolute carry cells.
The remaining dynamic issue is bounded reuse of the dispersed cells and the
coarse-to-fine recreation ledger.

No all-`n` theorem is claimed here.  The star/matching extraction, signature
pigeonhole, cell capacities, and combined thresholds are checked in
[`scripts/verify_prime_power_line_energy_carry.py`](../scripts/verify_prime_power_line_energy_carry.py).
