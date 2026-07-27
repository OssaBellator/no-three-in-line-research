# Line-energy profiles give an exact geometric offspring census

CMR1734--CMR1765 determine prescription multiplicities rank by rank. The same
geometry has a more compact linewise form. If a real line contains `h` background
points and `k` selected response points, then every new collinear triple on that
line is counted by one binomial difference.

This profile identity keeps the three residual ranks coupled. It also gives a
sharper background-potential charge: the congestion paid by one background
triple depends on the actual response load of its supporting line, not on the
full response side.

Let `B` and `Q` be disjoint finite point sets in the real affine plane. Write

\[
N=|B|,
\qquad
 d=|Q|.
\]

For each real line `ell`, put

\[
h_\ell=|B\cap\ell|,
\qquad
k_\ell=|Q\cap\ell|.
\]

Only lines with `h_ell+k_ell>=3` contribute below.

## 1. Exact linewise binomial identity

### Theorem CMR1766 -- PROVED

For every pair of nonnegative integers `h,k`,

\[
\boxed{
C(h+k,3)-C(h,3)
=
kC(h,2)+C(k,2)h+C(k,3).
}
\]

### Proof

A three-element subset of an `h+k` element set which is not entirely among the
first `h` elements contains exactly one, two or three elements from the final
`k` elements. The three cases give the terms on the right. ∎

The three summands are respectively the rank-one, rank-two and rank-three
response-prescription contributions.

## 2. Exact global line-energy census

Let

\[
\Psi(X)
=
|\{T\subseteq X:|T|=3\text{ and }T\text{ is collinear}\}|.
\]

### Theorem CMR1767 -- PROVED

The number of collinear triples in `B union Q` which are not entirely contained
in `B` is exactly

\[
\boxed{
\Psi(B\cup Q)-\Psi(B)
=
\sum_\ell
\left[
 k_\ell C(h_\ell,2)
 +C(k_\ell,2)h_\ell
 +C(k_\ell,3)
\right].
}
\]

### Proof

Every collinear triple lies on one unique real line. On each line apply CMR1766,
then sum over the finitely many lines containing at least three points of
`B union Q`. ∎

This is an exact geometric census, not an expectation or union bound.

## 3. Corrected genuinely-new row

Let `N_new(B,Q)` count any corrected family of genuinely new triples created by
installing `Q` over fixed background `B`.

### Theorem CMR1768 -- PROVED

\[
\boxed{
N_{\mathrm{new}}(B,Q)
\le
\Psi(B\cup Q)-\Psi(B).
}
\]

Equality holds when every triple in `B union Q` containing at least one response
point is genuinely new and retained in the row.

### Proof

Every corrected genuinely new triple is one of the triples counted by
CMR1767. Correction can only delete old, duplicated, contracted or otherwise
nonrecurrent triples. ∎

Hence the line-energy profile is an honest universal upper row.

## 4. Exact response-pair and response-triple identities

### Theorem CMR1769 -- PROVED

\[
\boxed{
\sum_\ell C(k_\ell,2)=C(d,2),
}
\]

and

\[
\boxed{
\sum_\ell C(k_\ell,3)=\Psi(Q).
}
\]

### Proof

Every unordered response pair determines one unique real line, proving the first
identity. Every collinear response triple lies on one unique real line, proving
the second. ∎

Thus the rank-two low-slot term has an exact global pair budget, while rank three
is the actual response triple count rather than the ambient `C(d,3)`.

## 5. Background-triple linewise charge

Define the pair-only incidence count

\[
R_2(B,Q)
=
\sum_{\ell:h_\ell=2}k_\ell.
\]

### Theorem CMR1770 -- PROVED

\[
\boxed{
N_{\mathrm{new}}(B,Q)
\le
R_2(B,Q)
+2C(d,2)
+\Psi(Q)
+
\sum_{\ell:h_\ell\ge3}
C(h_\ell,3)
\left[3k_\ell+C(k_\ell,2)\right].
}
\]

### Proof

In the exact line energy of CMR1767, apply

\[
C(h,2)\le \mathbf 1_{h=2}+3C(h,3)
\]

and

\[
h\le2+C(h,3)
\]

from CMR1750. Sum the two low rank-two slots using
CMR1769, and sum the rank-three term as `Psi(Q)`. Then apply CMR1768. ∎

The charge attached to one background triple depends only on the response load
of its own supporting line.

## 6. Maximum response-load specialization

Let

\[
K_3(B,Q)
=
\max\{k_\ell:h_\ell\ge3\},
\]

with maximum zero when `B` has no collinear triple.

### Theorem CMR1771 -- PROVED

\[
\boxed{
N_{\mathrm{new}}(B,Q)
\le
R_2(B,Q)
+2C(d,2)
+\Psi(Q)
+
\Psi(B)
\left[3K_3+C(K_3,2)\right].
}
\]

Moreover

\[
\boxed{R_2(B,Q)\le d\lfloor N/2\rfloor.}
\]

### Proof

The coefficient `3k+C(k,2)` is increasing in `k`, so bound every background-
triple line by `K_3`. The sum of `C(h_ell,3)` over all lines is `Psi(B)`.

For the pair-only term, fix one response point `x`. CMR1758--CMR1759 show that
its pair-only background secants form a matching of size at most `floor(N/2)`.
Sum over the `d` response points. ∎

This improves the potential-only coefficient whenever the actual response load
on background-triple lines is smaller than `d`.

## 7. Triple-free response specialization

### Theorem CMR1772 -- PROVED

If `Q` contains no collinear triple, then `Psi(Q)=0` and `K_3<=2`, so

\[
\boxed{
N_{\mathrm{new}}(B,Q)
\le
R_2(B,Q)+2C(d,2)+7\Psi(B).
}
\]

Consequently

\[
\boxed{
N_{\mathrm{new}}(B,Q)
\le
d\lfloor N/2\rfloor+2C(d,2)+7\Psi(B).
}
\]

If `B` is also triple-free, the final term vanishes.

### Proof

A triple-free response set has at most two points on every real line. Insert
`K_3<=2` and `Psi(Q)=0` into CMR1771. Since
`3*2+C(2,2)=7`, the displayed bound follows. ∎

This criterion is conditional on the chosen response itself being triple-free;
it does not assert that every matching host contains such a response.

## 8. Line-energy certificate endpoint

### Corollary CMR1773 -- PROVED

The geometric offspring frontier now has an exact line-profile compiler.

1. A profile `(h_ell,k_ell)` gives the exact uncorrected new-triple count.
2. Corrected genuinely new rows are dominated by that count.
3. Response-pair mass is exactly `C(d,2)` and response-triple mass is `Psi(Q)`.
4. Background-triple congestion is `3k_ell+C(k_ell,2)` on its own line.
5. The coarse potential coefficient uses the actual maximum response load `K_3`,
   not the full side `d`.
6. Triple-free responses have the explicit coefficient seven on current
   background triples.

The remaining work is to control `R_2(B,Q)`, `K_3(B,Q)` and `Psi(Q)` inside the
exact response host, either by geometric response selection, assignment/cover
bounds or canonical thin-host enumeration. No all-`n` theorem is claimed.

Exact line energies, rank decompositions, pair/triple identities and charged
bounds are checked in
[`scripts/verify_prime_power_line_energy_profile_census.py`](../scripts/verify_prime_power_line_energy_profile_census.py).
