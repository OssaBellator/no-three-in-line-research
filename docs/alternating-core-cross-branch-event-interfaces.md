# Cross-branch event interfaces for the AC5 menu router

**Branch:** `research/alternating-core-chain`

AC5ag--AC5ao reduce protected-safe menu selection to endpoint-cost Hall flows
and explicit threshold/cause capacities. This note imports four exact local
interfaces from the bounded-denominator, rational-inverse, superregular and
sparse-spread tracks. Every statement retains its physical hypotheses; none
asserts that an arbitrary AC menu automatically satisfies them.

## AC5ap -- bounded-left-hole endpoint-flow import -- PROVED

Let `Gamma subseteq A x B` be one AC candidate switching graph satisfying
Hall's condition. Assume every candidate source `a in A` excludes at most
`Delta` endpoints:

\[
|B\setminus N_\Gamma(a)|\le \Delta.
\]

Let `c:B -> Z_{>=0}` be the complete current/protected event cost and write
its values in nondecreasing order

\[
c_{(1)}\le\cdots\le c_{(|B|)}.
\]

If `|B|>=|A|+Delta`, then one saturating AC flow has cost at most

\[
\boxed{\sum_{i=1}^{|A|}c_{(i+\Delta)}.}
\]

In particular, if at least `|A|+Delta` endpoints have cost at most `t`, one
feasible stationary flow has average event cost at most `t`.

### Proof

For every nonempty `X subseteq A`,

\[
B\setminus N_\Gamma(X)
=
\bigcap_{a\in X}(B\setminus N_\Gamma(a))
\]

has size at most `Delta`. Hence every endpoint set `S` has matchable rank at
least `min{|A|,(|S|-Delta)_+}`. Apply the transversal-matroid greedy algorithm
to the endpoint cost order: by the time the first `i+Delta` endpoints are
scanned, at least `i` have been selected. The `i`-th selected endpoint costs
at most `c_(i+Delta)`. Summation proves the bound. QED.

## AC5aq -- diagonal BDA cause separation -- PROVED UNDER THE BDA DECODER HYPOTHESES

Consider one diagonal bounded-denominator channel comparison `(omega,omega)`
with distinct role parameters `u,v`.

1. For `omega in {A,B,C,D}`, either one role has at least half its weight on
   the anchor-ray wall, or the two non-wall context-pair families are
   disjoint and each retains more than half its role-side weight.
2. For `omega=CD`, the two full context-cell families lie on distinct parallel
   affine lines and are disjoint.
3. For `omega=AB`, both families lie on the original radial anchor line.

Consequently, away from the radial/wall route, the endpoint/cause inventory
has no cross-role duplication at a fixed context address:

\[
\boxed{
 m_{E_u\uplus E_v}(b)=\max\{m_{E_u}(b),m_{E_v}(b)\}.
}
\]

### Proof

For a one-local channel, collinearity with the same context pair at both role
parameters forces the context line to be the anchor ray. The `CD` equations
have distinct affine right-hand sides, while the `AB` equation is the radial
line independently of the role. The multiplicity identity follows from
disjoint support. QED.

## AC5ar -- bank-ready RI one-target event law -- PROVED UNDER THE PHYSICAL BLOCK HYPOTHESES

Let one installed RI block have `m` source cosets of subgroup order `h`. Let
`T_1` be a weighted multiset of one-target terminal records, each carrying one
complete physical source-coset, target-row-coset and shift prescription, and
put

\[
Q_1=\sum_{T\in T_1}c(T).
\]

Under the uniform I6 bank,

\[
\boxed{\mathbb E C_1=\frac{Q_1}{mh}.}
\]

A fixed context pair supports at most two target-hyperbola cells. For a
multistep AC path, summing the corresponding `Q_{1,s}/(m_sh_s)` over steps is
a valid protected-event contribution; no independence between steps is
required for this first-moment bound.

### Proof

One physical rank-one prescription fixes one permutation value and one shift,
so it occurs with probability `1/(mh)`. Weighted linearity of expectation gives
the display. A line meets the nondegenerate target hyperbola in at most two
points. Summing stepwise expectations proves the multistep assertion. QED.

## AC5as -- exact sparse structural failure alphabet -- PROVED

For a proposed one-layer matching swap at rows `i,j`, structural legality is
equivalent to the two cross host edges being present. For a two-layer simple
state, exactly two additional row-local noncollision inequalities are needed.
Thus the least structural failure of one proposed sparse swap is one of four
atoms:

1. first missing cross host edge;
2. second missing cross host edge;
3. first opposite-layer row collision;
4. second opposite-layer row collision.

For two disjoint swaps satisfying reversal and disjoint-transport invariance,
two base checks certify every side of the operation square. Therefore AC5's
cause router need not retain any further anonymous matching-validity cause;
all remaining sparse causes are arithmetic-word, line, boundary, owner or
context fields.

### Proof

Swapping two images preserves bijectivity and changes only the two cross
edges. In two layers, only the same two rows can acquire a duplicate cell.
The four displayed tests are therefore necessary and sufficient. Disjoint
involutive swaps commute, and transported legality certifies the opposite
square sides. QED.

## AC5at -- combined event-cost continuation -- PROVED UNDER THE DECLARED CONTRACTS

For any AC menu satisfying the bounded-left-hole hypothesis, build its exact
endpoint cost from:

- radial/wall BDA events routed separately and disjoint diagonal BDA events
  counted without cross-role duplication;
- bank-ready RI one-target costs `Q_1/(mh)` and the exact remaining RI cylinder
  costs;
- the four explicit sparse structural cause atoms and every nonstructural
  cause already present in AC5ao.

If the resulting shifted-quantile sum is strictly below `t|A|`, one feasible
stationary flow has average event cost below `t`. If not, the failure is now
localized to one of:

1. excessive left-hole degree or failure of Hall feasibility;
2. a radial/wall BDA output or an off-diagonal/higher-rank BDA profile;
3. a non-bank-ready or rank-at-least-two RI profile;
4. one exact sparse structural or nonstructural cause;
5. an already named AC5 high-event/blocker overload.

### Proof

AC5ap gives the flow comparison. AC5aq--AC5as give a complete accounting of
the imported event/cause terms under their contracts. Negating any required
hypothesis returns the corresponding named branch; otherwise the strict cost
inequality selects the desired flow. QED.

## Remaining AC5/AC6 work

This import does not prove a useful `Delta` for every AC menu, does not close
off-diagonal BDA or two-target RI events, and does not pay arithmetic or
context-sensitive sparse guards. It converts those gaps into explicit terms
of the existing AC5 event-cost and cause-capacity router.

## Finite check

`scripts/verify_ac_cross_branch_event_interfaces.py` checks the shifted-quantile
matching bound on small bounded-hole graphs, disjoint-role multiplicity,
`1/(mh)` RI prescriptions, and the exact four-atom sparse structural criterion.
