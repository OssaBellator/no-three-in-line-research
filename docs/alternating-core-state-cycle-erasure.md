# Monotone-mask state-cycle erasure and canonical cross signatures

**Branch:** `research/alternating-core-chain`

The residual AC4 quotient after AC3hw still allows same-denominator changes of
rank/channel, context, external role and bank type. Two generic matching facts
remove a large part of that residual graph. First, inside one epoch whose
unavailable-resource mask only grows, exact repetition of the ordered two-layer
state is cycle-erasable. Second, every nontrivial change of one permutation layer
has a canonical local cross around one removed cell. The symmetric-difference
component through that cell is either the exact four-cell rectangle already
covered by a capacity-one ticket, or a genuinely long alternating cycle.

The state-cycle statement is the two-layer specialization of the monotone-mask
principle used on the all-`n` composite-modulus branch. The cross-signature and
rectangle/long-cycle refinement are proved here in the alternating-core
notation.

## Epoch model

Let

\[
S=(M^0,M^1)
\]

be an ordered pair of disjoint permutation graphs on `[n] x [n]`. Let `R` be a
finite resource universe and let `F subseteq R` be the current unavailable mask.
A state is feasible at mask `F` when it avoids every resource forbidden by `F`.

A **monotone-mask epoch** is a history

\[
(S_0,F_0),(S_1,F_1),\ldots,(S_m,F_m)
\]

such that

\[
F_0\subseteq F_1\subseteq\cdots\subseteq F_m,
\]

every `S_i` is feasible at `F_i`, the outside arithmetic/context label is fixed,
and every later transition rule and terminal test depends only on the current
ordered state, current mask and that fixed outside label.

## AC3hx -- exact two-layer state-cycle erasure -- PROVED

If

\[
S_i=S_j\qquad(i<j),
\]

then the segment from `i` to `j` is erasable. More precisely, replace
`(S_i,F_i)` directly by

\[
(S_i,F_j)
\]

and replay every operation after time `j`. Every later selected state and every
terminal classification remain unchanged.

Consequently a shortest history reaching a prescribed terminal output inside
one fixed epoch contains no repeated ordered two-layer state and has fewer than

\[
\boxed{(n!)^2}
\]

nonterminal state occurrences.

If only one local block state repeats, then either the outside state changed or
the intervening segment is erasable.

### Proof

Since `S_i=S_j` and `S_j` is feasible under `F_j`, the identical state `S_i` is
feasible under `F_j`. The pair `(S_i,F_j)` is therefore exactly the state/mask
input present at time `j`. The Markovian epoch hypothesis allows every later
operation to be replayed verbatim. A repeated state in a shortest history would
contradict minimality. There are at most `n!` choices for each labelled
permutation layer. The local-block statement follows by comparing the outside
components. QED.

The factorial bound is deliberately qualitative. AC4 still needs polynomial
payment or a structural return for long sequences of distinct states.

## Canonical cross of a nontrivial layer change

Let `M,M'` be distinct permutation graphs. Order physical cells once and for all.
Choose the least removed cell

\[
e=(u,v)\in M\setminus M'.
\]

Since `M'` is a permutation, it has unique cells

\[
r_y=(u,y),\qquad y\ne v,
\]

in column `u`, and

\[
c_x=(x,v),\qquad x\ne u,
\]

in row `v`. The two cells are distinct. For an ordered two-layer transition,
choose the least changed layer `ell` and perform this construction there.

If the transition carries one of `L` finite role labels `lambda`, define

\[
\Sigma_{\rm ch}
=(\ell,e,r_y,c_x,\lambda).
\]

## AC3hy -- finite cross-signature stock -- PROVED

Every nontrivial ordered two-layer state change has one canonical cross
signature. For an alphabet of `L` role labels, all signatures lie in a universe
of size

\[
\boxed{
N_{\rm ch}(n,L)
=2L n^2(n-1)^2.
}
\]

The set of signatures actually realized by canonical least-cell selection may be
smaller; `N_ch` is the exact ambient stock used for recurrence bounds.

For any `J` transition episodes in one fixed epoch and any integer
`lambda_0>=2`, either one signature occurs at least `lambda_0` times, or

\[
\boxed{
J\le(\lambda_0-1)N_{\rm ch}(n,L).
}
\]

### Proof

Choose the changed layer in two ways, the removed cell `e` in `n^2` ways, the
new row in column `u` in `n-1` ways, the new column in row `v` in `n-1` ways,
and the role in `L` ways. The canonical construction gives existence and
uniqueness. These choices enumerate the ambient signature universe; canonical
least-cell selection may use only a subset. The recurrence bound is
weighted-free pigeonhole on this safe stock. QED.

A weighted version is immediate: one signature carries at least
`1/N_ch(n,L)` of the total episode weight. This is historical transition weight,
not simultaneous bank payment.

## AC3hz -- rectangle or genuinely long alternating cycle -- PROVED

Let

\[
p=(x,y).
\]

Consider the symmetric-difference component of `M triangle M'` containing the
removed cell `e=(u,v)`.

Exactly one of the following holds.

1. **Rectangle component.** `p in M`. The component is exactly the four-cycle
   whose old diagonal is `{e,p}` and whose new diagonal is `{r_y,c_x}`.
2. **Long alternating component.** `p notin M`. The component has length at
   least six.

In the rectangle case the canonical cross signature determines the complete
four-cell support. Reversing the local change has the same unordered rectangle
address, so every AC rectangle realization consumes the existing capacity-one
rectangle ticket.

### Proof

In the bipartite row-column representation, `e` is incident with column `u` and
row `v`. In `M'`, the alternating component leaves those vertices through
`r_y=(u,y)` and `c_x=(x,v)`. It closes after four edges exactly when `M` contains
the edge joining the remaining vertices `x` and `y`, namely `p=(x,y)`. If not,
the alternating cycle cannot close at length four; every nontrivial matching
symmetric-difference component is an even cycle, so its length is at least six.
The ticket statement follows because the reverse move has the same four cells
and opposite diagonal assignment. QED.

## AC3ia -- recurrent cross router and cell churn -- PROVED

Fix one monotone-mask epoch and one role alphabet of size `L`. Let `J` be the
number of nontrivial selected-state changes after exact state cycles have been
erased.

For every threshold `lambda_0>=2`, one of the following holds.

1. **Polynomially bounded nonrecurrence:**
   \[
   J\le(\lambda_0-1)2Ln^2(n-1)^2.
   \]
2. **Repeated rectangle address:** one canonical rectangle signature occurs at
   least `lambda_0` times. Unticketed recurrence is impossible after the first
   realization because every traversal consumes the same capacity-one rectangle
   ticket.
3. **Fixed-cross long-cycle core:** one exact tuple
   \[
   (\ell,e,r_y,c_x,\lambda)
   \]
   occurs in at least `lambda_0` transitions whose canonical symmetric-difference
   component has length at least six.
4. **Epoch/context change:** the outside context or monotone-mask epoch changes,
   so the occurrences are not members of one fixed signature stock.

Moreover, if one fixed signature removing `e` occurs `r` times along a linear
history, then the layer-cell `e` is reinserted at least

\[
\boxed{r-1}
\]

times between those episodes.

### Proof

Apply AC3hy within a fixed epoch. A repeated signature is rectangle or long by
AC3hz. Rectangle recurrence consumes the same ticket. For repeated removal of
`e`, the cell is absent immediately after each episode and must be present before
the next episode with the same signature; therefore at least one absent-to-present
reinsertion occurs between consecutive episodes. QED.

## Interface to the all-n branches

The three all-`n` branches have different current strengths.

- `research/all-n-prime-patching` has the strongest asymptotic patch architecture.
  Its matchable non-superregular hosts factor over alternating SCCs; high mobility
  gives cycle banks, while low mobility gives feedback hubs, cycle stars or
  two-hub theta cores. AC3ia's long-cycle output is the exact local shape needed
  for that interface, but delegation is valid only after the prime-patching
  source-credit and host hypotheses are verified.
- `research/all-n-composite-modulus` proves monotone-mask cycle erasure, exact
  matching churn and polynomial signature-ancestry ledgers inside prime-power
  envelopes. AC3hx is the general two-layer import that does not use prime-power
  arithmetic.
- `research/all-n-product-construction` supplies exact finite witnesses and SAT
  reductions for product hosts, but currently has no stronger general
  state-recurrence theorem to import into AC4.

No all-`n` branch is claimed to close AC4 or AC6 by itself.

## Consequence

After AC3hw and AC3hx--AC3ia, a residual same-denominator cycle cannot hide as an
exact selected-state loop or an unlabelled matching change. It must leave one of
these explicit outputs:

- a new canonical cross signature;
- a ticketed rectangle address;
- a fixed-cross long alternating-cycle core;
- repeated reinsertion of one exact layer-cell;
- or a genuine epoch/outside-context change.

The next AC4 target is payment and finite ancestry for the fixed-cross long-cycle
and cell-reinsertion outputs, together with physical realization of the retained
carry/BDA/RI role.

## Finite check

`scripts/verify_ac_state_cycle_erasure.py` exhausts permutation changes through
side six, checks canonical cross uniqueness and the ambient stock, verifies the
rectangle-versus-long-cycle criterion from symmetric-difference components,
checks monotone-mask cycle erasure on small abstract hosts, exhausts recurrence
pigeonholes, and verifies that repeated removal of one signature forces
intervening reinsertion.
