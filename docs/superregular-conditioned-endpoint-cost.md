# Conditioned endpoint-cost stability by local neighbourhood loss

**Branch:** `research/superregular-resampling`

SRR2j--SRR2m express the minimum endpoint cost of a Hall flow as a sum of
sublevel matching deficiencies.  A bounded remote partial matching does not need
to be treated as a global hole set.  Its exact effect is the loss of low-cost
endpoint neighbours in the switching graph.

## Conditioned switching graph

Let `G=(A,S,E)` be a balanced bipartite switching graph with an integer endpoint
cost

\[
c:S\to\{0,1,\ldots,C\}.
\]

Let `G'` be the graph after conditioning on a remote partial matching.  Thus
`G'` has the same vertex sets and only deletes switching edges that are no longer
feasible.  Assume both graphs admit perfect matchings.

For `1<=t<=C`, put

\[
S_{<t}=\{s\in S:c(s)<t\}
\]

and define the exact sublevel deficiency

\[
\delta_t(G)
=
\max_{X\subseteq A}
\bigl(|X|-|N_G(X)\cap S_{<t}|\bigr)_+.
\]

Define the threshold neighbourhood loss

\[
b_t(G,G')
=
\max_{X\subseteq A}
\left(
|N_G(X)\cap S_{<t}|
-
|N_{G'}(X)\cap S_{<t}|
\right).
\]

## SRR2n -- sublevel deficiency is Lipschitz under conditioning -- PROVED

For every threshold `t`,

\[
\boxed{
\delta_t(G')
\le
\delta_t(G)+b_t(G,G').
}
\]

### Proof

For every `X subseteq A`,

\[
|X|-|N_{G'}(X)\cap S_{<t}|
\le
|X|-|N_G(X)\cap S_{<t}|+b_t(G,G').
\]

Take positive parts and then the maximum over `X`. QED.

## SRR2o -- exact conditioned min-cost drift bound -- PROVED

Let `Phi(G,c)` be the minimum total endpoint cost of a perfect matching in `G`.
Then

\[
\boxed{
\Phi(G',c)
\le
\Phi(G,c)
+
\sum_{t=1}^C b_t(G,G').
}
\]

### Proof

SRR2k--SRR2l give the exact layer-cake formula

\[
\Phi(G,c)=\sum_{t=1}^C\delta_t(G)
\]

and the same identity for `G'`.  Sum SRR2n over thresholds. QED.

This is often much sharper than charging every host hole: only lost neighbours
inside the actual low-event sublevel sets contribute.

## SRR2p -- local conditioning-incidence bound -- PROVED

Suppose the remote partial matching contains `k` fixed assignments.  For each
threshold `t`, assume one fixed assignment can remove at most `mu_t` distinct
vertices from `N_G(X) cap S_{<t}` for every `X`.  Then

\[
\boxed{
b_t(G,G')\le k\mu_t
}
\]

and consequently

\[
\boxed{
\Phi(G',c)
\le
\Phi(G,c)+k\sum_{t=1}^C\mu_t.
}
\]

### Proof

Expose the fixed assignments one at a time.  At threshold `t`, each exposure
reduces any low-cost neighbourhood by at most `mu_t`.  Telescope and apply
SRR2o. QED.

The hypothesis is an event-incidence statement.  For rank-two and rank-three
geometric cylinders, `mu_t` is to be proved from their actual coordinate
support, not from the total number of missing host cells.

## SRR2q -- robust low-cost Hall criterion after conditioning -- PROVED

If the unconditioned graph satisfies

\[
|N_G(X)\cap S_{<t}|
\ge
|X|+\sigma_t
\]

for every nonempty `X` with `|X|<=|A|-sigma_t`, and
`b_t(G,G')<=sigma_t`, then no new threshold-`t` deficiency is created on those
sets.  Any new deficiency must lie in the explicitly retained large-set
boundary range.

### Proof

Subtract the neighbourhood-loss bound from the displayed slack inequality.
The conditioned low-cost neighbourhood still has size at least `|X|`. QED.

## SRR2r -- conditioned event-flow interface -- PROVED UNDER THE DECLARED
INCIDENCE CONTRACT

For a declared current/protected rank-two or rank-three event inventory, a
bounded remote partial matching changes the optimal endpoint objective by at
most the sum of its threshold-local neighbourhood losses.  Hence one may prove
the required reverse-scale inequality by either:

1. the original unconditioned min-cost bound plus
   `k sum_t mu_t`;
2. robust sublevel expansion with slack `sigma_t`;
3. or one explicit threshold set where the local incidence bound fails.

The remaining SRR2 frontier is geometric: construct bounded-cycle switching
graphs with small `mu_t` and sublevel deficiency for the actual event cylinders,
and extend the same accounting through two-layer multistep kernels.

## Finite check

`scripts/verify_srr_conditioned_endpoint_cost.py` samples more than ten thousand
pairs of finite switching graphs, computes minimum perfect-matching costs by
brute force, verifies the exact sublevel-deficiency formula and checks the
conditioned Lipschitz bound.
