# Exact `m=8` critical witnesses and the parity-clean macro graph

`docs/325` proves that the unrestricted flaw-targeted graph at `m=8` has exact
strict-descent horizon five, with 44 sharp states at the minimum positive defect
level `B_3=4`.  This chapter classifies those witnesses and compares them with
the owner-intersecting parity-clean macro action from `docs/316` and `docs/320`.

No uniform asymptotic horizon or seed theorem is claimed.

## 1. Support dichotomy for the 44 sharp witnesses

### Theorem PP3bnl -- VERIFIED FINITELY / CRITICAL SUPPORT CLASSIFICATION

The 44 signed Hamilton states at `m=8` with strict-descent distance five have the
following exact structure:

```text
32 states: one three-owner flaw support and no two-owner support,
12 states: one two-owner flaw support and no three-owner support.
```

They lie on 14 Hamilton cycles and form 22 pairs under simultaneous complement
of all eight orientation bits.

#### Verification

The checker reconstructs the exact two-owner and three-owner interaction tables,
identifies the `B_3=4` states at distance five from the lower level, and counts
the nonzero owner-support masks.  The global-complement pairing is tested on the
state indices themselves. ∎

Thus every sharp state consists of a single quarter-turn orbit of bad triples,
but that orbit may be owned by either two or three signed assignments.  The
parity-clean manifold retains exactly the 32 three-owner states and excludes the
12 two-owner states.

## 2. Forced first-step collateral

### Theorem PP3bnm -- VERIFIED FINITELY / FIRST-STEP PROFILE

For the 44 sharp states, the minimum defect count among all legal one-step
targeted neighbours has distribution

| minimum neighbour `B_3` | states |
|---:|---:|
| 4 | 4 |
| 8 | 8 |
| 12 | 8 |
| 16 | 20 |
| 20 | 4 |

Every shortest five-move path to validity has one of the two move words

```text
F,R,R,R,R : 12 states,
R,R,R,R,R : 32 states,
```

where `F` is a targeted owner-orientation flip and `R` is a targeted
three-source successor rotation.

#### Proof

Each two-owner sharp state has one bad owner pair, so its only supported move
type is an orientation flip at one of the two owners.  Each three-owner sharp
state has one bad owner triple, so its only supported move type is the successor
rotation on those owners with eight possible fresh sign assignments.  Exact
neighbour scoring gives the displayed first-step distribution.  Reverse BFS
from the valid set records a shortest successor for every sharp state and gives
the two move words. ∎

In particular, 40 of the 44 sharp states must strictly increase `B_3` on the
first move.  The obstruction is a genuine collateral-repair phenomenon rather
than a failure to choose fresh signs well.

## 3. Exact parity-clean macro graph

A parity-clean macro step is defined as follows.  Start from a parity-clean
signed Hamilton state `x`, choose a present three-owner flaw with owner set `S`,
choose a source triple `T` such that

```text
T intersect S != empty,
```

require the successor rotation on `T` to have a satisfiable target parity
system, and then choose any clean orientation in the target fibre.  By PP3blo,
the selected old flaw is deleted; by PP3bmd, the target clean fibre is explicit.

### Proposition PP3bnn -- PROVED / IMPLICIT MACRO PREDECESSORS

Fix a parity-clean target cycle `eta` and a source triple `T`.  Put

```text
rho = switch_T(eta).
```

A parity-clean signed state `x` over `rho` has a macro edge to every clean
orientation over `eta` if and only if `x` contains a three-owner flaw whose owner
set intersects `T`.

#### Proof

The successor rotation on a fixed source triple is an involution, so `rho` is
the unique predecessor cycle for label `T`.  The target-fibre choice is
arbitrary among clean orientations.  A forward macro move with label `T` is
legal exactly when some selected flaw owner set `S` meets `T`; then PP3blo
deletes that flaw.  No orientation data from the target fibre enter the
legality test. ∎

Consequently reverse search can be compressed through target cycles: once one
clean orientation over `eta` has known distance `d`, all legal predecessor
states described above have distance at most `d+1`.

### Theorem PP3bno -- VERIFIED FINITELY / COMPLETE CLEAN-MACRO REACHABILITY

The parity-clean signed Hamilton state space at `m=8` has

```text
404,080 states.
```

Every one reaches a valid state under the owner-intersecting parity-clean macro
action.  The exact distance distribution is

| macro distance to validity | states |
|---:|---:|
| 0 | 28 |
| 1 | 66,844 |
| 2 | 303,576 |
| 3 | 33,632 |

Thus the maximum macro distance is three.

#### Verification

The checker constructs every parity-clean orientation fibre, starts reverse BFS
from the 28 valid states, and applies PP3bnn without materializing the macro edge
set.  It verifies that all 404,080 clean states are reached and compares the
complete distance distribution against the stored ledger. ∎

## 4. The five-step obstruction disappears after parity preprocessing

### Corollary PP3bnp -- VERIFIED FINITELY / SHARP WITNESS COLLAPSE

The 32 sharp three-owner states from PP3bnl have exact parity-clean macro-distance
distribution

```text
1:12,
2: 4,
3:16.
```

Hence no sharp unrestricted witness requires more than three parity-clean macro
steps.  The 12 two-owner sharp states do not belong to the parity-clean manifold
and are removed from this residual process by parity preprocessing.

#### Proof

The 32 three-owner states have no two-owner support, so they are included in the
complete macro search of PP3bno.  Reading their verified distances gives the
distribution.  The remaining 12 states each contain a two-owner flaw and are
therefore outside the clean state space by definition. ∎

This is the strongest finite evidence so far for separating the algorithm into

```text
parity preprocessing,
then owner-intersecting clean macro repair.
```

The unrestricted five-step horizon is not the relevant residual obstruction on
that manifold.

## 5. Revised descent frontier

The finite data now give two different horizons at `m=8`:

```text
unrestricted targeted graph: exact strict-descent horizon 5,
parity-clean macro graph:     maximum distance to validity 3.
```

The next asymptotic targets are:

1. prove that pair-safe logarithmic-near-clean states from `docs/326` can be
   brought to the clean manifold without losing Hamilton mobility;
2. prove a uniform clean-macro distance or strict-descent horizon;
3. classify the 33,632 clean states at macro distance three by flaw geometry;
4. derive a weighted potential on clean fibres whose one-step macro drift is
   negative;
5. combine the three-step finite macro phenomenon with the weighted Hall
   transport of `docs/324` and the trajectory-local window of `docs/317`.

The exact `m=8` macro result does not prove asymptotic clean reachability or the
prime-minus-one seed theorem.
