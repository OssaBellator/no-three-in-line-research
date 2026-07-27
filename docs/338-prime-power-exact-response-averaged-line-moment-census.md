# Exact response-averaged line moments sharpen the geometric host compiler

The occupancy-capacity compiler bounds each real line by the largest load attained
by any response.  For a uniform response law one can instead retain the complete
response distribution on every line.  This chapter records the resulting exact
integer numerators and executes the census on all 740 raw side-four/five hosts.

For an exact response host `G`, put

\[
Z(G)=|\operatorname{PM}(G)|.
\]

For every nonaxis real grid line `ell` and `r=1,2,3`, define

\[
z_r(G,\ell)
=
\sum_{Q\in\operatorname{PM}(G)}
\binom{|Q\cap\ell|}{r}.
\]

These are denominator-cleared response-averaged line moments.  They differ from
`Z C(tau_G(ell),r)`: the latter replaces every response by the linewise maximum.

## 1. Exact linewise numerator

### Theorem CMR1878 -- PROVED

If a fixed background has load

\[
h_\ell=|B\cap\ell|
\]

on line `ell`, then the exact response-summed contribution of that line is

\[
\boxed{
\sum_{Q\in\operatorname{PM}(G)}
\left[
 |Q\cap\ell|\binom{h_\ell}{2}
 +\binom{|Q\cap\ell|}{2}h_\ell
 +\binom{|Q\cap\ell|}{3}
\right]
=
\binom{h_\ell}{2}z_1(G,\ell)
+h_\ell z_2(G,\ell)
+z_3(G,\ell).
}
\]

### Proof

Distribute the finite sum over responses across the three binomial terms and use
the definition of `z_r`. ∎

### Corollary CMR1879 -- PROVED

The complete exact uniform-response numerator is

\[
\boxed{
A_G(B)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
 +z_3(G,\ell)
\right].
}
\]

Hence

\[
\mathbb E[\Psi(B\cup Q)-\Psi(B)]=A_G(B)/Z(G).
\]

This is the linewise form of the exact rook-marginal numerator.  No incompatible
line maxima are combined.

## 2. Global pair and triple identities

Define

\[
N_r(G)=\sum_\ell z_r(G,\ell).
\]

### Theorem CMR1880 -- PROVED

For response side `d`,

\[
\boxed{N_2(G)=Z(G)\binom d2.}
\]

### Proof

Fix one response matching `Q`.  Its selected cells have distinct first and second
coordinates, so every unordered pair lies on one unique nonaxis real line.
Therefore

\[
\sum_\ell\binom{|Q\cap\ell|}{2}=\binom d2.
\]

Sum over the `Z(G)` responses. ∎

Thus the global denominator-cleared rank-two moment is independent of the
embedded host once `d` and `Z` are fixed.

### Theorem CMR1881 -- PROVED

Let `A_3(G)` be the exact uniform rank-three numerator of CMR1809--CMR1810.  Then

\[
\boxed{N_3(G)=A_3(G).}
\]

### Proof

For one response `Q`, every collinear response triple lies on one unique nonaxis
line, so

\[
\sum_\ell\binom{|Q\cap\ell|}{3}=\Psi(Q).
\]

Sum over all responses. ∎

Consequently only `N_1` remains a genuinely free global moment after the exact
denominator and rank-three numerator are known.

## 3. Relation to rook marginals and occupancy capacities

### Theorem CMR1882 -- PROVED

For every line,

\[
z_1(G,\ell)=\sum_{e\in\ell}z(e),
\]

\[
z_2(G,\ell)=
\sum_{\substack{P\subseteq\ell\\|P|=2}}z(P),
\]

and

\[
z_3(G,\ell)=
\sum_{\substack{P\subseteq\ell\\|P|=3}}z(P),
\]

where `z(P)` is the exact contracted response count and only compatible,
extendable prescriptions contribute.

### Proof

Both sides count pairs `(Q,P)` with `P` an `r`-element prescription contained in
`Q` and on `ell`.  Count first by response or first by prescription. ∎

This gives two interchangeable compilers: enumerate responses directly or reuse
the contracted rook table.

### Theorem CMR1883 -- PROVED

For every line and `r=1,2,3`,

\[
\boxed{
z_r(G,\ell)
\le
Z(G)\binom{\tau_G(\ell)}r.
}
\]

Therefore the exact averaged numerator of CMR1879 is at most `Z(G)` times the
deterministic occupancy-capacity row of CMR1816.

### Proof

Every response has `|Q cap ell|<=tau_G(ell)`.  The binomial coefficient is
nondecreasing on nonnegative integers.  Sum over responses, then insert the three
linewise inequalities into CMR1879. ∎

The inequality is frequently strict because different line maxima occur in
different responses.

## 4. Exact uniform-height envelopes

If every relevant background line has load at most `H`, define the exact averaged
host score

\[
\overline F_H(G)
=
\binom H2N_1(G)+HN_2(G)+N_3(G).
\]

### Theorem CMR1884 -- PROVED

For every such background,

\[
\boxed{A_G(B)\le\overline F_H(G).}
\]

Moreover the 740 raw hosts compress denominator-by-denominator as follows.

| side | raw hosts | exact denominators | Pareto triples `(N_1,N_2,N_3)` | integer-height-active triples |
|---:|---:|---:|---:|---:|
| 4 | 86 | 6 | 13 | 11 |
| 5 | 654 | 18 | 90 | 37 |

Thus only

\[
\boxed{48}
\]

exact moment triples are worst for at least one integer height cap.

Every exact side-four envelope is terminal by `H=2`.  Every exact side-five
envelope is terminal by `H=4`.

The terminal data are:

### Side four

| `Z` | Pareto | active | terminal from `H` | terminal `(N_1,N_2,N_3)` |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | `(32,6,0)` |
| 2 | 4 | 2 | 2 | `(64,12,0)` |
| 3 | 2 | 2 | 2 | `(93,18,1)` |
| 4 | 2 | 2 | 2 | `(122,24,1)` |
| 5 | 2 | 2 | 2 | `(148,30,4)` |
| 6 | 1 | 1 | 0 | `(177,36,5)` |

### Side five

| `Z` | Pareto | active | terminal from `H` | terminal `(N_1,N_2,N_3)` |
|---:|---:|---:|---:|---:|
| 8 | 5 | 2 | 2 | `(492,80,3)` |
| 9 | 3 | 2 | 2 | `(544,90,6)` |
| 10 | 9 | 2 | 2 | `(616,100,4)` |
| 11 | 4 | 2 | 2 | `(667,110,7)` |
| 12 | 9 | 2 | 2 | `(738,120,5)` |
| 13 | 7 | 2 | 2 | `(791,130,6)` |
| 14 | 9 | 2 | 2 | `(860,140,6)` |
| 15 | 8 | 3 | 3 | `(913,150,7)` |
| 16 | 6 | 2 | 2 | `(982,160,7)` |
| 17 | 5 | 3 | 3 | `(1023,170,7)` |
| 18 | 6 | 2 | 2 | `(1092,180,9)` |
| 19 | 4 | 2 | 2 | `(1150,190,10)` |
| 20 | 3 | 2 | 2 | `(1207,200,14)` |
| 22 | 4 | 2 | 2 | `(1329,220,11)` |
| 24 | 1 | 1 | 0 | `(1416,240,16)` |
| 25 | 3 | 2 | 2 | `(1501,250,17)` |
| 26 | 3 | 3 | 4 | `(1551,260,16)` |
| 33 | 1 | 1 | 0 | `(1956,330,23)` |

### Proof

Apply `h_ell<=H` termwise in CMR1879.  Enumerate the exact triples, discard
componentwise dominated triples only within one denominator class, and evaluate
the remaining quadratic integer scores.  Terminality follows by checking the
score and its forward difference against every competitor at the displayed
height. ∎

Compared with the maximum-occupancy moment compiler, the exact averaged uniform
frontier falls from 57 active triples to 48 and its latest terminal height falls
from sixteen to four.

## 5. Exact averaged endpoint

### Corollary CMR1885 -- PROVED

The side-four/five geometric compiler now has an exact response-averaged layer.

1. Every raw host and every nonaxis line has exact integer moments `z_1,z_2,z_3`.
2. Arbitrary background height profiles enter the exact dot product of CMR1879.
3. The global pair moment is `Z C(d,2)` and the global triple moment is `A_3`.
4. Exact line moments are obtainable either from responses or contracted rook
   numerators.
5. Occupancy capacities remain a valid upper fallback but never improve the exact
   averaged row.
6. Uniform-height classes require only 48 active exact moment triples through side
   five.
7. Owner, collision, correction and provenance labels are not erased by this
   host-only averaging; they must still be attached to the corresponding
   prescription coefficients.

No all-`n` conclusion is claimed.  The next use is to combine exact line moments
with the rank-three slack budgets and actual background/provenance fibres.

All 740 hosts, 89,664 host-line moment triples, 1,188,144 response-line
occurrences, 537,984 line-height identities, global pair/triple identities,
Pareto classes and terminal envelopes are checked in
[`scripts/verify_prime_power_exact_response_averaged_line_moments.py`](../scripts/verify_prime_power_exact_response_averaged_line_moments.py).
