# Rank-one star decoding and exact short-cycle constants

PX225--PX227 reduce the ambient support-four obstruction to the square-root
scale, but their support-two and minimal-support constants were inherited from
the coarse pre-thinning weighted count.  On the retained block, these sectors
have exact combinatorial descriptions.

This chapter proves two improvements.

1. A candidate cell with large one-replacement/two-background weight is already
   the centre of an endpoint-disjoint secant star.  If no such star exists, the
   whole rank-one sector has linear expected load.
2. Rank-two transpositions and rank-three directed cycles have constant expected
   load by direct counting on the retained endpoint labels.

Let the retained endpoint block have order `s`.  Every diagonal candidate cell
is forbidden.  Let `Z` be the fixed background point set, disjoint from the
candidate grid, and suppose every line contains at most `K` points of `Z`.

## 1. Rank-one weight is a secant-star degree

For a candidate cell `f`, put

\[
\mu(f)
=
|\{\{z,z'\}\subseteq Z:
 f,z,z'\text{ are collinear}\}|.
\]

Thus the rank-one/two-background certificate weight is

\[
W_{1,2}
=
\sum_f\mu(f),
\]

where the sum runs over allowed-support candidate cells.

### Theorem PX228 -- PROVED

For every candidate cell `f`, there is an endpoint-disjoint secant star centred
at `f` with at least

\[
\boxed{
\frac{\mu(f)}K
}
\]

rays.

Consequently, for every integer `m>=1`, either:

1. some candidate cell centres an endpoint-disjoint star of order at least `m`;
   or
2. every candidate cell satisfies `mu(f)<Km`.

### Proof

Partition `Z` by the lines through `f`.  If one such line contains `r` background
points, it contributes `binom(r,2)` certificate pairs.  A matching on those `r`
points contains `floor(r/2)` endpoint-disjoint pairs, and

\[
\left\lfloor\frac r2\right\rfloor
\ge
\frac1r\binom r2
\ge
\frac1K\binom r2.
\]

Take such a matching independently on every line through `f`.  Distinct lines
through `f` have disjoint background vertices, so the union is an
endpoint-disjoint secant star.  Summing the displayed inequality over the lines
gives at least `mu(f)/K` rays. \(\square\)

No arithmetic information is needed: the rank-one obstruction is exactly the
clean-star geometry already handled by the recursive neutralization bank.

## 2. Linear rank-one load outside the star outcome

Let the forbidden-position graph on the retained block have maximum row and
column degree at most `Delta`, and let `M` be uniform on the allowed matching
family.

### Theorem PX229 -- PROVED

Fix `m>=1`.  If no candidate cell centres an endpoint-disjoint secant star of
order `m`, then

\[
\boxed{
W_{1,2}
<
Km\,s(s-1)
}
\]

and

\[
\boxed{
\mathbb E T_{1,2}
<
e^{4\Delta}Km(s-1).
}
\]

The same statement holds after compatible exposure, with the residual order in
place of `s` and the conditioned PX199 cylinder constant.

### Proof

PX228 gives `mu(f)<Km` for every candidate cell.  A rank-one support-two cell is
off diagonal, so there are at most `s(s-1)` such cells.  This proves the weight
bound.

PX196 bounds the probability of every allowed candidate cell by

\[
\frac{e^{4\Delta}}s.
\]

Multiply by the cell weights and sum. \(\square\)

Thus rank one has the exact decoder-or-linear form required by the recursive
program.  The remaining issue is quantitative: the present cylinder constant
may still be too large for strict descent at a chosen star threshold.

## 3. Exact minimal-support rank-two and rank-three bounds

Let `L_Z` be the maximum number of background anchors on one candidate secant
line.

### Theorem PX230 -- PROVED

The expected rank-two support-two transposition contribution satisfies

\[
\boxed{
\mathbb E T_{2,2}
\le
\frac12e^{4\Delta}L_Z.
}
\]

The expected internal rank-three support-three directed-cycle contribution
satisfies

\[
\boxed{
\mathbb E T_{3,3}
\le
\frac13e^{4\Delta}.
}
\]

### Proof

PX203 identifies rank-two support two with the transposition pairs

\[
\{e_{ij},e_{ji}\},
\qquad i<j.
\]

There are `binom(s,2)` such pairs and each has anchor weight at most `L_Z`.
PX196 bounds each rank-two cylinder by `e^(4Delta)/(s)_2`.  Therefore

\[
\mathbb E T_{2,2}
\le
L_Z\binom s2
\frac{e^{4\Delta}}{(s)_2}
=
\frac12e^{4\Delta}L_Z.
\]

PX203 also identifies rank-three support three with the two directed cycles on
each three-element endpoint set.  There are at most

\[
2\binom s3
=
\frac{(s)_3}{3}
\]

such candidate triples.  The collinear ones are a subfamily.  Apply the
rank-three cylinder bound `e^(4Delta)/(s)_3`. \(\square\)

This closes the two undamped short-cycle sectors at constant expected scale.

## 4. Exact support-three path coefficient

### Theorem PX231 -- PROVED

The rank-two support-three contribution satisfies

\[
\boxed{
\mathbb E T_{2,3}
\le
e^{4\Delta}L_Z(s-2).
}
\]

### Proof

PX205 identifies every support-three rank-two pattern with a directed path of
length two.  On `s` labels there are exactly

\[
s(s-1)(s-2)
=(s)_3
\]

such paths.  Every corresponding candidate pair lies on one secant line and
therefore has anchor weight at most `L_Z`.  Apply the rank-two cylinder bound:

\[
\mathbb E T_{2,3}
\le
L_Z(s)_3
\frac{e^{4\Delta}}{(s)_2}
=
e^{4\Delta}L_Z(s-2).
\]

\(\square\)

This replaces the earlier coefficient `256e^(4Delta)L_Z` from PX227 by the
exact direct-count coefficient `e^(4Delta)L_Z`.

## 5. Updated collateral ledger

On every retained block of order `s`:

- rank one either extracts an executable star or has expected load
  `O(e^(4Delta)Kms)`;
- rank-two support two is constant-scale;
- rank-two support three is linear with exact coefficient
  `e^(4Delta)L_Z`;
- rank-three support three is constant-scale;
- adaptive support four is at most `s/2` above the square-root ambient scale.

The minimal-support and rank-one asymptotic gaps are therefore closed.  The
remaining problem is exact net descent: sharpen the allowed-matching cylinder
constant or obtain larger guaranteed destruction from the loaded-line and
clean-star outcomes.

## 6. Verification

Run

```bash
python scripts/verify_product_rank_one_short_cycles.py
```

The verifier exhausts line-clique star extraction, exact transposition/path/
cycle populations, and the expected-load identities in PX229--PX231.
