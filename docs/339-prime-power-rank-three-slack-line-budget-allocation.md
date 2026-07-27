# Rank-three slack allocates exact response-averaged line budgets

CMR1870--CMR1877 classify the exact rank-three slack

\[
S_3(G)=Z(G)-A_3(G).
\]

CMR1878--CMR1885 give the exact response-averaged line moments `z_1,z_2,z_3`.
This chapter combines them.  It separates the already-paid pure response-triple
numerator from the background-dependent rank-one and rank-two terms and gives an
exact integer budget for every strict host.

The statements concern a scalar self-row, or a labelled row after all displayed
coefficients have been evaluated against the chosen child weights.  Contributions
routed to different children must remain labelled and are not silently charged to
one scalar budget.

## 1. Exact residual geometric numerator

For a background height profile `h=(h_ell)`, define

\[
R_G(h)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
\right].
\]

### Theorem CMR1886 -- PROVED

The complete exact geometric numerator is

\[
\boxed{A_G(B)=A_3(G)+R_G(h).}
\]

### Proof

CMR1879 gives the exact linewise numerator.  Sum the `z_3` terms and use
CMR1881, which identifies their total with `A_3(G)`. ∎

### Theorem CMR1887 -- PROVED

On a rank-three-strict host, the complete scalar geometric row satisfies

\[
A_G(B)<Z(G)
\]

if and only if

\[
\boxed{R_G(h)\le S_3(G)-1.}
\]

### Proof

Substitute CMR1886 and use integer strictness:
`A_3+R<=Z-1` is equivalent to `R<=Z-A_3-1=S_3-1`. ∎

Thus `S_3-1` is not merely a residual total.  It is the exact denominator-cleared
budget for all background-dependent rank-one and rank-two self-contributions.

## 2. Line-budget allocation

### Theorem CMR1888 -- PROVED

For a strict host, the condition in CMR1887 is equivalent to the existence of
nonnegative integer line budgets `b_ell` satisfying

\[
\binom{h_\ell}{2}z_1(G,\ell)+h_\ell z_2(G,\ell)
\le b_\ell
\]

for every line and

\[
\boxed{\sum_\ell b_\ell\le S_3(G)-1.}
\]

### Proof

If the budgets exist, sum their linewise inequalities.  Conversely, when the
total criterion holds, choose each `b_ell` equal to its exact line cost. ∎

This form is useful for labelled state decomposition: a line or line class may be
assigned an explicit share of the parent slack, while all other owner and
provenance labels remain visible.

## 3. One-line residual profiles

Suppose a recurrent self-row retains the background-dependent coefficient of one
line `ell`, while all other such coefficients are absent, corrected away or
routed to already-accounted children.  If that line has background load `h`, put

\[
B_h(G,\ell)
=
\binom h2z_1(G,\ell)+h z_2(G,\ell).
\]

### Theorem CMR1889 -- PROVED

The one-line residual profile is strict after exact rank-three payment if and only
if

\[
\boxed{B_h(G,\ell)\le S_3(G)-1.}
\]

This theorem does not assert that an arbitrary geometric background has only one
nonzero line contribution.  It applies to an explicitly isolated line component
or to one line inside a verified allocation of CMR1888.

## 4. Load-one line census

For `h=1`,

\[
B_1(G,\ell)=z_2(G,\ell).
\]

A line is rank-two-active when `z_2>0`.

### Theorem CMR1890 -- PROVED

Across the 651 rank-three-strict raw hosts, the exact load-one census is:

| side | strict hosts | rank-two-active host-line pairs | pairs fitting `S_3-1` | hosts with at least one fitting active line | hosts whose every active line fits |
|---:|---:|---:|---:|---:|---:|
| 4 | 53 | 601 | 395 | 32 | 12 |
| 5 | 598 | 34,017 | 26,797 | 562 | 14 |
| **total** | **651** | **34,618** | **27,192** | **594** | **26** |

The fitting active pairs by grid-line length are:

| side | length 2 | length 3 | length 4 | length 5 |
|---:|---:|---:|---:|---:|
| 4 | 328 | 48 | 19 | -- |
| 5 | 21,166 | 4,571 | 935 | 125 |

### Proof

For every strict host and every line with `z_2>0`, evaluate `z_2<=S_3-1` and
tabulate by side and line length. ∎

Thus 78.55 percent of the rank-two-active host-line pairs fit inside the exact
rank-three residual budget.  This percentage is descriptive only; the exact
integer tables are the certificate data.

## 5. Load-two line census

For `h=2`,

\[
B_2(G,\ell)=z_1(G,\ell)+2z_2(G,\ell).
\]

A line is response-active when `z_1>0`.

### Theorem CMR1891 -- PROVED

The exact load-two census is:

| side | strict hosts | response-active host-line pairs | pairs fitting `S_3-1` | hosts with at least one fitting active line | hosts whose every active line fits |
|---:|---:|---:|---:|---:|---:|
| 4 | 53 | 1,934 | 676 | 32 | 0 |
| 5 | 598 | 70,258 | 16,162 | 460 | 0 |
| **total** | **651** | **72,192** | **16,838** | **492** | **0** |

The fitting active pairs by line length are:

| side | length 2 | length 3 | length 4 | length 5 |
|---:|---:|---:|---:|---:|
| 4 | 631 | 45 | 0 | -- |
| 5 | 14,852 | 1,252 | 39 | 19 |

### Proof

Evaluate `z_1+2z_2<=S_3-1` on every response-active line of every strict host and
tabulate. ∎

No strict raw host absorbs every possible response-active load-two line using
rank-three slack alone.  Therefore a universal load-two claim still needs actual
background-line localization, nonuniform child weights, correction or additional
row slack.

## 6. Weighted and labelled allocation

### Theorem CMR1892 -- PROVED

Let the exact line candidates be partitioned among labelled children, and let
`X_j>0` be fixed integer child weights.  Replace `z_1,z_2` by their corresponding
weighted labelled numerators on each line.  If the weighted pure rank-three
numerator has residual parent budget `S^{(X)}_3-1`, then the line-allocation
criterion of CMR1888 remains valid verbatim with the weighted line costs.

### Proof

The proof of CMR1888 uses only nonnegativity, additivity over labelled candidates
and integer strictness.  Weighting each child coefficient before summation
preserves all three properties. ∎

This is the form inserted into the labelled assignment manifest.  The scalar
census above applies directly only when the rank-three child has the normalized
parent weight or has already been evaluated against the chosen weight vector.

## 7. Line-budget endpoint

### Corollary CMR1893 -- PROVED

The 651 rank-three-strict hosts now have an exact host-line budget compiler.

1. Pure rank three is paid once through `A_3`.
2. Every remaining geometric self-coefficient is an exact line cost
   `C(h,2)z_1+h z_2`.
3. Strictness is the one integer inequality `sum line costs<=S_3-1`.
4. The same inequality may be published as explicit nonnegative line budgets.
5. Load-one active lines fit individually in 27,192 of 34,618 strict host-line
   cases.
6. Load-two active lines fit individually in 16,838 of 72,192 cases.
7. These individual fits do not replace the total budget when several line
   contributions remain in the same recurrent row.
8. The remaining task is to insert the actual background-height and labelled
   routing profile, not to recompute response probabilities.

All 740 hosts, exact line moments, 651 strict-host budgets, 80,602 strict
host-line pairs and the load-one/load-two tables are checked in
[`scripts/verify_prime_power_rank_three_slack_line_budget_allocation.py`](../scripts/verify_prime_power_rank_three_slack_line_budget_allocation.py).
