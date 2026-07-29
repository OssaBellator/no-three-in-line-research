# Second frontier import for AC5 event and cause routing

**Branch:** `research/alternating-core-chain`

AC5ap--AC5at import bounded-hole endpoint flows, diagonal BDA separation,
bank-ready RI rank-one costs and the atomic single-swap structural alphabet.
This note adds the next three exact interfaces: bounded-rank conditioning,
bank-ready RI rank-two secants and one-row-overlapping sparse swap words.

## AC5au -- conditioned quantile import -- PROVED

Let one AC switching graph `Gamma subseteq A x B` satisfy Hall's condition and
suppose each source excludes at most `Delta` endpoints.  Let a compatible remote
or protected assignment delete a fixed endpoint set `D` of size `k`, and assume
the conditioned graph `Gamma[A,B\D]` still satisfies Hall's condition.

If the endpoint event costs on `B\D` are ordered as

\[
c'_{(1)}\le\cdots\le c'_{(|B|-k)},
\]

then, whenever `|B|-k>=|A|+Delta`, one conditioned saturating flow has cost at
most

\[
\boxed{\sum_{i=1}^{|A|}c'_{(i+\Delta)}.}
\]

In the original global order the safe bound is

\[
\boxed{\sum_{i=1}^{|A|}c_{(i+\Delta+k)}.}
\]

### Proof

Inside the surviving endpoint set, conditioning introduces no new host hole;
each source still excludes at most `Delta` surviving endpoints.  Apply AC5ap to
the conditioned graph.  Deleting `k` ordered endpoints moves the `j`-th survivor
rightward by at most `k`. QED.

## AC5av -- bank-ready RI rank-two event law -- PROVED UNDER THE PHYSICAL
## BLOCK HYPOTHESES

Let an installed RI block have `m` source cosets of subgroup order `h`.  Let
`T_2` be a weighted multiset of two-target secant records whose two prescriptions
use distinct source cosets and distinct target row cosets, and put

\[
Q_2=\sum_{T\in T_2}c(T).
\]

Under the uniform I6 bank,

\[
\boxed{\mathbb E C_2=\frac{Q_2}{(m)_2h^2}.}
\]

One fixed secant address determines its unordered target pair uniquely.
Repeated source or target cosets are evaluated with their actual lower-rank
correlation law.

### Proof

A compatible rank-two prescription fixes two permutation images and two shifts,
leaving `(m-2)!h^(m-2)` states among `m!h^m`.  Weighted linearity gives the
expectation.  The secant determines target-column sum and product, hence the
unordered pair. QED.

## AC5aw -- overlapping sparse structural alphabet -- PROVED

For two matching swaps sharing exactly one row, fix distinct rows `i,j,k` and
apply `sigma_ij` followed by `sigma_jk`.  The final first-layer images are

\[
\pi(j),\quad\pi(k),\quad\pi(i)
\]

at rows `i,j,k`.  Structural legality is equivalent to:

1. the three corresponding cross host edges are present;
2. in two layers, none of those three new edges equals the opposite-layer edge
   in its row.

Thus the least structural failure belongs to an exact six-atom alphabet.  If
all six tests pass, every remaining failure is arithmetic, collinearity,
boundary, owner, payment or context data.

### Proof

The composition is a three-cycle on distinct current images and therefore
preserves bijectivity.  Only three host edges and three row-local duplicate-cell
conditions change. QED.

## AC5ax -- strengthened bank-ready conditioned continuation -- PROVED UNDER
## THE DECLARED CONTRACTS

For a conditioned AC menu satisfying AC5au, include in its exact endpoint cost:

- bank-ready RI one-target weight `Q_1/(mh)`;
- bank-ready distinct-coset two-target weight `Q_2/((m)_2h^2)`;
- every exact remaining RI cylinder cost;
- the four one-swap and six shared-row two-swap sparse structural atoms;
- all BDA and other AC5 event terms already retained by AC5at.

If the conditioned shifted-quantile sum is below `t|A|`, one conditioned
stationary flow has average event cost below `t`.  Otherwise failure is
localized to Hall loss under conditioning, excessive `Delta+k`, a non-bank-ready
or rank-three RI profile, an off-diagonal/higher-rank BDA output, one exact
sparse structural/nonstructural cause, or an existing AC5 overload.

### Proof

Use AC5au for the conditioned flow, AC5av for rank-two RI collateral, AC5aw for
the structural cause alphabet, and AC5at for the previously imported terms.
QED.

## Remaining AC5/AC6 work

The bank-ready terminal RI interaction audit is now exact through rank two, and
bounded-rank conditioning costs only an additive endpoint-quantile shift.
Remaining work is rank-three or non-bank-ready RI collateral, quantitative Hall
survival and low-cost endpoint abundance for actual menus, off-diagonal BDA
profiles, and arithmetic/geometric sparse guards.

## Finite check

`scripts/verify_ac_second_frontier_import.py` checks conditioned quantile bounds,
rank-two I6 counts and shared-row three-cycle structural legality on small
instances.
