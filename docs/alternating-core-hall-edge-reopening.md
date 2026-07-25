# Monotone Hall-edge reopening and context-reset localization

**Branch:** `research/alternating-core-chain`

AC3ji--AC3jm turn every failed blocker completion into one centred family of
missing hard targets.  This note records the exact progress made when one of
those hard reasons can be discharged and its missing blocker edge reopened.

The result is deliberately conditional on **persistence**.  Inside one fixed
owner/context epoch, a successful discharge must keep every previously
reopened blocker-host edge available.  If a later transition closes such an
edge again, that is a named context, mask, owner or envelope reset and leaves
the monotone epoch.  It is not counted as progress inside the theorem below.

## Bipartite exchange notation

Let `G=(L,R;E)` be the blocker exchange graph for one projected active
matching.  Both sides have size `n`.  Assume `G` has no perfect matching and let
`X subseteq L` be its canonical inclusion-minimal Hall-deficient source set.
Put

\[
Y=N_G(X),
\qquad
m=|X|.
\]

AC3ix gives

\[
|Y|=m-1
\]

also in the singleton dead-row case.  Let

\[
Z=R\setminus Y.
\]

Every pair `(a,b) in X times Z` is a missing exchange edge.  AC3iz separates
those explained by the projected active matching and protected pivot from the
genuine blocker-base-host defects.

## AC3jn -- every cut-edge reopening destroys its current minimal core -- PROVED

For every missing exchange edge

\[
e=(a,b)\in X\times Z,
\]

let

\[
G^+=G+e.
\]

Then

\[
\boxed{|N_{G^+}(X)|=m.}
\]

Consequently `X` is not Hall-deficient in `G^+`.  If `G^+` still has no perfect
matching, its canonical inclusion-minimal Hall core is different from `X`.

Moreover, `G[X,Y union {b}]` has a matching saturating `X`.

### Proof

The new destination `b` lies outside `Y=N_G(X)`, so adding `(a,b)` enlarges the
neighbourhood of `X` by exactly one:

\[
N_{G^+}(X)=Y\cup\{b\}.
\]

Its size is `m`.  Hence `X` is no longer deficient and cannot be the next
canonical deficient core.

For the final assertion, minimality of `X` implies Hall's condition on every
proper subset of `X`.  The full set has exactly `m` neighbours after the edge
addition.  Hall's theorem on the induced bipartite graph with left side `X`
and right side `Y union {b}` therefore gives a matching saturating `X`. QED.

The last assertion is local to the repaired core.  Other source sets may remain
deficient, so one reopened edge is not claimed to produce a global cycle
cover.

## Persistent host-expansion epochs

Fix one projected active matching, pivot, arithmetic/context label, envelope,
owner interpretation and all hard constraints except a finite family of unary
reasons which may be discharged.  Let

\[
B_0\subseteq B_1\subseteq\cdots\subseteq B_t
\]

be the blocker base hosts after successful discharges.  A strict reopening step
adds at least one previously missing physical blocker cell.  Recompute the
exchange graph and its canonical Hall core after every step.

## AC3jo -- monotone blocker-host expansion has length at most `n^2` -- PROVED

There are at most

\[
\boxed{n^2-|B_0|}
\]

strict reopening steps in one persistent host-expansion epoch.

At every nonterminal step, choose any executable genuine defect cell from the
current canonical Hall cut.  AC3jn guarantees that the current core disappears,
and the physical host size strictly increases.  Therefore the process reaches
one of:

1. a blocker exchange graph with a cycle cover;
2. a canonical Hall core none of whose genuine defect reasons is executable in
   the fixed owner/context epoch;
3. an outer context, mask, owner or envelope reset before persistence can be
   maintained.

### Proof

Every strict step adds a new cell and no cell is removed.  The board contains
`n^2` cells.  AC3jn proves core progress at each selected cut, while the finite
host-size bound proves termination.  A failed persistence hypothesis is by
definition conclusion 3. QED.

## Executable unary reasons

A genuine defect cell `z` has its AC3jd canonical hard check and AC3jh owner
class.  Call the reason **edge-executable in the current epoch** when there is a
proved local state which:

1. discharges that hard reason and makes `z` available to the blocker host;
2. keeps the projected active matching and protected paid pivot fixed;
3. preserves every previously reopened blocker-host cell;
4. includes all touched hard scopes, soft factors and private paid sets in its
   AC3v envelope; and
5. satisfies the declared reverse ticket and owner-payment contract.

This definition does not infer executability from a reason name.  Carry, BDA,
RI, phase, protected-bank and exceptional owners must supply their stated
local theorem.

## AC3jp -- executable reason or terminal centred fan -- PROVED

For the current canonical Hall core, exactly one of the following applies.

1. Some genuine defect reason is edge-executable.  Execute its local state,
   consume its exact edge/owner ticket and continue in the enlarged host.
2. No genuine defect reason is edge-executable.  Then all of the AC3ji--AC3jm
   centred target records are terminal within the current epoch:
   - one role-pure target fan;
   - unconditional hard targets;
   - a common residual literal fan;
   - support-disjoint residual blockers;
   - a same-owner fan; or
   - a many-owner resource star.
3. The attempted discharge changes the context, mask, base-host construction,
   owner interpretation or envelope.  Retain that exact changed field as the
   outer transition.

### Proof

The first alternative is the existence definition above followed by AC3jn.
If it fails while the epoch data remain fixed, every genuine cut cell is
nonexecutable and AC3ji--AC3jm classify their complete centred family.  If the
epoch data do not remain fixed, the changed field is exactly alternative 3.
QED.

## AC3jq -- finite reopening potential and the remaining AC4 edge -- PROVED

Let `E_open` be the set of exact physical blocker-host cells reopened in the
current persistent epoch and define

\[
\Xi_{\rm open}=|E_{\rm open}|.
\]

Then

\[
0\le\Xi_{\rm open}\le n^2,
\]

and every executable Hall-edge reopening strictly increases `Xi_open`.
Combining this with AC3it and AC3jc gives the following temporal router.

A long fixed-context state history either:

- executes a repaired common-host pivot menu;
- exposes a missing-host target fan which is terminal in that epoch;
- performs at most `n^2` persistent edge reopenings before blocker repair or
  terminality;
- or changes one exact outer field required by the reopening contract.

Thus successful missing-edge discharge cannot itself cycle.  The remaining
frontier is payment/installation of the explicit terminal fans and termination
of the exact outer context, owner and envelope resets.

## Finite check

`scripts/verify_ac_hall_edge_reopening.py` exhausts bipartite exchange graphs
through four sources, every canonical minimal Hall core and every cut-edge
addition.  It verifies destruction of the selected core, Hall saturation of
the repaired core, strict host-size growth and all reopening-potential bounds.