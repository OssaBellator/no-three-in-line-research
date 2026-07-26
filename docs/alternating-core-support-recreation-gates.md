# Physical-support restoration gates for exact owner recreation

**Branch:** `research/alternating-core-chain`

AC3nx--AC3ob reduce faithfully destroyed common-owner recurrence to exact
recreation gates.  Many installed owner tokens have a stronger property: their
current occurrence is supported by a finite set of physical cells, capacities,
mask atoms or protected-resource atoms.  If payment destroys at least one of
those support atoms, exact recreation cannot occur until a canonical lost atom
is restored.

This note closes that support-destroying class under monotone or capacity-one
restoration contracts.  It does not cover status-only or context-only
recreation in which every physical support atom remains present.

## Support-faithful owner tokens

Fix one outer epoch with a fixed builder context.  Let `A` be a finite totally
ordered universe of exact physical support atoms.  Every exact owner token
`pi` has a nonempty support set `supp(pi) subseteq A`.

The token is **support-faithful** in the epoch when currentness of `pi` implies
that every atom in `supp(pi)` is present.  The support address includes physical
cell identity, layer, scale, resource occurrence, protection epoch and every
field needed to distinguish equal symbolic formulas.

A faithful destruction edge is **support-destroying** when at least one atom of
`supp(pi)` is present in the parent and absent in the child.  Choose the least
such atom and denote it by `z(pi,T)`.

## AC3oc -- exact recreation contains a canonical support-restoration gate -- PROVED

Let `T` faithfully destroy a support-faithful token `pi`, and suppose `T` is
support-destroying with canonical lost atom `z=z(pi,T)`.  Every later path that
recreates the same exact token contains a unique first edge on which `z`
changes from absent to present.

### Proof

Immediately after `T`, atom `z` is absent.  When the exact token is current
again, support-faithfulness implies that `z` is present.  The finite membership
word of `z` therefore begins with zero and ends with one.  Its first one has a
unique preceding zero, giving the canonical restoration edge. QED.

The gate address is the exact pair `(pi,z)` together with the retained
restoration kind and outer-epoch context.

## AC3od -- monotone support destruction forbids recreation -- PROVED

If `z(pi,T)` is deletion-monotone for the rest of the epoch, then `pi` cannot be
recreated in that epoch.

### Proof

Recreation requires restoration of `z` by AC3oc, while deletion monotonicity
forbids such an edge. QED.

This applies to a consumed capacity bit, erased mask atom or removed protected
resource that has no restoration operation inside the epoch.

## Token--atom restoration tickets

For every support pair `(pi,z)` let `c(pi,z)` be a nonnegative integer
restoration capacity.  A restoration edge charged to `(pi,z)` consumes one
unit, and consumed units are not restored inside the epoch.  Different owner
tokens sharing one physical cell have different token--atom addresses unless a
separate theorem supplies shared capacity accounting.

## AC3oe -- support-recreation episodes have a finite ticket bound -- PROVED

In one fixed builder context, suppose every support-destroying recreation of
`pi` is charged to the canonical pair `(pi,z(pi,T))`.  Then the number of such
recreation episodes is at most

`C_supp = sum_pi sum_{z in supp(pi)} c(pi,z)`.

For capacity-one pairs this becomes

`C_supp <= sum_pi |supp(pi)|`.

### Proof

AC3oc assigns each recreation episode one canonical token--atom restoration
edge.  The contract consumes one unit from its exact pair capacity.  No unit is
restored, so the total number of charged episodes is at most the total initial
capacity. QED.

A single physical restoration may make several tokens current.  Those returns
consume separate token--atom capacities; this prevents accidental many-owner
reuse of one physical ticket.

## AC3of -- weighted support-gate localization -- PROVED

Let support-destroying return episodes have total nonnegative weight `W`.  If
there are at most `P_supp` live token--atom pairs and at most `K_supp`
restoration kinds, then one exact support-gate address carries weight at least

`W/(P_supp*K_supp)`.

For returns of one fixed token with support size `s`, one atom/kind gate carries
weight at least `W/(s*K_supp)`.

### Proof

Use the canonical pair from AC3oc, append the restoration kind, and apply
weighted pigeonhole. QED.

## AC3og -- closure of support-destroying owner recurrence -- PROVED UNDER THE SUPPORT-TICKET CONTRACT

Assume every faithfully destroyed exact owner token follows one of these
routes:

1. payment deletes a support atom that is monotone, so AC3od forbids return;
2. payment deletes a support atom whose exact token--atom restoration has finite
   unrestorable capacity, so AC3oe bounds returns;
3. recreation gives an improving/terminal output or advances another bounded
   potential;
4. the owner change is declared context-only and enters the outer
   recreation/reset router without being charged to physical support.

Then support-destroying owner recurrence cannot sustain an infinite
nonterminal history inside one fixed builder context.

### Proof

Recreation-free common-owner segments are bounded by AC3nz.  Every
support-destroying return has AC3oc's canonical gate.  Routes 1--3 forbid or
bound recurrence.  Route 4 makes no support-ticket claim and is handled as an
explicit outer reset.  Hence only finitely many support-destroying returns and
only finitely much work between them are possible. QED.

## Corrected AC4 owner frontier

The following recreation classes are no longer unstructured:

- physical cell/resource deletion with monotone support;
- capacity-one protected or mask support;
- any finite token--atom restoration stock;
- weighted returns after localization to one exact support gate.

The remaining owner-recreation cases are now:

- faithful destruction that leaves every support atom present;
- builder-context changes which reinterpret an unchanged support;
- restoration capacities that can themselves be recreated;
- nonadditive owner resources not represented by exact support atoms or spent
  vectors.

Thus the next AC4 target is specifically **context-only recreation**, not
physical support restoration in general.

## Finite check

`scripts/verify_ac_support_recreation_gates.py` exhausts small support masks and
paths.  It checks canonical first restoration, impossibility under monotone
deletions, exact token--atom ticket accounting and the capacity-one bound.