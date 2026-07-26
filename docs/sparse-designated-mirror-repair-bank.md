# Designated mirror repairs under original-swap composition

**Branch:** `research/sparse-algebraic-spread`

SAS5ae--SAS5ai produce endpoint-disjoint donor transpositions for reflected-label
defects, and SAS5aj--SAS5an extract a globally constraint-compatible subbank.
A reflected mirror record still requires the two original swap columns to exchange
labels.  Therefore a donor transposition repairs its designated record only when
composed with the fixed original swap.

This note states the corrected interface.  The fixed swap `omega={x,y}` is
applied once, together with a donor subbank.  Distinct defect columns give
distinct designated records, and global compatibility preserves them
simultaneously.  Donor energy is additive relative to the post-`omega` coloring.

## Designated donor records

Fix one original swap `omega={x,y}`, one destruction word, its mirror repair word,
one failing non-swapped row position and one required label `ell`.

Let `B` be an endpoint-disjoint donor bank from SAS5ag.  Every member

`tau={z_tau,q_tau}`

comes with one retained mirror record `Q_tau` such that:

- `z_tau` is its unique defect column in the fixed failing role;
- `q_tau` currently carries label `ell`;
- `q_tau` is outside the scope of `Q_tau`;
- after applying `omega`, every scope column of `Q_tau` except `z_tau` has its
  required label.

The bank uses distinct defect columns and distinct donor columns, all outside
`{x,y}`.  Hence `omega` commutes with every donor transposition.

## SAS5ao -- distinct defect columns give distinct designated records -- PROVED

If `tau` and `sigma` are distinct members of `B`, then

`Q_tau != Q_sigma`.

### Proof

The failing non-swapped row position is fixed throughout the role.  An exact
record has one column in that position, namely its defect column.  The donor bank
uses distinct defect columns, so two selected records cannot be the same exact
record. QED.

## SAS5ap -- the composed move repairs its designated mirror record -- PROVED WITH ORIGINAL-SWAP COMPOSITION

For every `tau in B`, the combined move

`omega union tau`

changes `Q_tau` from unsatisfied in the original coloring to satisfied.
Equivalently, applying `tau` to the post-`omega` coloring repairs `Q_tau`.

### Proof

The original swap puts the required opposite labels at `x,y`.  Before the donor
transposition, the designated defect column `z_tau` still has the wrong label.
The donor `q_tau` carries the required label `ell` and lies outside the record
scope.  Applying `tau` puts `ell` at `z_tau` without altering any other scope
column.  Thus all three required labels are present after the composed move.
QED.

A donor transposition alone need not repair the mirror record, because it leaves
`x,y` unswapped.  This is the composition correction.

## SAS5aq -- global compatibility preserves all composed designated repairs -- PROVED WITH ORIGINAL-SWAP COMPOSITION

Let `I subseteq B` be independent in the global donor interaction graph of
SAS5aj.  Apply `omega` once and every donor transposition in `I`.  Then every
designated record `Q_tau`, `tau in I`, is satisfied after the combined move.
Hence it repairs at least `|I|` distinct designated mirror records.

### Proof

The composed move `omega union tau` repairs `Q_tau` by SAS5ap.  Independence says
no constraint scope meets endpoints of two selected donor transpositions, so no
other donor in `I` changes a column of `Q_tau`.  The common original swap acts in
the required way on every mirror record.  Distinctness follows from SAS5ao. QED.

The designated records have multiplicity exactly one in the selected donor bank.

## SAS5ar -- quantitative composed mirror-repair extraction -- PROVED WITH ORIGINAL-SWAP COMPOSITION

Suppose a reflected-label defect family has total weight `W`, there are `b`
labels, every label class has `d` donor columns, and the diffuse threshold is
`mu>0`.  Assume the global column-incidence cap is `Lambda`.

In the diffuse branch of SAS5ai, define

`M=min(ceil(W/(b*mu)),(d-3)_+)`.

Then there is a globally constraint-compatible donor subbank of size at least

`ceil(M/(4*Lambda+1))`.

Applying the original swap together with this subbank repairs at least that many
distinct designated mirror records.

### Proof

SAS5ae retains a required-label class of weight at least `W/b`.  SAS5af and
SAS5ag produce an endpoint-disjoint donor bank of size at least `M`.  SAS5aj
colours its interaction graph with at most `4*Lambda+1` colours, so one colour
class has size at least the displayed ceiling.  Apply SAS5aq to that independent
class. QED.

The conclusion is a count statement.  It does not claim that one selected record
per defect column carries a fixed fraction of the original weight.

## SAS5as -- corrected composed-move energy router -- PROVED

Write `kappa^omega` for the coloring after the original swap.  For a donor
transposition `tau`, define its post-swap energy increment

`Delta_(tau|omega)=T((kappa^omega)^tau)-T(kappa^omega)`.

For an independent donor subbank `I`,

`T(kappa^(omega union I))-T(kappa)
 = [T(kappa^omega)-T(kappa)] + sum_(tau in I) Delta_(tau|omega)`.

Moreover the combined move repairs at least `|I|` distinct designated mirror
records.  Therefore exactly one of the following holds:

1. the combined move lowers the original energy;
2. it does not lower the original energy, but still realizes the quantified
   designated mirror-repair bank with an exact post-`omega` additive ledger.

### Proof

Apply SAS5ak to the donor transpositions using `kappa^omega` as the baseline.
Independence makes their post-swap energy changes additive.  Add the energy
change of `omega`, and use SAS5aq for the designated repairs. QED.

A swap-local minimum does not eliminate the first branch: local minimality
controls single transpositions at the original coloring, not a composed
multi-transposition move or donor increments evaluated after `omega`.

## Corrected SAS6 frontier

The diffuse reflected-label route now has a valid composed continuation:

- a combined original-plus-donor move which lowers energy; or
- a quantified bank of distinct simultaneous designated mirror repairs with an
  exact additive donor ledger relative to the post-original-swap coloring.

The remaining work is weighted and arithmetic: control represented weight per
defect column, classify designated and collateral records, and handle
high-incidence or reflected-board boundary profiles.

## Finite check

`scripts/verify_sparse_designated_mirror_repairs.py` exhausts small balanced label
assignments, endpoint-disjoint donor banks, designated scopes and interaction
graphs.  It applies the original swap and donor subbank as a composed move and
checks record distinctness, individual composed repair, simultaneous survival,
the colouring bound and post-swap energy additivity.
