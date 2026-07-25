# Arbitrary common-host alternating-cycle menus

**Branch:** `research/alternating-core-chain`

AC3ic imports the prime-patching one-hub star / two-hub separator refinement for
long alternating cycles in one current exchange host.  For the alternating-core
payment comparison, however, that refinement is not needed before execution.
Only one cycle state is selected at a time.  Therefore overlapping petals,
fixed spines and two-hub theta families are all legal states of one finite menu
as soon as they share one current reference matching and one current allowed
host.

This note closes the static two-hub output.  The remaining historical issue is
only whether recurrent cycles from different times can be represented in one
common current host/reference state.

## Common-host cycle family

Fix:

- one current permutation matching `M` in layer `ell`;
- one current allowed-edge host `K` containing `M` and excluding every occupied
  cell of the opposite layer;
- one current matching edge `e in M`;
- one nonempty finite family `C` of distinct directed alternating cycles of the
  exchange digraph of `(K,M)`, every cycle containing `e`;
- one private current pivot bucket through `e`, of certified weight `W_e`.

For `Gamma in C`, let `M_Gamma` be the matching obtained by switching exactly
that cycle, and let `S_Gamma` be the resulting ordered two-layer union.

No disjointness between different cycles is assumed.

## AC3ig -- arbitrary common-host cycle menu -- PROVED

The states

\[
\{S_\Gamma:\Gamma\in\mathcal C\}
\]

form one legal equal-margin finite menu.  Every state:

1. preserves all row and column resources;
2. remains disjoint from the unchanged opposite layer;
3. removes the cell `e` from the full two-layer union;
4. destroys the complete private pivot bucket of weight `W_e`.

### Proof

A directed alternating-cycle switch replaces one perfect-matching cycle by the
opposite diagonal cycle and therefore preserves every row and column resource.
Every inserted edge lies in `K`, whose definition excludes the opposite layer.
Because `e` is a reference edge on every selected cycle, it is removed from the
changed layer.  It was absent from the opposite layer by disjointness, so it is
absent from the final union.  Every certificate in the private pivot bucket
contains `e` and is destroyed.

Different cycles may overlap because they are alternative values of one finite
state variable; they are never switched simultaneously. QED.

Thus the one-hub star, fixed-spine theta family, distinct-signature theta family
and two-hub separator family all share the same basic AC execution interface.

## Exact support multiplicities

Choose `Gamma` uniformly from `C`.  For a compatible set `F` of `r<=3`
possible inserted matching cells, put

\[
m_r(F)=|\{\Gamma\in\mathcal C:F\subseteq
M_\Gamma\setminus M\}|.
\]

## AC3ih -- exact cycle-menu cylinder law -- PROVED

For every compatible `F` of rank `r<=3`,

\[
\boxed{
\Pr(F\subseteq M_\Gamma\setminus M)
=
\frac{m_r(F)}{|\mathcal C|}.
}
\]

In particular, if

\[
\Delta_r=\max_{|F|=r}m_r(F),
\]

then every rank-`r` cylinder has probability at most

\[
\boxed{\Delta_r/|\mathcal C|}.
\]

### Proof

The event occurs exactly for the cycle states counted by `m_r(F)`. QED.

No product-power estimate is asserted.  A heavy `Delta_r` is retained as one
literal inserted cell, pair or triple shared by many alternative cycle states.

## AC3ii -- failed arbitrary-cycle menu returns a realized rank -- PROVED

Let `C_{Gamma,r}` be the exact created union-collateral weight of rank `r`
in state `S_Gamma`, relative to the common parent state.  Put

\[
E_r=
\frac1{|\mathcal C|}
\sum_{\Gamma\in\mathcal C}C_{\Gamma,r}.
\]

Then

\[
\mathbb E[\text{created collateral}]
=
E_1+E_2+E_3,
\qquad
\mathbb E[\text{destroyed certified payment}]
=
W_e.
\]

If

\[
W_e>E_1+E_2+E_3,
\]

one cycle state strictly improves the union potential.

If no state improves, one rank satisfies

\[
\boxed{E_r\ge W_e/3}.
\]

AC3gk realizes that rank in one legal cycle state.  For every `K_0>=1`,
AC3gi--AC3gj return:

- an explicit complete-envelope overload;
- a pivot bank with payment at least
  \[
  \boxed{W_e/(3K_0)};
  \]
- or a next-rank return at least
  \[
  \boxed{W_e/(9K_0)}.
  \]

### Proof

AC3ig gives the same certified destroyed payment in every menu state.  Average
the exact created-minus-destroyed identity.  If the average is negative, one
state improves.  Otherwise the three nonnegative rank expectations sum to at
least `W_e`; pigeonhole and apply AC3gk--AC3gj. QED.

## AC3ij -- static two-hub cores are not terminal -- PROVED

Under the common-host hypothesis, every output of AC3ic is executable through
AC3ig--AC3ii.

- A one-hub petal family is the special disjoint-support case.
- A two-hub separator family is still a finite family of alternative legal
  cycles through `e`.
- A fixed-spine or distinct-signature theta decomposition may be retained to
  sharpen the cylinder multiplicities `Delta_r`, but is not required for
  payment or local existence.

Therefore the static two-hub resource core is not an AC4 terminal profile.  Its
only possible failed output is an explicit created-cell rank, complete-envelope
overload or literal heavy inserted support.

### Proof

All families consist of cycles in the same exchange host relative to the same
matching and all contain `e`.  Apply AC3ig--AC3ii. QED.

## AC3ik -- exact residual historical obstruction -- PROVED

For a recurrent fixed-cross history from AC3ib--AC3if, exactly one of the
following remains.

1. A nonempty recurrent subfamily is represented relative to one common current
   matching and one common current allowed host.  Then AC3ig--AC3ij execute it.
2. No such common-host representation is available.  Between occurrences at
   least one of the following changed:
   - the reference matching state;
   - the opposite-layer exclusion;
   - the allowed-edge/resource mask;
   - the arithmetic/context role;
   - the envelope epoch.

The second output is an explicit **host-drift profile**.  It is a
same-denominator non-scalar edge of AC3hw, not a residual long-cycle geometry
problem.

### Proof

This is the definition of common-host representability, followed by AC3ig in
the represented case. QED.

## Consequence

Long alternating cycles are now locally executable whenever they are genuinely
simultaneous alternatives.  Neither one-hub overlap nor two-hub overlap remains
a local obstruction.

The AC4 frontier is reduced further to finite ancestry/payment for host-drift
profiles and physical occurrence realization of their attached carry/BDA/RI
roles.

## Finite check

`scripts/verify_ac_common_host_cycle_menu.py` exhausts directed cycle switches
through side seven, including heavily overlapping and two-hub families.  It
checks matching legality, pivot removal, exact cylinder multiplicities, the
created-rank pigeonhole and all composition constants.
