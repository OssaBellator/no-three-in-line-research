# Faithful common-owner destruction and recreation gates

**Branch:** `research/alternating-core-chain`

AC3w and AC3kj correctly count one common owner once across alternative menu
states.  The remaining AC4 frontier still lists common-owner recurrence because
the same symbolic owner might appear again after a paid transition.  For exact
occurrence-addressed owner tokens, however, faithful payment removes the token
from the child state.  It cannot pay a second time until an explicit recreation
edge restores that exact token occurrence.

This note separates those two events.  Common ownership is an accounting rule,
not a source of infinite payment.  The recurrent object is the exact recreation
gate.  An equivalent owner with different physical support, scale, epoch or
certificate ancestry is a different token unless a theorem proves that the two
addresses represent one conserved resource.

## Exact current-owner sets

Fix a finite totally ordered universe `Pi` of exact owner-token occurrences.  A
closure state `S` has current-owner set

\[
O(S)\subseteq\Pi.
\]

A token address includes every field needed for faithful identity: owner kind,
physical support, scale or quotient occurrence, parent certificate, protection
epoch and any capacity address.  Symbolic equality of an arithmetic formula is
not equality of exact tokens.

For a transition

\[
T:S\longrightarrow S',
\]

an exact token `pi` is a **faithfully destroyed common owner** when:

1. `pi in O(S)`;
2. `pi` is the common owner counted once in every selected alternative of `T`;
3. the selected child state satisfies `pi notin O(S')`;
4. the complete AC3v envelope and AC3ke--AC3kf row certify that disappearance as
   destroyed payment.

## AC3nx -- faithful common payment is one-use before recreation -- PROVED

After a transition faithfully destroys `pi`, no later transition can charge that
same exact token again until some intervening edge changes its current-owner bit
from absent to present.

### Proof

AC3ke requires a paid owner to be current in the parent state.  Immediately after
faithful destruction, `pi` is absent from the current-owner set.  It remains
noncurrent until an edge restores membership.  Therefore every intervening
transition has `current=0` for that exact token and cannot charge it. QED.

A fixed owner left present in the child state is `FIXED_CURRENT`, not covered by
this theorem and not destroyed payment.

## Recreation gates

Suppose a chronological path begins immediately after faithful destruction of
`pi`, so the initial owner bit is zero.  A **recreation edge** is an edge whose
source omits `pi` and whose target contains `pi`.  Choose the first such edge on
the path as the canonical recreation gate.

## AC3ny -- every exact owner-set return contains a canonical recreation gate -- PROVED

Let a path begin at a state `S_0` with `pi notin O(S_0)` and end at a state
`S_m` with `pi in O(S_m)`.  Then the path contains one unique first recreation
edge for `pi`.  Before that edge the token is absent; immediately after it the
token is current.

In particular, every exact macro cycle which faithfully destroys `pi` and returns
to its starting owner set contains a recreation gate for `pi`.

### Proof

The finite membership word of `pi` starts with zero and ends with one.  Let the
first index with value one be `j`.  The preceding value is zero by minimality, so
edge `j-1 -> j` is the unique first recreation edge.  A cycle returning to the
pre-destruction owner set ends with `pi` present and therefore has such an edge.
QED.

This is AC3nn's reverse-atom principle specialized to an exact owner token, but it
uses the payment interpretation to identify departure as faithful destruction and
return as recreation.

## AC3nz -- recreation-free common-owner epochs have a linear potential -- PROVED

Consider an epoch in which no exact owner token is recreated after disappearance.
Let `D_used` be the set of tokens faithfully destroyed by accepted transitions and
put

\[
\boxed{\Xi_{\rm common}=|D_{\rm used}|.}
\]

Every accepted transition carrying positive common-owner payment strictly
increases this potential by at least one, and

\[
\boxed{\Xi_{\rm common}\le|\Pi|.}
\]

Hence at most `|Pi|` accepted transitions in the epoch can be paid solely by
faithfully destroyed common owners.

### Proof

By AC3nx, a faithfully destroyed token cannot be charged again without
recreation.  Recreation is excluded in the epoch, so every positive common-owner
payment contributes at least one token not previously in `D_used`.  The token
universe is finite. QED.

Several common owners destroyed by one transition only increase the potential
faster.  One common owner shared across many menu alternatives is inserted once
into `D_used`, exactly matching AC3w and AC3kj.

## Recreation addresses

Let every recreation edge have one canonical kind from a finite dictionary of
size `K_rec`.  The kind may record:

- physical certificate re-creation;
- capacity or protected-resource reset;
- phase or literal reactivation;
- arithmetic occurrence reconstruction;
- owner-status reinterpretation;
- outer-epoch restoration.

Give the gate address

\[
\boxed{(\pi,\kappa_{\rm rec}).}
\]

## AC3oa -- finite exact recreation-gate stock -- PROVED

If at most `N_owner=|Pi|` exact tokens are live and the recreation-kind dictionary
has size `K_rec`, then

\[
\boxed{
R_{\rm rec}\le N_{\rm owner}K_{\rm rec}.
}
\]

For return episodes with total weight `W`, one exact token/kind recreation address
carries weight at least

\[
\boxed{W/R_{\rm rec}.}
\]

For episodes following destruction of one fixed token `pi`, one recreation kind
carries weight at least `W/K_rec`.

### Proof

Choose the exact token and recreation kind, then apply ordinary or weighted
pigeonhole. QED.

Equality of a recreation address is not payment.  It identifies the exact gate
whose physical cause must be discharged.

## AC3ob -- conditional closure of common-owner recurrence -- PROVED UNDER THE RECREATION-GATE CONTRACT

Assume every recurrent recreation gate for a faithfully destroyed common owner
satisfies at least one of:

1. it returns an improving state, paid executable menu, accepted arithmetic
   chamber or terminal literal/resource profile;
2. it strictly advances a separately bounded integer potential;
3. it consumes a previously unused capacity-one recreation ticket;
4. it is physically impossible under its retained occurrence and coherence
   decorations.

Then faithfully destroyed common owners cannot support an infinite nonterminal
history.  Between recreation gates, AC3nz bounds common-owner-paid transitions by
`|Pi|`; recurrent recreation gates terminate under the four alternatives and
AC3lc.

### Proof

AC3nx prevents reuse before recreation.  AC3nz bounds every recreation-free
segment.  AC3ny assigns every return of a destroyed token one exact recreation
gate.  Alternatives 1 and 4 terminate that recurrence, alternative 2 advances a
bounded counter, and alternative 3 consumes a finite unrestorable ticket.  Thus
no recreation address recurs indefinitely.  AC3kb bounds first edges and internal
epoch work, so the combined history is finite. QED.

## Corrected common-owner frontier

Under exact occurrence identity and faithful destruction:

1. a common owner is counted once in the selected state;
2. the same token pays at most once before recreation;
3. recreation-free segments have the linear potential AC3nz;
4. every owner-set cycle exposes AC3ny's canonical recreation gate;
5. recurrence is localized to the finite address `(token, recreation kind)`.

The remaining live cases are:

- purported payment which leaves the exact token current;
- symbolic owner names without occurrence-faithful identity;
- recreation gates lacking payment, descent, impossibility or tickets;
- unbounded token or recreation-kind dictionaries;
- restoration of a purported recreation ticket across outer epochs;
- nonadditive capacities whose consumption is not represented by token
  disappearance or the AC3ni--AC3nm spent vector.

Thus common ownership itself is removed as an unstructured AC4 recurrence field.
The residual theorem must classify or pay the exact owner-recreation gate.

## Finite check

`scripts/verify_ac_common_owner_recreation.py` exhausts owner-set paths on up to
four tokens, verifies one-use-before-recreation, canonical first recreation gates,
recreation-free epoch bounds and the combined destruction/recreation ticket
counter.
