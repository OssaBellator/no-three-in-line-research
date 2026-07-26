# Polynomial atomic outer alphabets and the set-valued profile guardrail

**Branch:** `research/alternating-core-chain`

AC3ka--AC3kd reduce global alternating closure to a finite outer-profile quotient,
but AC3ka is polynomial only after every outer field and reset decoration receives
an explicit polynomial bound.  AC3lh and AC3ls already bound the hard-check and
saturated-literal portions.  This note audits the remaining physical owner,
protected-contract, base-host and envelope fields.

The central correction is that a polynomial universe of atoms does not make an
arbitrary set-valued field polynomial: a universe of size `U` has `2^U` subsets.
Thus a base host, protected registry or envelope cannot be placed into a claimed
polynomial outer profile merely because all of its cells or checks are
polynomially indexed.  What is polynomial without further hypotheses is the
stock of **atomic witnesses** for owner identities, scoped contracts and set
changes.  Full set-valued fields require deterministic reconstruction,
monotonicity, or an edge-specific recurrence theorem.

## Physical address universe

Let `Omega_lay` be the two-layer physical address universe.  On an `n x n`
board use the safe bound

\[
A=|\Omega_{\rm lay}|\le 2n^2.
\]

A physical object of support rank at most `r` is represented by an object kind,
an ordered support of size at most `r`, and at most `m` additional labels per
support.  Ordered supports are used only for a safe upper bound; unordered
objects use no more addresses.

## AC3lt -- bounded physical owner-token stock -- PROVED UNDER THE DECLARED SUPPORT CONTRACT

Assume:

1. there are at most `K_own` physical owner kinds;
2. every physical owner token has support rank at most `r_own`;
3. after its kind and physical support are fixed, it has at most `m_own`
   admissible arithmetic/transition decorations;
4. capacity-only tokens not carried by such a support lie in a separately
   declared universe of size `Q_cap`.

Then the exact owner-token universe satisfies

\[
\boxed{
N_{\rm own}
\le
K_{\rm own}m_{\rm own}
\sum_{s=1}^{r_{\rm own}}A^s
+Q_{\rm cap}.
}
\]

In particular, when `r_own`, `K_own`, `m_own` and `Q_cap` are polynomially
bounded and `r_own` is constant, the owner-token identity field is polynomial in
`n`.

### Proof

Choose the owner kind, support rank, ordered physical support and one of the
remaining decorations.  There are at most `A^s` ordered supports of rank `s`.
Add the separately addressed capacity tokens. QED.

This theorem applies to current pivot, BDA, RI/OP, phase and protected-resource
owners only after the relevant interface states a bounded physical support and
all arithmetic multiplicities not determined by that support.  A normalized
arithmetic name is not bounded by this theorem unless its physical realization
and residual multiplicity are included in `m_own`.

## Scoped hard and protected atoms

A scoped constraint atom consists of:

- one of `q_sc` constraint kinds;
- an ordered physical scope of rank at most `r_sc`;
- one of at most `m_sc` local relation/declaration labels on that scope.

Global constraints with scope `Omega_lay` are not covered by a constant-rank
claim and must remain separate.

## AC3lu -- bounded scoped-contract atom stock -- PROVED

The exact bounded-scope contract-atom universe satisfies

\[
\boxed{
N_{\rm sc}
\le
q_{\rm sc}m_{\rm sc}
\sum_{s=1}^{r_{\rm sc}}A^s.
}
\]

For constant `r_sc` and polynomial `q_sc,m_sc`, this is polynomial in `n`.
The same bound applies to bounded-rank hard checks, protected-bank clauses,
replacement constraints and AC3v factor/constraint witnesses after their
kinds and local relations are declared.

### Proof

Choose the kind, rank, ordered scope and relation label.  The number of ordered
rank-`s` scopes is at most `A^s`.  Sum over the permitted ranks. QED.

AC3x may further compress conflict causes to a finite incidence-word alphabet,
but that compression is a label bound and does not identify two distinct
physical contract atoms.

## AC3lv -- polynomial atoms do not imply polynomial set profiles -- PROVED

Let `U` be any nonempty finite atom universe.  An arbitrary active registry,
base host, protected-contract set or envelope is a subset of `U`, so the number
of possible exact set states is

\[
\boxed{2^{|U|}.}
\]

This bound is attained.  Consequently, even when `|U|` is polynomial in `n`,
the exact set-valued outer field can have exponentially many values.

### Proof

Every atom may be independently present or absent, giving a bijection between
set states and binary words on `U`. QED.

Therefore none of the following statements is valid without an extra theorem:

- a base host has polynomially many states because it contains only `n^2`
  cells;
- an AC3v envelope has polynomially many states because every envelope cell is
  physical;
- a protected registry has polynomially many states because its clauses have a
  polynomial address dictionary;
- a hard registry has polynomially many states because its exact checks are
  polynomially indexed.

The valid replacements are deterministic reconstruction from a smaller
profile, monotone evolution, or recurrence accounting for exact atom changes.

## Canonical atomic changes of set-valued fields

Fix a total order on a finite atom universe `U`.  For two distinct set states
`F,F' subseteq U`, let

\[
u=\min(F\triangle F').
\]

Record the direction `+` when `u in F'\F` and `-` when `u in F\F'`.

## AC3lw -- least-atom reset decoration -- PROVED

Every strict change of a set-valued field has one canonical decoration

\[
\boxed{(u,+)\quad\text{or}\quad(u,-)}
\]

from an alphabet of size at most `2|U|`.

For weighted set changes of total weight `W`, one exact atom/direction class
carries weight at least

\[
\boxed{W/(2|U|)}.
\]

Equality of this decoration does not imply equality of the source or target set
states.

### Proof

The symmetric difference is nonempty, so its least atom exists and belongs to
exactly one of `F,F'`, determining the direction.  There are two directions per
atom.  Weighted pigeonhole gives the concentration bound.  Other atoms may
differ between two transitions with the same least changed atom, proving the
last warning. QED.

For a base-host or envelope field whose atoms are layer-addresses, `|U|<=2n^2`
and the least-cell add/remove decoration has size at most `4n^2`.  For a
bounded-scope protected or hard registry, use `U` equal to its exact atom
universe from AC3lu.

## AC3lx -- monotone set fields have a linear atom potential -- PROVED

Let

\[
F_0,F_1,\ldots
\]

be a history of subsets of a fixed atom universe `U`.

1. If the history is monotone increasing and every strict step adds at least one
   atom, it has at most `|U|` strict changes.
2. If it is monotone decreasing and every strict step removes at least one atom,
   it has at most `|U|` strict changes.
3. For several monotone set fields with atom universes `U_1,...,U_t`, the total
   number of strict changes is at most
   \[
   \boxed{\sum_i|U_i|.}
   \]

### Proof

In the increasing case, `|F_j|` is a strictly increasing integer between zero
and `|U|`.  In the decreasing case, `|U\F_j|` is strictly increasing in the
same range.  Sum the counters for several fields. QED.

This theorem covers the existing monotone unavailable mask and persistent host
reopening potentials.  It also applies to a protected or envelope registry only
when persistence proves that earlier atoms cannot be restored or removed in the
opposite direction inside the same closure attempt.

## AC3ly -- corrected physical outer-alphabet interface -- PROVED

Under the declarations above, the physical part of the outer-reset system has
the following exact status.

1. **Owner identities.**  Bounded by `N_own` from AC3lt.
2. **Scoped hard/protected atoms.**  Bounded by `N_sc` from AC3lu.
3. **Host/envelope/protected set-change decorations.**  Bounded by twice the
   corresponding atom-universe size through AC3lw.
4. **Monotone set histories.**  Terminate after the AC3lx atom budget and need
   not be multiplied into the outer-profile count.
5. **Nonmonotone set histories.**  Have a polynomial atomic reset decoration,
   but their exact set states may still be exponential by AC3lv.  Repetition of
   one atom/direction is not global progress unless a ticket, payment, bounded
   descent, impossibility theorem or deterministic reconstruction closes it.
6. **Global or unbounded-scope contracts.**  Remain separate outer fields and
   receive no polynomial claim from bounded physical addresses.

Consequently, AC3ka may use polynomial decoration alphabets for the physical
owner/check/host/envelope witnesses proved here.  It may claim a polynomial
outer-profile count only after every retained set-valued field is either:

- reconstructed canonically from already polynomial scalar/address data;
- monotone and removed into an AC3lx potential;
- replaced by a bounded exact ticket state;
- or otherwise proved to have a polynomial quotient.

### Proof

Items 1--4 are AC3lt, AC3lu, AC3lw and AC3lx.  AC3lv gives the obstruction in
item 5, while AC3kd lists the valid recurrence-closing mechanisms.  Item 6 is
the explicit scope limitation in AC3lu and AC3v. QED.

## Consequence

The outer-alphabet frontier is now narrower and safer.

- Exact physical owner identities are polynomial under a constant-support and
  bounded-multiplicity contract.
- Exact bounded-scope hard/protected atoms and their reset witnesses are
  polynomial.
- Base-host and envelope **change labels** are polynomial at the atomic level.
- Arbitrary full registries, hosts and envelopes are not automatically
  polynomial; their set-state entropy is a real residual obstruction.

The remaining global work is to prove deterministic or monotone evolution for
the live base-host, protected-registry and envelope fields, and to bound the
remaining denominator/same-denominator arithmetic multiplicities.  Any field
which can genuinely toggle must enter the repeated macro-edge router with an
exact atom-level ticket or descent theorem.

## Finite check

`scripts/verify_ac_outer_alphabet_audit.py` checks the owner and scoped-contract
counting formulae, exhausts all pairs of set states through eight atoms, verifies
the least-atom direction and weighted concentration bounds, confirms the
`2^U` profile count, and audits increasing/decreasing atom potentials and
combined monotone budgets.
