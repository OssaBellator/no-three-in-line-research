# Normalized builder-state boundary gates for changing context semantics

**Branch:** `research/alternating-core-chain`

AC3om--AC3op close context-only recreation for one fixed finite Boolean predicate.
A builder change may alter the predicate, the context-bit dictionary or the legal
transition relation.  If the complete builder state is nevertheless drawn from
one finite reconstructed family, this apparent semantic change is still a finite
state transition and has the same canonical first false-to-true boundary.

This note makes that normalization explicit.  It closes finite changing-builder
semantics under exact boundary tickets, descent or terminal output.  It does not
cover unbounded builder dictionaries or builder changes whose physical state is
not reconstructed.

## Normalized builder states

Fix one outer super-epoch.  Let `Beta` be a finite set of exact builder labels.
For each `beta in Beta`, let `X_beta` be its finite reconstructed internal context
state set.  Form the disjoint normalized state space

`Y = {(beta,x): beta in Beta, x in X_beta}`.

An exact owner token `pi` has unchanged physical identity and a currentness map

`g_pi:Y->{0,1}`.

The normalized address retains every field needed to distinguish equal symbolic
builders, including registry occurrence, phase, protection epoch, host generator,
context interpretation and owner occurrence.  A transition may change `beta`,
`x`, or both.

Let `D` be the directed graph of legal normalized builder-state transitions.
A recreation path starts at `y_0` with `g_pi(y_0)=0` and ends at `y_m` with
`g_pi(y_m)=1`.

## AC3oq -- changing-builder recreation has a canonical normalized boundary -- PROVED

Every such path has one unique first index `j` satisfying

`g_pi(y_(j-1))=0` and `g_pi(y_j)=1`.

The exact directed legal edge `(y_(j-1),y_j)` is the canonical normalized
builder-state recreation gate.

### Proof

The truth word along the path begins with zero and ends with one.  Choose the
least index with value one.  The preceding value is zero by minimality, and the
least index is unique.  The path is legal, so the directed pair is an edge of
`D`. QED.

The source and target may use different builders and unrelated context-bit
alphabets.  No common literal or common coordinate system is required after the
states have been normalized into `Y`.

## AC3or -- explicit normalized boundary stock -- PROVED

Write

`Z_pi={y in Y:g_pi(y)=0}` and `O_pi={y in Y:g_pi(y)=1}`.

If `S=|Y|`, then the number of possible directed false-to-true gate addresses is
at most

`E_pi=|Z_pi|*|O_pi| <= floor(S^2/4)`.

Using the legal transition graph gives the sharper exact bound

`E_pi <= |E(D) intersect (Z_pi x O_pi)| <= |E(D)|`.

If every normalized state has legal outdegree at most `d_out`, then

`E_pi <= |Z_pi|*d_out <= S*d_out`.

### Proof

Every gate lies in `Z_pi x O_pi`, whose product is maximized by a balanced
partition of `S`.  Restricting to legal transitions leaves only the crossing
edges of `D`.  Summing at most `d_out` outgoing edges over the zero states gives
the last bound. QED.

Appending one of `K_build` transition kinds and one of `N_owner` exact tokens
gives total address stock at most

`N_owner*K_build*floor(S^2/4)`,

or the corresponding legal-edge bound.

## AC3os -- weighted localization and finite gate capacity -- PROVED

Give every exact address

`(pi,y^-,y^+,kappa_build)`

an integer capacity `c_build`, consumed when the gate is charged and not restored
inside the normalized super-epoch.  Then:

1. the number of charged changing-builder recreation episodes is at most
   `C_build=sum c_build`;
2. a weighted family of such episodes of total weight `W` contains one exact
   gate address of weight at least
   `W/(N_owner*K_build*E_max)`,
   where `E_max` is any valid per-token bound from AC3or.

### Proof

AC3oq assigns every episode one exact first false-to-true legal edge.  Charging
consumes one unit of its capacity, so the total episode count is bounded by the
initial stock.  Weighted pigeonhole over the finite address set gives the second
claim. QED.

One builder transition may recreate several owner tokens.  Their token-edge
addresses remain separate unless a shared-capacity theorem is installed.

## AC3ot -- closure for finite reconstructed changing-builder semantics -- PROVED UNDER THE NORMALIZED-BOUNDARY CONTRACT

Inside one finite normalized super-epoch, suppose every changing-builder
recreation gate follows at least one route:

1. the directed normalized edge is impossible;
2. traversing it gives an improving or terminal output;
3. traversing it strictly advances another bounded integer potential;
4. it consumes finite unrestorable capacity at its exact normalized gate address;
5. the transition leaves the reconstructed finite family and is recorded as a
   higher outer reset.

Then changing-builder owner recreation cannot sustain an infinite nonterminal
history inside that normalized super-epoch.

### Proof

AC3oq assigns every exact return one normalized boundary gate.  Routes 1--4
forbid or bound repetition of each gate, while route 5 exits the super-epoch.
There are finitely many gate addresses by AC3or.  Recreation-free common-owner
segments are bounded by AC3nz, so only finite work occurs between the finitely
many builder gates. QED.

## Corrected AC4 owner frontier

Fixed predicates and finite changing-builder families are now both boundary-gate
problems.  The remaining owner frontiers are:

- unbounded or nonreconstructed builder/context state spaces;
- transitions that change owner identity without an occurrence-faithful map;
- normalized gate capacities that can themselves be recreated;
- nonadditive resources outside support atoms, finite normalized states and spent
  vectors;
- interaction with unresolved availability, conflict, reverse and arithmetic
  macro-cycle fields.

Thus ordinary finite builder switching is no longer an unstructured recreation
case.

## Finite check

`scripts/verify_ac_builder_state_boundary_gates.py` exhausts small disjoint
builder-state families, nonconstant currentness maps, legal transition graphs and
short recreation paths.  It checks the canonical first crossing, product and
legal-edge stock bounds, outdegree bounds, weighted localization and exact ticket
accounting.