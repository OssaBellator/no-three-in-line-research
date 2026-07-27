# Exact rank-three fibre slack localizes the remaining side-four/five rows

CMR1806--CMR1813 compute, for every raw side-four/five geometric response host,
its exact response denominator

\[
Z(G)=|\operatorname{PM}(G)|
\]

and its exact uniform rank-three numerator

\[
A_3(G)=\sum_{Q\in\operatorname{PM}(G)}\Psi(Q).
\]

This chapter classifies the integer slack

\[
S_3(G)=Z(G)-A_3(G).
\]

The classification concerns the scalar rank-three self-contribution.  Other
return, selector, rank-one, rank-two and provenance-routed terms must still be
inserted into the complete labelled row.

## 1. Exact residual numerator budget

### Theorem CMR1870 -- PROVED

Let `B(G)` be any additional nonnegative integer numerator on the same uniform
response denominator.  Then

\[
\frac{A_3(G)+B(G)}{Z(G)}<1
\]

if and only if

\[
\boxed{B(G)\le S_3(G)-1.}
\]

Consequently a host with `S_3>0` has exact residual integer budget `S_3-1` after
paying its complete rank-three self-contribution.

### Proof

The strict inequality is equivalent to the integer inequality
`A_3+B<=Z-1`.  Rearranging gives `B<=Z-A_3-1=S_3-1`. ∎

This budget may be spent only on terms represented in the same current row and
denominator.

## 2. Side-four slack distribution

### Theorem CMR1871 -- PROVED

Among the 86 raw side-four hosts:

\[
\boxed{
53\text{ have }S_3>0,
\qquad
6\text{ have }S_3=0,
\qquad
27\text{ have }S_3<0.
}
\]

The exact slack distribution is:

| `S_3` | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| raw hosts | 11 | 12 | 4 | 6 | 21 | 24 | 8 |

### Proof

Compute `Z-A_3` from the exact response list of every raw side-four host and
tabulate.  The counts sum to 86. ∎

## 3. Side-five slack distribution

### Theorem CMR1872 -- PROVED

Among the 654 raw side-five hosts:

\[
\boxed{
598\text{ have }S_3>0,
\qquad
38\text{ have }S_3=0,
\qquad
18\text{ have }S_3<0.
}
\]

The exact slack distribution is:

| `S_3` | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| raw hosts | 1 | 1 | 6 | 10 | 38 | 36 | 67 | 89 | 112 | 84 | 96 | 53 | 39 | 14 | 6 | 2 |

### Proof

Compute `Z-A_3` on all 654 raw side-five hosts.  The displayed counts sum to
654. ∎

The largest exact residual rank-three slack through side five is eleven.

## 4. Denominator-localized strict, critical and excess hosts

### Theorem CMR1873 -- PROVED

The exact sign counts by response denominator are:

### Side four

| `Z` | strict `S_3>0` | critical `S_3=0` | excess `S_3<0` |
|---:|---:|---:|---:|
| 1 | 12 | 0 | 2 |
| 2 | 26 | 0 | 14 |
| 3 | 11 | 0 | 9 |
| 4 | 2 | 5 | 2 |
| 5 | 1 | 1 | 0 |
| 6 | 1 | 0 | 0 |

### Side five

| `Z` | strict | critical | excess |
|---:|---:|---:|---:|
| 8 | 15 | 3 | 3 |
| 9 | 17 | 0 | 1 |
| 10 | 76 | 10 | 7 |
| 11 | 42 | 6 | 0 |
| 12 | 90 | 10 | 4 |
| 13 | 26 | 3 | 1 |
| 14 | 105 | 4 | 2 |
| 15 | 49 | 1 | 0 |
| 16 | 62 | 1 | 0 |
| 17 | 12 | 0 | 0 |
| 18 | 24 | 0 | 0 |
| 19 | 15 | 0 | 0 |
| 20 | 45 | 0 | 0 |
| 22 | 6 | 0 | 0 |
| 24 | 1 | 0 | 0 |
| 25 | 6 | 0 | 0 |
| 26 | 6 | 0 | 0 |
| 33 | 1 | 0 | 0 |

Every host of side five with denominator at least seventeen is rank-three strict.

## 5. Automatic rank-three-only elimination

### Corollary CMR1874 -- PROVED

Across the complete 740-host layer,

\[
\boxed{651}
\]

hosts have `A_3<Z`.  Therefore every scalar recurrent module whose only retained
self-contribution is the exact rank-three response row is already strictly
subcritical on those hosts.

### Proof

Add the 53 strict side-four hosts and 598 strict side-five hosts.  On each such
host the scalar row sum is `A_3/Z<1`. ∎

This does not eliminate a complete host row when other recurrent terms remain.
It supplies their exact residual budget from CMR1870.

## 6. Critical and excess localization

### Theorem CMR1875 -- PROVED

The non-strict rank-three host set has exactly

\[
\boxed{44\text{ critical hosts and }45\text{ excess hosts}.}
\]

1. On a critical host, any positive additional scalar self-numerator destroys a
   row-sum-below-one certificate unless correction or labelled routing removes
   some rank-three contribution.
2. On an excess host, the uncorrected rank-three scalar row already exceeds one;
   a successful certificate must use corrected offspring deletion, nontrivial
   child weights, off-diagonal routing or a sharper exact state decomposition.
3. No host with side-five denominator at least seventeen belongs to this set.

### Proof

Add the exact sign counts of CMR1871--CMR1873 and apply CMR1870. ∎

Thus the difficult rank-three part is localized to 89 explicit raw hosts rather
than all 740.

## 7. Slack-aware unified outer score

### Theorem CMR1876 -- PROVED

On a strict host, suppose all remaining denominator-cleared return, bounded
selector, rank-one and rank-two contributions are certified by one integer outer
dual objective `B`.  The complete scalar row is strict whenever

\[
\boxed{B\le S_3-1.}
\]

Equivalently, the exact rank-three numerator may be removed from the outer search
and its integer slack used as the parent budget.

### Proof

Insert the exact rank-three numerator into CMR1870.  The remaining terms are
nonnegative and share the same denominator after clearing. ∎

For labelled rows, the rank-three child weights may differ, so the full
label-weighted manifest remains authoritative.  This scalar slack compiler applies
when the rank-three term returns to the same normalized child weight or has already
been evaluated against the chosen weights.

## 8. Rank-three slack endpoint

### Corollary CMR1877 -- PROVED

The background-independent rank-three frontier through side five is now divided
exactly into:

1. 651 strict hosts with explicit residual integer budgets;
2. 44 critical hosts requiring zero additional scalar self-load or a correction;
3. 45 excess hosts requiring correction, routing or nontrivial labelled weights;
4. 89 total hosts requiring special rank-three attention;
5. no non-strict side-five host above denominator sixteen.

The next host computation may therefore prioritize the 89 non-strict hosts and
spend the exact `S_3-1` budget on shorter-line rank-one/rank-two and return-selector
terms for the other 651.

All hostwise numerators, sign classes, denominator tables and residual-budget
identities are checked in
[`scripts/verify_prime_power_rank_three_fibre_slack_classification.py`](../scripts/verify_prime_power_rank_three_fibre_slack_classification.py).
