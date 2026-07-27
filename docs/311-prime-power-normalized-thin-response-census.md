# Exact normalized thin-response census through side five

CMR1654--CMR1661 normalize every fixed-interface response board to

\[
O=I_d,
\qquad
e=(0,1),
\]

and quotient deleted partial matchings by the residual `S_{d-2}` stabilizer.
This chapter executes that normalized host census through side five.  It counts
every deleted partial matching in the extension-free host, discards boards with
no perfect matching, computes exact response denominators, and checks every
extendable rank-one and rank-two prescription.

The census concerns matching response probabilities.  It does not by itself
bound every geometric offspring count.  It closes sides two and three at the
matching level and gives exact probability caps for the unresolved side-four and
side-five fixed-interface rows.

For each `d`, put

\[
H_d
=
K_{d,d}\setminus(I_d\cup\{(0,1)\}).
\]

Let `X` range over all partial matchings contained in `H_d`, and define

\[
G_X=H_d\setminus X.
\]

Two deletions are identified only when they lie in the same residual
`S_{d-2}` orbit fixing the labels `0` and `1`.

## 1. Raw and canonical host counts

### Theorem CMR1662 -- PROVED

The complete normalized counts through side five are:

| side `d` | partial matchings `X` | executable raw hosts | canonical executable orbits |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 0 |
| 3 | 13 | 4 | 4 |
| 4 | 86 | 86 | 45 |
| 5 | 654 | 654 | 124 |

### Proof

Enumerate partial matchings recursively by deciding each allowed edge while
retaining source and target disjointness.  Test executability by exact perfect-
matching enumeration.  Canonicalize every executable deletion under the
`S_{d-2}` action of CMR1657--CMR1658. ∎

The side-four and side-five extension-free hosts survive every partial-matching
deletion in this normalized family, in agreement with CMR1510--CMR1517.

## 2. Exact response-denominator distributions

### Theorem CMR1663 -- PROVED

The perfect-matching counts on canonical executable hosts have the following
exact distributions.

### Side three

\[
\boxed{4\text{ hosts with }1\text{ response}.}
\]

### Side four

\[
\boxed{
\begin{array}{c|rrrrrr}
|\operatorname{PM}(G_X)|&1&2&3&4&5&6\\\hline
\#\text{ orbits}&7&20&10&6&1&1
\end{array}}
\]

### Side five

\[
\boxed{
\begin{array}{c|rrrrrrrrrrrrrrrrrr}
|\operatorname{PM}(G_X)|
&8&9&10&11&12&13&14&15&16&17&18&19&20&22&24&25&26&33\\\hline
\#\text{ orbits}
&4&3&16&8&21&5&19&9&15&2&4&3&8&2&1&2&1&1
\end{array}}
\]

### Proof

For every canonical host, enumerate all permutations and retain those avoiding
the forbidden board.  Count the surviving perfect matchings and tabulate the
results. ∎

These integers are the exact common denominators for uniform fixed-interface
response rows on the corresponding hosts.

## 3. Side two has no extension-free response

### Theorem CMR1664 -- PROVED

For `d=2`, even the undeleted normalized host

\[
K_{2,2}\setminus(I_2\cup\{(0,1)\})
\]

has no perfect matching.  Hence no side-two target-avoiding extension-free row
exists.

### Proof

After deleting the identity matching and `(0,1)`, only the edge `(1,0)` remains.
It cannot cover both source vertices. ∎

Side two must therefore terminate through a contraction, fixed core or another
structural branch before this response family is invoked.

## 4. Side three is completely forced

### Theorem CMR1665 -- PROVED

Every executable normalized side-three host has exactly one perfect matching.
Across the four canonical hosts there are exactly

\[
\boxed{12}
\]

extendable rank-one prescriptions and

\[
\boxed{12}
\]

extendable rank-two prescriptions.  Every one has probability one.

### Proof

Use the denominator census of CMR1663 and enumerate every compatible rank-one
or rank-two partial matching.  A prescription is extendable exactly when it is
contained in the unique response. ∎

Thus side-three fixed-interface prescriptions are forced common prescriptions
and belong to the exact contraction branch.  There is no genuinely stochastic
side-three fixed-interface diagonal row.

## 5. Side-four nonforced prescription caps

A prescription is **forced** when it occurs in every perfect matching of its
host.  Forced rank-one or rank-two prescriptions enter the existing exact
contraction branch and need not remain in a stochastic recurrent row.

### Theorem CMR1666 -- PROVED

Across the 45 canonical side-four hosts:

1. there are `313` extendable rank-one prescription instances, of which `66` are
   forced;
2. there are `613` extendable rank-two prescription instances, of which `55` are
   forced;
3. every nonforced rank-one prescription satisfies
   \[
   \boxed{\Pr(P\subseteq Q)\le\frac34;}
   \]
4. every nonforced rank-two prescription satisfies
   \[
   \boxed{\Pr(P\subseteq Q)\le\frac23.}
   \]

Both displayed caps are attained.

### Proof

Compute the exact numerator by counting response matchings containing each
prescription and divide by the host denominator.  Separate numerator equal to
the denominator from the nonforced cases and maximize the remaining exact
fractions. ∎

## 6. Side-five nonforced prescription caps

### Theorem CMR1667 -- PROVED

Across the 124 canonical side-five hosts:

1. there are `1971` extendable rank-one prescription instances;
2. there are `9374` extendable rank-two prescription instances;
3. none is forced;
4. every rank-one prescription satisfies
   \[
   \boxed{\Pr(P\subseteq Q)\le\frac23;}
   \]
5. every rank-two prescription satisfies
   \[
   \boxed{\Pr(P\subseteq Q)\le\frac25.}
   \]

Both displayed caps are attained.

### Proof

Use the exact numerator/denominator census as in CMR1666.  The smallest side-five
host denominator is eight, but the extremal fractions arise on other canonical
hosts.  Exhaustive enumeration gives the stated maxima and no numerator equal
to its denominator. ∎

These caps are stronger than the trivial probability-one bound and may be
inserted directly into fixed-interface class capacities and selector capacity
gaps.

## 7. Exact capacity consequences

Let a side-four or side-five fixed-interface class contain `N_1` corrected
rank-one prescriptions and `N_2` corrected rank-two prescriptions.

### Theorem CMR1668 -- PROVED

After removing forced contractions, the following uniform expectation bounds
hold.

### Side four

\[
\boxed{
A_{\rm interface}
\le
\frac34N_1+\frac23N_2.
}
\]

### Side five

\[
\boxed{
A_{\rm interface}
\le
\frac23N_1+\frac25N_2.
}
\]

After clearing the exact host denominator, these become integer class capacities
for the CMR1646--CMR1653 selector gap compiler and exact row bounds for the
CMR1618 thin-table compiler.

### Proof

Sum the prescription probability caps of CMR1666 or CMR1667 over the corrected
class.  Forced side-four prescriptions have already been routed to contraction. ∎

The bound is additive only within one current response row; historical
interface episodes are not treated as simultaneous.

## 8. Thin-census endpoint

### Corollary CMR1669 -- PROVED

The normalized fixed-interface/thin frontier through side five now has the
following exact status.

1. Side two has no extension-free target-avoiding response.
2. Every executable side-three host has a unique response, so all positive
   rank-at-most-two prescriptions contract.
3. Side four has 45 canonical executable hosts and exact nonforced probability
   caps `3/4` and `2/3` in ranks one and two.
4. Side five has 124 canonical executable hosts and exact caps `2/3` and `2/5`.
5. All response denominators are explicitly tabulated and can be used for strict
   integer capacity and Lyapunov certificates.

The remaining thin-table work begins with geometric offspring enumeration on
these canonical hosts, followed by larger required sides if the structural
reductions do not already exit.  No all-`n` theorem is claimed.

Canonical host counts, denominator distributions, forced contractions and all
`12,295` extendable rank-one/rank-two prescription instances are checked in
[`scripts/verify_prime_power_normalized_thin_response_census.py`](../scripts/verify_prime_power_normalized_thin_response_census.py).
