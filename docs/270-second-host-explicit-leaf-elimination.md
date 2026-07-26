# Elimination of raw second-host interface failures

The complete second-host theorem PP3azu lists four alternatives.  Its proof,
however, applies the buffered role-domain theorem PP3awo.  That theorem has only
two outcomes: a role-respecting independent helper assignment, or dense support
in the complete rank-at-most-three table.  After splitting dense support into
current and source types, there are three second-host outcomes, not four.

This chapter removes the phantom raw interface row.  It does **not** prove the
conditional conversion interfaces that may be reached later while processing a
dense current or dense source structure.

Throughout, one nonempty post-first-trade block contains `r` marked endpoint
roles, with

```text
1<=r<=W,
```

and the current potential is

```text
Theta_E^+=Xi_cell+Lambda_E+Xi_old.
```

## 1. Every local endpoint condition is already represented

### Proposition PP3bai -- PROVED

For the complete second-host cycle in one permanent matching block, every
positive local obstruction is represented in exactly one of the following two
ways.

1. A role-domain deletion forbids one helper value for one marked role.
2. A nonempty helper support of rank at most three belongs to the complete
   support hypergraph.

In particular:

- selected-controller and reserved-coordinate exclusions are role-domain
  deletions;
- cell distinctness and one-inserted-point failures have rank one;
- candidate-shadow, old-grid endpoint-shadow, transition, anchor, and
  two-inserted-point failures have rank at most two;
- internal triples and every remaining bounded distinguished-endpoint condition
  have rank at most three.

There is no additional distinguished-endpoint condition outside the table.

#### Proof

The complete endpoint normal form PP3atv--PP3aty exhausts saturation,
cell-distinctness, the one/two/three-inserted-point source-validity trichotomy,
controller preservation, candidate-shadow insertion, and every fixed
transition, anchor, pool, and distinguished-endpoint rule.  Strict alternation
gives each positive event nonempty ordinary-helper support of rank at most
three.  The old-grid term adds only rank-at-most-two supports by PP3ayd.
Controller membership and fixed reservations are imposed before selection as
role-domain deletions. ∎

## 2. Buffered role domains have no separate Hall failure

Let the helper reservoir be `H`.  For every marked role `j`, let `H_j` be its
allowed helper domain.  PP3baa supplies a fixed constant `kappa` such that

```text
|H\H_j|<=kappa r.
```

Put

```text
b=ceil((kappa+1)r).
```

### Proposition PP3baj -- PROVED

If the complete support hypergraph has an independent set `U` of size at least
`b`, then the marked roles have a role-respecting injective helper assignment
inside `U`.

Consequently no conditional Hall, alternating, non-superregular, or role-host
failure is produced by the raw second-host selection.

#### Proof

For every role,

```text
|U cap H_j|
>=|U|-|H\H_j|
>=b-kappa r
>=r.
```

For any nonempty role set `J`, the union of its allowed subsets inside `U`
contains the allowed subset of one role and therefore has size at least
`r>=|J|`.  Hall's condition holds, giving distinct representatives.

The construction is an assignment from a support-free helper set, not a
perfect-matching problem in a conditioned residual endpoint host.  Hence
alternating-component and non-superregular-host alternatives do not arise at
this call site.  A missing role domain is also impossible under the displayed
bound. ∎

This is the buffered Hall argument PP3awk, now applied to the exact universal
data recorded by PP3baa.

## 3. Failure of the independent assignment is typed support

### Theorem PP3bak -- PROVED / CONDITIONAL NAMED CONVERSION INTERFACES

For one complete second-host block, exactly one of the following occurs.

1. A pool-compatible source-valid cycle moves the whole marked block and creates
   zero new incidence in every component of `Theta_E^+`.
2. The complete support table produces an `Omega(r)` current credited
   structure.
3. The complete support table produces an `Omega(r)` source structure entering
   the fixed-template and paired-switch closure.

There is no fourth raw explicit-host alternative.

#### Proof

Trim the permanent block to `Theta(max(r^2,1))` helpers and apply PP3awo to the
complete support table of PP3bai.

If the required buffered independent set exists, PP3baj gives the
role-respecting assignment and PP3aty gives item 1.  If it does not exist,
PP3awl gives dense singleton, rank-two, or rank-three support.  Finite canonical
type refinement splits this support into current-potential events or
source-validity events.  The first class gives item 2; the second gives item 3.
These alternatives are exhaustive. ∎

The conditional status concerns conversion of the typed dense structures, not
existence of the three-way classification.

## 4. Revised complete second-host call matrix

### Corollary PP3bal -- PROVED

The raw second-host call matrix has four rows.

| Row | Raw outcome | Next step |
|---|---|---|
| A | independent zero-cost cycles in every block | complete insertion cancellation and strict payment |
| B | dense current support | current-credit localization and direct-payment chain |
| C | dense source support | old-grid unary payment or fixed-template/paired-switch source-host closure |
| E | robust final completion reached downstream | install the patch |

The former row D is empty.

Conditional Hall, alternating, non-superregular, distinguished-endpoint, and
role-host interfaces may still occur **downstream** inside a separately stated
current or source conversion theorem.  They are not independent outputs of the
complete second-host selector.

#### Proof

Apply PP3bak in each block.  Independent blocks are paid by PP3azt--PP3azw.
Dense current and source blocks are exactly rows B and C of PP3bac--PP3bad.
Robust final completion remains row E.  Proposition PP3baj eliminates a raw
row D. ∎

## 5. Revised second-host endpoint

### Theorem PP3bam -- PROVED / CONDITIONAL FINITE NAMED CONVERSION SET

For every source-valid first endpoint package, the complete blockwise second
host has exactly one of the following outcomes.

1. Complete insertion cancellation gives strict `Theta_E^+` payment.
2. A newly credited current structure enters its named conversion chain.
3. A typed source structure enters the fixed-template/paired-switch closure.
4. A robust final-state branch installs the patch.

Any named conditional interface failure occurs only after item 2 or item 3 has
already produced its typed geometric object.

#### Proof

Use PP3bak blockwise and the global helper accounting PP3baf.  If every block is
independent, use PP3bab.  Otherwise choose the first dense block and use its
typed current or source output.  The downstream alternatives are those already
recorded in PP3bac--PP3bad. ∎

## 6. Frontier reduction

### Corollary PP3ban -- PROVED

The complete second-host frontier no longer contains raw:

- role-domain failure;
- distinguished-endpoint failure;
- conditional Hall failure;
- alternating-component failure; or
- non-superregular-host failure.

The remaining local work is conversion of the typed current and source objects
produced by PP3bak, including any conditional interfaces explicitly generated
inside those later conversion chains.  The separate global frontier remains
the prime-minus-one seed theorem.

The no-three-in-line conjecture remains unproved.

## 7. Finite diagnostic

The elementary buffered-domain and outcome checks are exercised by

```bash
python scripts/check_second_host_leaf_elimination.py \
  experiments/second-host-leaf-elimination-example.json
```

The checker verifies quadratic helper supply, linear domain loss, support rank,
the buffered Hall lower bound, the three exhaustive raw outcomes, and absence
of a raw explicit-host-failure outcome.
