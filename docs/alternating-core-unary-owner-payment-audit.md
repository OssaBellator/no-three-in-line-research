# Unary arithmetic owners: physical occurrence and payment audit

**Branch:** `research/alternating-core-chain`

AC3jd--AC3jm turn every missing blocker-host cell into an actual target cell,
one current-aligned hard-check scope and one declared owner token.  An
arithmetic name on that check does not by itself make it paid.

This note records the exact distinction.  The target blocker cell is absent
from the current blocker state.  Hence any forbidden BDA/RI/carry template
whose realization uses that target is prospective geometry.  It can obstruct a
repair and can generate a literal/residual profile, but it is not a current
certificate destroyed by the repair.  Payment requires a separate current
owner token and a faithful destruction assignment.

## AC3jv -- an activated unary check is not current payment -- PROVED

Let `z` be a currently absent blocker cell and let

\[
C=(S_C,f_C)
\]

be a canonical hard check activated by inserting `z`.  Then

\[
f_C(z)=1,
\qquad
\omega(z)=0,
\]

so

\[
\boxed{f_C\ne\omega|_{S_C}.}
\]

Consequently any certificate, arithmetic template or protected pattern whose
presence is exactly the forbidden assignment `f_C` is absent from the current
blocker configuration.  Its weight cannot be counted as current destroyed
payment for reopening `z`.

The check may still be:

- a hard feasibility exclusion;
- a prospective created-collateral template;
- a protected pattern owned by a separate current charging token;
- or a terminal arithmetic label for a separately paid object.

### Proof

Activation changes `z` from zero to one and leaves every residual literal at
its current value.  Thus the forbidden target assignment differs from the
current assignment at `z`.  A current paid certificate must be present in the
current union, so the target-containing forbidden pattern is not such a
certificate. QED.

This is the hard-constraint analogue of the earlier union-potential rule:
explicit created geometry is collateral of an already paid transition, not new
payment merely because its formula is known.

## Separate current owner tokens

Give every canonical unary check an optional owner token `pi`.  The owner is
**currently chargeable** only when all of the following are proved.

1. `pi` is an actual current certificate or current charging resource.
2. Its paid weight is assigned privately, except for an explicitly declared
   common token counted once by AC3w.
3. Every local state claimed to reopen the target edge destroys or consumes
   `pi` in the full two-layer union/resource ledger.
4. Every collateral and feasibility scope touched by the owner discharge is in
   the AC3v envelope.
5. The reverse ticket, capacity and scale-cleanliness contracts are stated.

## AC3jw -- exact charging criterion for unary owners -- PROVED

A unary missing-host reason contributes certified destroyed payment if and only
if it carries a separate current owner token satisfying the five charging
conditions above.

When several target reasons share one current owner token, AC3w counts that
owner once, not once per target.  When owner tokens are private and disjoint on
an AC3v-independent family, their paid weights add exactly.

A target-containing hard check without such an owner remains in AC3jg--AC3jl's
literal/residual router and receives zero destroyed-payment credit.

### Proof

The forward implication is the definition of certified payment used throughout
AC1--AC3: current presence, actual destruction/consumption, private assignment
and scope completeness are mandatory.  The reverse implication is AC3w's exact
paid-set accounting together with AC3v legality and collateral additivity.
AC3jv excludes payment from the target pattern itself. QED.

## Bounded-denominator-shaped checks

Suppose a unary hard check has a radial coordinate template

\[
T_h(P)
=
\{P,\ P+hu\,d,\ P+hv\,d\}
\]

with primitive direction `d`, distinct nonzero slots `u,v`, and the target cell
`z` equal to one member of the displayed triple.

## AC3jx -- BDA target templates are prospective unless separately owned -- PROVED

If the radial hard check is activated by inserting `z`, then the displayed
three-cell template is not an occurrence-faithful current radial triple.
Therefore it does not enter the clean current BDA rectangle decoder as payment.

Exactly one of the following routes is valid.

1. A separate occurrence-faithful current radial triple or adjacent current
   radial pair is proved and assigned as the owner token.  Then the established
   union-safe BDA interface applies to that current object.
2. The target template is a missing-support/prospective hard blocker.  It enters
   AC3jg--AC3jl and may be completed or neutralized only through a scope-complete
   repair, with payment coming from the parent pivot bank or another current
   owner.
3. The coordinate template is reflected `CD` geometry.  AC3hs--AC3ht apply:
   the raw reflected pair is nonradial and routes through realized collateral
   ranks rather than the radial decoder.

### Proof

The first statement is AC3jv.  A clean BDA paid object is, by definition, an
actual current radial occurrence; an activated target template fails that
condition.  The three routes are the exhaustive ordinary-current,
prospective/missing-support and reflected cases already distinguished by the
BDA support correction. QED.

## Rational-inverse-shaped checks

Suppose the target cell is declared to be a physical source cell with nonzero
column `x`, normalized source coset `U_alpha H`, and physical source coset
`xH`.  Multiplication in the quotient gives one forced scale coset

\[
\boxed{
S=(U_\alpha H)^{-1}xH.
}
\]

At that scale, the normalized root and image labels determine the physical
anchor and partner cosets as in AC3au.

## AC3jy -- RI target cells determine scale but not payment -- PROVED

A physically declared RI source target has a unique derived scale coset.
Therefore a unary RI reason is never left with an unspecified scale: it returns
one of

1. a coherent physical scale and its exact root/image/owner decorations;
2. an explicit scale mismatch with another witness in the same declared owner;
3. an invalid RI declaration because the target does not lie in the claimed
   physical source coset.

However, scale realization does not imply current payment or component
payability.  Since the target is absent from the current blocker state, the
RI-shaped target check is prospective.  The generic movable RI bank requires a
separate current paid owner satisfying AC3ax's scale-faithful and
component-payable hypotheses.  Canonical current OP root factors continue to
use AC3bf--AC3bj because they are fixed by completion.

### Proof

Coset multiplication is cancellative, giving the unique displayed scale.
Comparing the derived scales of all owner witnesses gives coherence or an exact
mismatch.  AC3jv proves the payment statement, while AC3ax and AC3bf state the
two valid RI payment routes. QED.

## Owner-status chart

For every arithmetic unary reason retain four exact Boolean flags:

\[
(\texttt{current},
 \texttt{physical},
 \texttt{coherent},
 \texttt{payable}).
\]

Here:

- `current` means a separate owner token is present now;
- `physical` means all coordinates/cosets in the owner declaration are realized
  by actual cells;
- `coherent` means all scale/anchor/context witnesses agree;
- `payable` means the declared transition actually destroys/consumes the owner
  under a faithful assignment.

## AC3jz -- exact owner-route dictionary -- PROVED

The status chart has the following safe routes.

1. `payable=1` implies all other required flags and enters the declared paid
   carry/BDA/RI/protected-resource bank.
2. `current=1`, `physical=1`, `coherent=1`, `payable=0` is a fixed current owner
   which is not moved by the proposed repair; it cannot be charged to that
   repair and must use a different bank or the closed/fixed-term interface.
3. `physical=1`, `current=0` is prospective target geometry and enters the
   hard-literal/collateral router.
4. `physical=0` returns a physical occurrence failure.
5. `physical=1`, `coherent=0` returns an exact scale/anchor/context mismatch.
6. Any change of these flags between recurrent occurrences is an owner-
   interpretation outer reset in AC3jt.

No normalized arithmetic owner is terminal merely from its name.  The owner
chart must select one of the six exact routes.

### Proof

The implications are the definitions of current presence, physical
realization, coherence and faithful payment, together with AC3jv--AC3jy.  The
cases are exhaustive after testing physicality, coherence, current presence
and payability in that order. QED.

## Consequence

The missing-host physical-occurrence frontier is now separated cleanly.

- Target-containing BDA/RI/carry formulas are actual prospective hard geometry,
  not current payment.
- A separate current owner may be paid only through its proved destruction
  contract.
- RI target cells determine their physical scale exactly, but component
  payability remains an independent test.
- BDA target templates require a separate occurrence-faithful current radial
  owner or remain in the missing-support/literal router.

The remaining physical work is to fill the owner-status chart for each live
carry/BDA/RI/protected-resource role and to install the nonpayable literal and
residual outputs.  No role can bypass that audit by retaining only a normalized
arithmetic label.

## Finite check

`scripts/verify_ac_unary_owner_payment_audit.py` exhausts binary activated
checks through rank four, BDA target/current incidence patterns, quotient-scale
recovery in finite cyclic quotient groups, owner-status truth tables and every
route implication above.