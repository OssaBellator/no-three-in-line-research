# Exact rank-three response energy on all side-four and side-five fibres

CMR1798--CMR1805 expand the matching denominator classes into 740 exact
coordinate-labelled hosts.  The rank-three line-energy term is independent of
the background set, so it can be completed immediately on every one of those
hosts.

For an executable raw host `G_X`, let

\[
Z(G_X)=|\operatorname{PM}(G_X)|
\]

and define the exact uniform rank-three numerator

\[
A_3(G_X)
=
\sum_{Q\in\operatorname{PM}(G_X)}\Psi(Q),
\]

where `Psi(Q)` is the number of collinear triples contained in the response
matching `Q`.  Thus the rank-three expectation is `A_3/Z`.

## 1. Response-level triple values

### Theorem CMR1806 -- PROVED

Across every executable raw side-four and side-five host, every response matching
has

\[
\boxed{
\Psi(Q)\in\{0,1,2,4\}.
}
\]

More precisely:

| side | `Psi(Q)=0` | `Psi(Q)=1` | `Psi(Q)=2` | `Psi(Q)=4` |
|---:|---:|---:|---:|---:|
| 4 | 137 | 34 | 0 | 35 |
| 5 | 4116 | 4115 | 548 | 275 |

### Proof

Enumerate every perfect matching of every executable raw host and count its
collinear triples by the exact determinant test.  The displayed counts include
all 206 side-four response occurrences and all 9054 side-five response
occurrences. ∎

In particular, no response in the corrected fibre census contains more than four
collinear triples.

## 2. Hostwise maximum response energy

### Theorem CMR1807 -- PROVED

The distribution of the maximum response-triple count within one raw host is:

### Side four

\[
\boxed{
37\text{ hosts with maximum }0,
\quad
14\text{ with maximum }1,
\quad
35\text{ with maximum }4.
}
\]

### Side five

\[
\boxed{
116\text{ hosts with maximum }1,
\quad
263\text{ with maximum }2,
\quad
275\text{ with maximum }4.
}
\]

### Proof

Take the maximum of `Psi(Q)` over the exact response list of every raw host and
tabulate. ∎

Thus every side-four/five rank-three row has the deterministic cap `4`, improving
the ambient values `C(4,3)=4` and `C(5,3)=10`; the improvement is substantial on
side five.

## 3. Triple-free host count

### Corollary CMR1808 -- PROVED

Exactly

\[
\boxed{37}
\]

raw side-four hosts have only triple-free responses, so their rank-three line-
energy term vanishes identically.

No raw side-five host has an identically zero rank-three term.

### Proof

The rank-three term vanishes exactly when the hostwise maximum in CMR1807 is zero.
Read the two distributions. ∎

The side-five conclusion does not say that every side-five response has a triple;
4116 individual response occurrences are triple-free by CMR1806.

## 4. Exact side-four numerator table

### Theorem CMR1809 -- PROVED

For raw side-four hosts, the exact denominator-specific maximum rank-three
numerators are:

| denominator `Z` | raw hosts | maximum `A_3` | sharp maximum expectation |
|---:|---:|---:|---:|
| 1 | 14 | 4 | `4` |
| 2 | 40 | 5 | `5/2` |
| 3 | 20 | 5 | `5/3` |
| 4 | 9 | 5 | `5/4` |
| 5 | 2 | 5 | `1` |
| 6 | 1 | 5 | `5/6` |

Each maximum is attained.

### Proof

Group the 86 raw hosts by exact response denominator and maximize the integer sum
`A_3=sum_Q Psi(Q)` in each group. ∎

Hence every side-four fibre has the exact integer cap shown in its denominator
row, rather than the uniform coarse cap `A_3<=4Z`.

## 5. Exact side-five numerator table

### Theorem CMR1810 -- PROVED

For raw side-five hosts, the exact denominator-specific maximum rank-three
numerators are:

| `Z` | raw hosts | max `A_3` | max expectation |
|---:|---:|---:|---:|
| 8 | 21 | 10 | `5/4` |
| 9 | 18 | 10 | `10/9` |
| 10 | 93 | 14 | `7/5` |
| 11 | 48 | 11 | `1` |
| 12 | 104 | 15 | `5/4` |
| 13 | 30 | 14 | `14/13` |
| 14 | 111 | 15 | `15/14` |
| 15 | 50 | 15 | `1` |
| 16 | 63 | 16 | `1` |
| 17 | 12 | 15 | `15/17` |
| 18 | 24 | 17 | `17/18` |
| 19 | 15 | 16 | `16/19` |
| 20 | 45 | 16 | `4/5` |
| 22 | 6 | 18 | `9/11` |
| 24 | 1 | 16 | `2/3` |
| 25 | 6 | 19 | `19/25` |
| 26 | 6 | 20 | `10/13` |
| 33 | 1 | 23 | `23/33` |

Each maximum is attained.

### Proof

Group the 654 raw side-five hosts by denominator and maximize the exact integer
rank-three numerator in each group. ∎

This table is directly insertable into every corrected geometric fibre row before
background-dependent coefficients are computed.

## 6. Sharp uniform expectation caps

### Theorem CMR1811 -- PROVED

Every raw side-four host satisfies

\[
\boxed{A_3\le4Z,}
\]

and this is sharp.

Every raw side-five host satisfies

\[
\boxed{5A_3\le7Z,}
\]

and this is sharp at denominator `Z=10`, numerator `A_3=14`.

### Proof

Take the maximum expectation in the denominator tables CMR1809--CMR1810 and clear
denominators. ∎

For most denominators the table gives a strictly stronger integer cap than the
uniform inequality.

## 7. Aggregate census totals

### Theorem CMR1812 -- PROVED

Across all raw hosts, counting response occurrences with their host multiplicity:

### Side four

\[
\boxed{
206\text{ responses},
\qquad
174\text{ total response triples}.
}
\]

### Side five

\[
\boxed{
9054\text{ responses},
\qquad
6311\text{ total response triples}.
}
\]

Thus the occurrence-weighted aggregate expectations are `87/103` and
`6311/9054`, respectively.

### Proof

Sum the response counts and `Psi(Q)` values over every raw host. ∎

These aggregate fractions are census checks, not substitutes for hostwise
certificates.

## 8. Rank-three fibre endpoint

### Corollary CMR1813 -- PROVED

The background-independent rank-three geometric fibre row is complete through
side five.

1. Every response contains at most four collinear triples.
2. Thirty-seven side-four hosts have rank-three row zero.
3. Every denominator has a sharp integer numerator cap.
4. Side five has the sharp uniform expectation cap `7/5`, replacing ambient rank
   mass `C(5,3)=10`.
5. Exact host numerators remain preferable and are already finite table entries.
6. The remaining geometric fibre work is rank one and rank two, plus corrected
   provenance routing of the resulting triples.

No all-`n` theorem is claimed.

All 740 raw hosts, 9260 response occurrences, exact triple counts, host maxima and
denominator-specific numerator caps are checked in
[`scripts/verify_prime_power_exact_rank_three_geometric_fibre_census.py`](../scripts/verify_prime_power_exact_rank_three_geometric_fibre_census.py).
