# Transition-relative owner-status registry

**Branch:** `research/alternating-core-chain`

AC3jv--AC3jz require every unary arithmetic owner to carry the exact status
chart

\[
(\texttt{current},\texttt{physical},\texttt{coherent},\texttt{payable}).
\]

This note applies that chart to the installed alternating-core banks.  The main
point is that status is attached to an owner **and a proposed transition**.  It
is not a permanent property of an arithmetic name or even of a current token.
A current token may be payable in one bank and fixed or irrelevant in another.

No new payment is asserted here.  Every payable row below points to an existing
destruction or consumption theorem.  Every prospective or nonpayable row is
kept outside the destroyed-payment ledger.

## Transition-relative owner records

An owner record is a tuple

\[
(\pi,\mathcal T,\kappa,
 \texttt{current},\texttt{physical},\texttt{coherent},\texttt{payable}),
\]

where:

- `pi` is the exact owner token;
- `mathcal T` is the proposed local transition or finite menu;
- `kappa` is the owner kind and theorem interface;
- `current` means `pi` is present as a current certificate/resource;
- `physical` means every declared cell, coset, scale, anchor and context witness
  exists physically;
- `coherent` means those witnesses agree on one transition instance;
- `payable` means every claimed state in `mathcal T` destroys or consumes `pi`
  under the private/shared accounting contract.

## AC3ke -- owner status is transition-relative -- PROVED

The four status flags are functions of `(pi,mathcal T)`, not of `pi` alone.
In particular:

1. a token may be current, physical and coherent but nonpayable for one
   transition which leaves it fixed;
2. the same token may be payable for another transition which destroys its
   certificate or consumes its capacity;
3. prospective geometry containing an absent target cell has `current=0` for
   that target template even when a separate current owner token exists;
4. changing `mathcal T`, its physical scale, its owner assignment, or its
   destruction contract may change the owner-status route and is therefore an
   AC3jt outer reset.

### Proof

Current presence is a property of `pi` in the parent state, while payability is
the statement that the proposed transition destroys or consumes it.  Two
transitions can act differently on the same current token.  AC3jv separates an
absent target template from any current owner; AC3jw makes actual destruction
or consumption mandatory.  The remaining statements are definitions of the
physical, coherence and outer-reset fields. QED.

## Canonical installed owner rows

The following registry uses six route labels from AC3jz:

- `PAID`;
- `FIXED_CURRENT`;
- `PROSPECTIVE`;
- `OCCURRENCE_FAILURE`;
- `COHERENCE_MISMATCH`;
- `OWNER_RESET`.

### Row P -- private union-safe pivot bucket

The owner token is one current certificate in a private bucket through a
realized pivot.  For the AC3fs--AC3fv rectangle decoder:

\[
\boxed{(1,1,1,1)}.
\]

Every selected local state removes the pivot from the full two-layer union and
destroys every represented private certificate.  AC3v and AC3w make joint
payment exact on an independent family.

### Row B -- occurrence-faithful current BDA owner

The owner is an actual current radial certificate or clean adjacent radial pair
with the physical support required by AC3fz--AC3gf.  For its union-safe BDA
decoder:

\[
\boxed{(1,1,1,1)}.
\]

The same normalized BDA formula containing an absent blocker target instead
belongs to row `B_pros`:

\[
\boxed{(0,1,1,0)}.
\]

It is prospective hard or collateral geometry and receives no destroyed
payment from its formula.

### Row R -- generic movable RI owner

A generic RI owner enters `PAID` only under AC3ax's scale-faithful,
component-payable and private-assignment hypotheses.  Then

\[
\boxed{(1,1,1,1)}.
\]

A physically declared target source cell determines its scale by AC3jy but is
prospective when the target cell is absent:

\[
\boxed{(0,1,1,0)}.
\]

Scale mismatch gives `COHERENCE_MISMATCH`; failure of the physical coset
identity gives `OCCURRENCE_FAILURE`.

### Row F -- canonical OP fixed-root owner

The current OP factor and its root cells are physical and coherent.  Relative
to a nontrivial RI completion component, the roots are fixed by AC3bf, so that
component assignment has

\[
\boxed{(1,1,1,0)}.
\]

This is `FIXED_CURRENT`, not failed physical realization.  Relative to the
closed-completion I6 bank AC3bg--AC3bj, the owner token is the complete current
factor/certificate payment specified by that bank; when its exact destruction
contract is used, the bank record has

\[
\boxed{(1,1,1,1)}.
\]

Thus the fixed root cell and the payable current certificate are not the same
owner token.

### Row S -- canonical phase token

A current canonical phase-block certificate enters `PAID` for a legal common
phase mismatch which destroys it under AC3s--AC3u and counts the shared token
once under AC3w:

\[
\boxed{(1,1,1,1)}.
\]

A phase-rigid token, an inactive literal, or a target check with no current
owner is `FIXED_CURRENT` or `PROSPECTIVE` according to whether a separate
current token exists.

### Row C -- capacity or protected-resource owner

A current capacity, mask, reverse-ticket or protected-bank token is `PAID`
exactly when the proposed transition consumes it under its stated capacity-one
or protected-resource contract.  Otherwise a current untouched token is
`FIXED_CURRENT`.  No protected pattern containing only the absent target is
paid without a separate current owner.

### Row U -- unowned hard literal

An unowned activated hard check has no current payment token.  Its target
geometry is

\[
\boxed{(0,1,1,0)}
\]

when physically realized, and it enters AC3jg--AC3jl's literal/residual router.

## AC3kf -- installed owner registry is payment-safe -- PROVED

Every currently installed alternating-core payment interface listed above
enters exactly one of the following safe classes.

1. `PAID`, backed by an existing exact destruction/consumption theorem and
   AC3v--AC3w accounting.
2. `FIXED_CURRENT`, physically current but not chargeable to the proposed move.
3. `PROSPECTIVE`, physically meaningful target geometry with no current target
   token.
4. `OCCURRENCE_FAILURE`.
5. `COHERENCE_MISMATCH`.
6. `OWNER_RESET`, when the transition-relative interpretation changes.

No row promotes a normalized BDA/RI/carry name, absent target pattern, fixed
root cell, or protected formula to payment without a separate current owner
and faithful destruction contract.

### Proof

Rows P and B use the union-safe pivot/BDA destruction theorems.  Row R is
AC3ax and AC3jy.  Row F is the distinction between AC3bf fixed completion roots
and AC3bg--AC3bj closed-bank factor payment.  Row S uses AC3s--AC3u and AC3w.
Rows C and U are the charging definition and AC3jv--AC3jw.  AC3jz proves the six
routes are exhaustive. QED.

## Finite owner-route reset alphabet

Let there be at most `K` owner kinds and at most `J` installed transition
families.  Use the six AC3jz route labels as the status alphabet.  A strict
owner-route reset changes one route label to another.

## AC3kg -- owner-route reset stock -- PROVED

The number of directed owner-route reset labels is at most

\[
\boxed{30KJ}.
\]

If the exact owner token is included and at most `N_owner` tokens are live, the
safe stock is

\[
\boxed{30KJ N_{\rm owner}}.
\]

A weighted family of owner-route resets of total weight `W` therefore contains
one exact kind/transition/status edge carrying at least

\[
\boxed{W/(30KJ)}
\]

when token identity is suppressed, or `W/(30KJ N_owner)` with exact identity.

### Proof

There are six source routes and five different target routes, giving thirty
directed route changes.  Multiply by the owner-kind and transition-family
choices, and by token identity when retained.  Weighted pigeonhole gives the
last statement. QED.

## AC3kh -- owner resets enter the outer macro quotient -- PROVED

Decorate every AC3jt owner-interpretation reset by:

- owner kind;
- installed transition family;
- source and target AC3jz route labels;
- exact token identity only when the recurrence theorem requires it.

Then the owner-reset component of the AC3ka decoration alphabet has size at
most `30KJ`, or `30KJ N_owner` with exact identity.  First traversal is charged
by AC3kb.  Repetition is one exact macro-edge recurrence under AC3kc.  It
terminates under AC3kd only when the corresponding owner theorem supplies a
capacity-one ticket, current payment, strict bounded descent or terminal
literal/resource output.

In particular, repeatedly reinterpreting prospective geometry as a different
owner cannot be hidden as arithmetic progress.  The source and target status
routes are part of the repeated macro edge.

### Proof

AC3kg supplies the finite decoration stock.  AC3ka--AC3kd apply after adding
that decoration to the source and target outer profiles.  The final limitation
is exactly the macro-ticket contract of AC3kd. QED.

## Consequence

The live owner frontier is no longer an undefined physical-occurrence gate.
For each carry/BDA/RI/protected owner one must fill one registry row for the
actual proposed transition.  A `PAID` row uses its existing bank.  Every other
row returns a fixed token, prospective literal, exact mismatch, occurrence
failure, or decorated outer reset.

## Finite check

`scripts/verify_ac_owner_status_registry.py` exhausts the valid owner-status
truth table, checks the transition-relative fixed/payable examples, enumerates
the six-route directed reset stock and verifies the weighted concentration and
AC3ka decoration bounds.
