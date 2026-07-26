# Finite Boolean boundary gates for nonconjunctive context recreation

**Branch:** `research/alternating-core-chain`

AC3oh--AC3ol reduce conjunctive context-only recreation to restoration of one
failed literal.  A fixed nonconjunctive currentness rule need not have such a
literal: parity and threshold rules may become true again without restoring any
canonically selected child defect.  They still have a canonical boundary edge.

This note proves the exact finite-state replacement.  For every fixed Boolean
builder predicate, the first false-to-true edge on a recreation path is unique.
Its complete source/target context address is finite, and monotonicity, descent
or unrestorable boundary tickets close recurrence inside the fixed-builder
epoch.

## Finite Boolean context-faithful tokens

Fix one outer epoch and a finite ordered context-bit set `B` of size `J`.  Write

`X={0,1}^B`.

An exact owner token `pi` has unchanged physical support and one fixed Boolean
predicate

`f_pi:X->{0,1}`.

While the support is present, the token is current exactly when `f_pi(x)=1`.
The predicate address retains the exact builder, registry, phase, protection and
owner occurrence fields.  Replacing the predicate or its bit interpretation is
an outer builder reset, not an internal Boolean transition.

A context-only destruction edge ends at a state `x_0` with `f_pi(x_0)=0`.  A
later exact recreation ends at a state `x_m` with `f_pi(x_m)=1`.

## AC3om -- every finite Boolean recreation has a canonical boundary gate -- PROVED

Along every path

`x_0,x_1,...,x_m`

from a noncurrent context to a context in which the same exact token is current,
there is one unique first index `j` such that

`f_pi(x_(j-1))=0` and `f_pi(x_j)=1`.

The directed pair `(x_(j-1),x_j)` is the canonical Boolean recreation gate.

### Proof

The finite truth word begins with zero and ends with one.  Let `j` be the least
index with value one.  Minimality gives value zero immediately before it, and
the least index is unique. QED.

Unlike AC3oi, the two contexts may differ in several bits.  No claim is made
that one child literal must be restored.

## Boolean boundary stock

Let

`Z_pi={x:f_pi(x)=0}` and `O_pi={x:f_pi(x)=1}`.

The directed Boolean boundary stock for arbitrary context transitions is
contained in `Z_pi x O_pi`.

## AC3on -- explicit finite boundary-address bounds -- PROVED

For one token on `J>=1` context bits, the number of possible directed
false-to-true boundary pairs is

`E_pi=|Z_pi|*|O_pi| <= 2^(2J-2)`.

If every context edge changes at most `s` bits, the safe bound is

`E_pi <= 2^J * sum_(k=1)^s binom(J,k)`.

For single-bit context updates,

`E_pi <= J*2^(J-1)`.

### Proof

The first bound is maximized when the zero and one truth classes are as balanced
as possible.  For the `s`-local bound, choose the source context and then the
nonempty changed-bit set of size at most `s`; only a subset of these directed
pairs crosses from zero to one.  Single-bit pairs are orientations of edges of
the `J`-cube, which has `J*2^(J-1)` edges. QED.

Appending one of `K_bool` transition kinds and one of `N_owner` exact tokens
gives total address stock at most

`N_owner*K_bool*2^(2J-2)`

under arbitrary transitions, with the corresponding local-update replacements.

## AC3oo -- Boolean boundary localization and ticket bound -- PROVED

Give every exact gate address

`(pi,x^-,x^+,kappa_bool)`

an integer capacity `c_bool`, consumed once when that boundary gate is charged
and not restored inside the fixed-builder epoch.

Then the number of charged Boolean recreation episodes is at most

`C_bool=sum c_bool`.

Moreover, a weighted family of Boolean returns of total weight `W` contains one
exact gate address of weight at least

`W/(N_owner*K_bool*E_max)`,

where `E_max` is any valid per-token boundary-stock bound from AC3on.

### Proof

AC3om assigns each recreation episode exactly one first false-to-true boundary
edge.  Charging consumes one unit of its exact address capacity, so the episode
count is bounded by the initial capacity sum.  The weighted statement is
pigeonhole over the finite address stock. QED.

One context edge may recreate several owner tokens.  Their exact token-boundary
addresses remain separate unless a shared-capacity theorem is supplied.

## AC3op -- closure for fixed finite Boolean builder semantics -- PROVED UNDER THE BOOLEAN-BOUNDARY CONTRACT

Inside one epoch with fixed finite context bits and fixed predicates `f_pi`,
assume every Boolean recreation gate satisfies at least one of:

1. the directed boundary edge is impossible under the transition rules;
2. traversing it gives an improving or terminal output;
3. traversing it strictly advances another bounded integer potential;
4. it consumes finite unrestorable capacity at its exact Boolean gate address;
5. the predicate or bit interpretation changes and the step is recorded as an
   outer builder reset.

Then arbitrary finite Boolean context-only recreation cannot sustain an infinite
nonterminal history inside one fixed-builder epoch.

### Proof

AC3om gives every exact recreation one canonical boundary gate.  Routes 1--4
forbid or bound repetition of every fixed-builder gate.  Route 5 exits the epoch.
Recreation-free common-owner segments are bounded by AC3nz, so only finite work
occurs between the finitely many Boolean gates. QED.

## Corrected AC4 owner frontier

Fixed nonconjunctive Boolean semantics are no longer an unstructured owner
recreation case.  They reduce to complete false-to-true context boundary edges.
The remaining owner frontiers are:

- changing builders not represented as decorated outer resets;
- unbounded or nonphysical context dictionaries;
- boundary capacities which can themselves be recreated;
- nonadditive owner resources outside support atoms, finite context states and
  spent vectors;
- interaction between these gates and the unresolved availability, conflict,
  reverse and arithmetic macro-cycle fields.

## Finite check

`scripts/verify_ac_boolean_boundary_gates.py` exhausts every nonconstant Boolean
predicate on up to three bits and short destruction/recreation paths.  It checks
the canonical first boundary, arbitrary and single-bit boundary-stock bounds,
weighted localization and exact capacity accounting.
