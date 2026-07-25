# Fixed-cross return ancestry and long alternating-cycle interfaces

**Branch:** `research/alternating-core-chain`

AC3ia leaves two related historical outputs inside one monotone-mask epoch:
a fixed-cross long alternating-cycle core and repeated reinsertion of the exact
layer-cell removed by that core.  This note gives the next exact reduction.

The first part is unconditional.  A fixed cell has only a polynomial stock of
role-labelled rectangle return addresses.  Once those capacity-one tickets are
spent, repeated reinsertion forces a long return cycle, and one exact return
cross repeats.

The second part is a deliberately scoped import of the alternating-SCC
technology on `research/all-n-prime-patching`.  When many returned cycles are
simultaneously available relative to one current matching and one current host,
directed Menger gives either a genuine one-hub cycle-star menu or a two-hub
separator core.  The cycle-star is an executable paid menu whenever the common
removed cell carries the private pivot payment already supplied by
AC3gg--AC3gj.

No historical alternatives from different current hosts are silently combined.

## Return crosses

Fix one layer `ell`, one physical cell

\[
e=(u,v),
\]

and one role alphabet of size `L`.  Suppose a fixed AC3ia removal signature

\[
\sigma=(\ell,e,r_y,c_x,\lambda)
\]

occurs `r` times in one linear history.  Between consecutive removals of `e`,
choose the first transition which reinserts `e`.

For such a transition `M -> M'`, inspect the reverse change `M' -> M`, in which
`e` is removed.  Its row and column neighbours define the **return cross**

\[
\tau=(\ell,e,\widehat r,\widehat c,\lambda_{\rm ret}).
\]

There are at most

\[
T_{\rm ret}=L(n-1)^2
\]

return-cross signatures for fixed `ell,e`.

## AC3ig -- finite rectangle returns or one repeated long return -- PROVED

Among the `r-1` selected reinsertion transitions, at most

\[
\boxed{T_{\rm ret}=L(n-1)^2}
\]

can be rectangle returns whose unordered rectangle ticket has not previously
been consumed.

Consequently at least

\[
\boxed{(r-1-T_{\rm ret})_+}
\]

selected returns have a symmetric-difference component through `e` of length at
least six.  One exact return cross occurs on at least

\[
\boxed{
\left\lceil
\frac{(r-1-T_{\rm ret})_+}{T_{\rm ret}}
\right\rceil
}
\]

of those long returns.

### Proof

Apply AC3hz to the reverse of each selected reinsertion.  A rectangle return is
determined by its fixed-cell return cross, and the reverse and forward
realizations have the same unordered four-cell support.  Its capacity-one
rectangle ticket permits at most one traversal.  There are at most
`T_ret` return crosses.

Every remaining return is long by AC3hz.  Pigeonhole the long returns over the
same `T_ret` signatures. QED.

Thus repeated cell churn is not an unlabelled event.  It yields either finite
ticket expenditure or a **two-cross history profile** consisting of one fixed
long removal cross and one fixed long return cross.

## Static common-host hypothesis

The historical conclusion above does not by itself make the cycles
simultaneous.  For the next interface fix:

- one current permutation matching `M`;
- one current allowed-edge host `K` containing `M`;
- one current matching edge `e in M`;
- a family `C` of directed alternating cycles of the exchange digraph of
  `(K,M)`, every one containing `e`;
- one private current pivot bucket through the cell `e`, of certified weight
  `W_e`.

Switching a cycle means replacing the reference edges of that cycle by its
off-diagonal edges.  Every switched state is required to remain disjoint from
the unchanged opposite permutation layer; this is part of the current host
`K`, not an inferred property.

## AC3ih -- cycle-star or two-hub separator -- PROVED

For every integer `p>=2`, exactly one of the following Menger alternatives is
available.

1. There are `p` cycles in `C` whose vertex sets intersect pairwise only at the
   hub represented by `e`.
2. There is a set `U` of fewer than `p` nonhub exchange vertices meeting every
   cycle in `C`.

If `t` distinct cycles are represented, the separator alternative contains one
vertex lying with the hub on at least

\[
\boxed{\frac{t}{p-1}}
\]

cycles.

### Proof

Delete the hub, split every remaining exchange vertex into an in-copy and an
out-copy joined by a capacity-one arc, give every transformed host arc infinite
capacity, and connect the outgoing and incoming neighbours of the hub to a
source and sink.  Source--sink paths are exactly hub cycles with the hub
deleted.  Integral max flow gives `p` internally vertex-disjoint paths or a
vertex cut of size below `p`.  In the cut case, pigeonhole the `t` cycles over
fewer than `p` cut vertices. QED.

The second output is an exact two-hub resource profile.  It retains the layer,
both cross signatures, both hub resources, the arithmetic role and the current
epoch label.

## AC3ii -- executable one-hub cycle-star menu -- PROVED

Assume the first alternative of AC3ih and write the cycles as

\[
\Gamma_1,\ldots,\Gamma_p.
\]

For state `j`, switch only `Gamma_j`.  Then:

1. every state is a permutation matching of `K`;
2. every state removes the current cell `e`;
3. every state destroys the complete private pivot bucket of certified weight
   `W_e`;
4. outside `e`, the removed and inserted matching resources of distinct states
   are disjoint;
5. every specific inserted off-diagonal edge occurs in at most one state, and
   hence has probability at most `1/p` under the uniform menu.

### Proof

An alternating-cycle switch preserves all row and column resources.  Pairwise
intersection only at the hub makes all nonhub resources disjoint.  The two
cycle edges incident with the hub are also distinct between petals, since a
shared neighbour would be a second shared vertex.  The opposite layer was
excluded when `K` was defined.  Every cycle contains and removes `e`; the
opposite layer does not contain `e`, so `e` is absent from the final union.
Every certificate in the private pivot bucket contains `e` and is destroyed.
QED.

This is a one-state-per-petal menu, not a Cartesian product.

## AC3ij -- failed cycle-star menu returns a realized rank -- PROVED

For state `j`, let `C_j` be the exact created union-collateral weight and let

\[
E_r=\frac1p\sum_{j=1}^p C_{j,r},
\qquad r=1,2,3,
\]

where `C_{j,r}` is its created-cell-rank-`r` part relative to the common parent
state.  Then

\[
\frac1p\sum_j C_j=E_1+E_2+E_3.
\]

If

\[
W_e>E_1+E_2+E_3,
\]

one cycle-star state strictly improves the union potential.

If no state improves, one rank satisfies

\[
\boxed{E_r\ge W_e/3}.
\]

AC3gk realizes that rank in one legal cycle-star state.  For every `K_0>=1`,
AC3gi--AC3gj then return:

- an explicit complete-envelope overload;
- a pivot bank with payment at least
  \[
  \boxed{W_e/(3K_0)};
  \]
- or a next created-cell rank of expected weight at least
  \[
  \boxed{W_e/(9K_0)}.
  \]

### Proof

Every menu state destroys the same certified payment `W_e`.  Average the exact
identity `created - destroyed` over the finite menu.  Negative average yields
an improving state.  Otherwise the average created weight is at least `W_e`;
split it among the three created-cell ranks and apply AC3gk--AC3gj. QED.

## AC3ik -- exact all-n handoff -- PROVED AS AN INTERFACE

A fixed-cross long-cycle history now has the following exhaustive scoped
continuation.

1. Finite rectangle-return tickets are consumed.
2. One fixed long return cross recurs, giving a two-cross history profile.
3. If a recurrent subfamily is simultaneously represented in one current
   exchange host, AC3ih gives:
   - an executable paid one-hub cycle-star menu through AC3ii--AC3ij; or
   - an exact two-hub separator core.
4. If no such common host exists, the current allowed host, opposite-layer
   exclusion or outside arithmetic/context label changed.  That change is the
   retained AC3hw non-scalar edge; it is not discarded.

The static cycle-star and two-hub alternatives are exactly the matching
interfaces developed on `research/all-n-prime-patching`.  Their source-credit,
controller and asymptotic patch hypotheses are not imported into AC.  AC uses
only the finite matching statement and its own private pivot payment.

## Consequence

The repeated-cell frontier is reduced to:

- a finite stock of spent rectangle tickets;
- a paid one-hub cycle-star menu;
- a two-hub exchange-resource core;
- or an explicit host/context change between historical occurrences.

The next AC4 target is the finite ancestry of two-hub cores and host changes,
together with physical occurrence realization of the attached carry/BDA/RI
roles.

## Finite check

`scripts/verify_ac_long_cycle_interface.py` exhausts permutation pairs through
side six, classifies reverse return crosses, checks the rectangle ticket stock
and long-return pigeonhole, verifies cycle switches on synthetic one-hub
flowers, checks inserted-edge uniqueness and pivot removal, and exhausts the
failed-menu rank and constant identities.
