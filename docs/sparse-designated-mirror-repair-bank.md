# Designated mirror repairs surviving global donor compatibility

**Branch:** `research/sparse-algebraic-spread`

SAS5ae--SAS5ai produce endpoint-disjoint donor transpositions for reflected-label
defects, and SAS5aj--SAS5an extract a globally constraint-compatible subbank with
exact additive energy.  This note connects those two interfaces directly to the
original mirror records.

Every donor transposition has one designated reflected record which it repairs.
Distinct defect columns give distinct designated records.  Therefore the global
compatibility extraction preserves a quantitatively large family of simultaneous
mirror repairs, even when no donor swap lowers the energy.

## Designated donor records

Fix one original swap `{x,y}`, one destruction word, its mirror repair word, one
failing non-swapped row position and one required label `ell`.

Let `B` be an endpoint-disjoint donor bank from SAS5ag.  Every member

`tau={z_tau,q_tau}`

comes with one retained mirror record `Q_tau` such that:

- `z_tau` is its unique defect column in the fixed failing role;
- `q_tau` currently carries label `ell`;
- `q_tau` is outside the scope of `Q_tau`;
- all other columns of `Q_tau` already have their required labels.

The bank uses distinct defect columns and distinct donor columns.

## SAS5ao -- distinct defect columns give distinct designated records -- PROVED

If `tau` and `sigma` are distinct members of `B`, then

`Q_tau != Q_sigma`.

### Proof

The failing non-swapped row position is fixed throughout the role.  An exact
record has one column in that position, namely its defect column.  The donor bank
uses distinct defect columns, so two selected records cannot be the same exact
record. QED.

## SAS5ap -- every donor swap repairs its designated mirror record -- PROVED

For every `tau in B`, applying `tau` alone changes `Q_tau` from unsatisfied to
satisfied.  Consequently its individual repair count satisfies

`R_tau>=1`.

### Proof

Before the transposition, the unique designated defect column `z_tau` has the
wrong label.  The donor `q_tau` carries the required label `ell`.  Local safety
places `q_tau` outside the designated scope, so swapping the labels at
`z_tau,q_tau` fixes the defect and leaves every other required column of
`Q_tau` unchanged. QED.

## SAS5aq -- global compatibility preserves all designated repairs -- PROVED

Let `I subseteq B` be independent in the global donor interaction graph of
SAS5aj.  Apply all transpositions in `I` simultaneously.  Then every designated
record `Q_tau`, `tau in I`, is satisfied after the batch.

Hence the batch repairs at least `|I|` distinct designated mirror records.

### Proof

The transposition `tau` repairs `Q_tau` by SAS5ap.  Independence says no
constraint scope meets endpoints of two selected transpositions.  Therefore no
other selected transposition changes any column of `Q_tau`.  Distinctness follows
from SAS5ao. QED.

This is stronger than the general repair-multiplicity-three bound for the
designated subfamily: designated records have multiplicity exactly one in the
selected bank.

## SAS5ar -- quantitative mirror-repair extraction from diffuse defect mass -- PROVED

Suppose a reflected-label defect family has total weight `W`, there are `b`
labels, every label class has `d` donor columns, and the diffuse threshold is
`mu>0`.  Assume the global column-incidence cap is `Lambda`.

In the diffuse branch of SAS5ai, define

`M=min(ceil(W/(b*mu)),(d-3)_+)`.

Then there is a globally constraint-compatible donor subbank of size at least

`ceil(M/(4*Lambda+1))`,

and its simultaneous application repairs at least that many distinct designated
mirror records.

### Proof

SAS5ae retains a required-label class of weight at least `W/b`.  SAS5af and
SAS5ag produce an endpoint-disjoint donor bank of size at least `M`.  SAS5aj
colours its interaction graph with at most `4*Lambda+1` colours, so one colour
class has size at least the displayed ceiling.  Apply SAS5aq to that independent
class. QED.

The conclusion is a count statement.  It does not claim that the designated
records carry a fixed fraction of the original weight, because several weighted
records may share one defect column.

## SAS5as -- designated-repair energy router -- PROVED

For the compatible subbank `I` from SAS5ar, exactly one of the following holds.

1. The simultaneous donor batch lowers the energy.  By SAS5ak its gain is the sum
   of the individual gains.
2. The simultaneous batch does not lower the energy.  It nevertheless creates at
   least `|I|` distinct designated mirror records, while all additional changed
   constraints are confined to the donor endpoints and the exact additive ledger
   of SAS5ak.

At a balanced swap-local minimum only the second branch can occur.

### Proof

SAS5ak gives exact energy additivity.  SAS5aq gives `|I|` distinct designated
repairs independently of the sign of the total energy change.  The alternatives
partition according to that sign.  At a local minimum no balanced batch can have
negative energy change. QED.

## Corrected SAS6 frontier

The diffuse reflected-label route now has a quantitative end product tied to the
original defect mass:

- a compatible improving donor batch; or
- at least `ceil(M/(4*Lambda+1))` distinct simultaneous designated mirror repairs.

The remaining work is genuinely weighted and arithmetic:

- control how much original defect weight is represented by one selected record
  per defect column;
- classify the designated and collateral repaired records through the finite word
  and parameter dictionaries;
- handle high-incidence and reflected-board boundary profiles.

The existence and simultaneous survival of a large designated mirror-repair bank
are no longer open.

## Finite check

`scripts/verify_sparse_designated_mirror_repairs.py` exhausts small balanced label
assignments, endpoint-disjoint donor banks, designated scopes and interaction
graphs.  It checks record distinctness, individual repair, simultaneous survival
on independent sets, the colouring bound and the diffuse quantitative router.