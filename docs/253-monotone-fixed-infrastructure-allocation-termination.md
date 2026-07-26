# Monotone fixed-infrastructure allocation termination

PP3aux--PP3avf provide the restart rule needed after a paid source repair.  The slab
coordinates, numerical labels, and candidate-cell universe remain fixed.  Controller
pairings may evolve inside the fixed pool rectangles, but every newly activated
same-slot entry is required to start with zero anchor mass.

The current numerical potential is

```text
Theta_E(S)=Xi_cell(S)+Lambda_E(S),
```

where `E` is the current pool matching.  Although the active anchor entry set changes,
PP3auz--PP3ava compare consecutive values exactly: old entries may disappear, new
entries contribute zero at activation, and all candidate-cell insertion is excluded.
Every failed allocation therefore gives a strict decrease of a nonnegative integer.

## 1. Permanent slab infrastructure

Fix once and for all

```text
(X_i,Y_i)_(i in [M]),
Aset,
Bset,
V_cell.
```

Assume the current distinguished source layer has the form

```text
P=E_1 dot-union ... dot-union E_M dot-union E_*,
```

where every `E_i` is a perfect matching between `X_i` and `Y_i`.  Let `Q` be the
complementary source matching layer.

A **permanent-infrastructure state** is a saturated no-three source with this fixed
matching-block decomposition.  Only the pairings inside the blocks may change.

### Proposition PP3avg -- PROVED

Every pool-compatible block repair from PP3avc maps a permanent-infrastructure state
to another permanent-infrastructure state.

#### Proof

Each block trade is a tied permutation inside one current matching block and fixes all
other blocks.  Hence every `E_i` remains a perfect matching between the same
`X_i,Y_i`, while `E_*` and `Q` retain their coordinate sets.  Source validity and
saturation are supplied by the complete restart-support cycle. ∎

## 2. Uniform completion energies

The patch-only external event table depends only on the fixed slab coordinates,
numerical labels, and proposed patch points.  The ordinary two-slot source-anchor
estimate PP3hk uses only:

1. two source points in every old row and column;
2. the fixed slab interval length `R`; and
3. the fixed label scale `T`.

### Proposition PP3avh -- PROVED

At every permanent-infrastructure state:

1. the patch-only external mass remains within the established `o(1)` budget; and
2. the ordinary two-slot source-anchor mass remains `o(1)` at every slot.

#### Proof

Pool-compatible repairs do not change the slab or label geometry, so the patch-only
relations are unchanged.  Every repaired source is still saturated, so the proof of
PP3hg--PP3hk applies verbatim to the current source. ∎

Thus every attempt satisfies the same completion-energy hypotheses as the first.

## 3. Allocation failure produces current potential credit

Perform the controller-aware random two-sided allocation using the current pool
matchings `E_i` and the fixed labels `Aset,Bset`.

### Proposition PP3avi -- PROVED / CONDITIONAL ESTABLISHED CONVERSION INTERFACES

If the allocation does not install the macro patch, it produces a marked source set
`D`, `|D|<=W`, carrying positive designated credit in the current potential
`Theta_E(S)`.

More precisely:

1. a movement/refill blocker star or bank carries `Xi_cell` credit;
2. a same-slot anchor star or endpoint bank carries `Lambda_E` credit;
3. fixed-macro defect and fixed-label score masses refine to one of these two types;
4. every terminal source pencil converts to one of these credited types; and
5. every insertion pencil enters the established bounded cancellation chain.

#### Proof

Apply PP3aur--PP3aut to the current attempt.  Candidate-cell defects are incidences in
`V_cell`, hence in `Xi_cell`.  Same-slot anchor defects are exactly active incidences
in `Lambda_E`.  The remaining refinements and terminal conversions are PP3aug and
PP3aqo--PP3aqt. ∎

No credit is transferred to an inactive latent anchor entry.

## 4. One permanent-infrastructure step

### Theorem PP3avj -- PROVED / CONDITIONAL ESTABLISHED CONVERSION INTERFACES

From every permanent-infrastructure state `(S,E)`, exactly one of the following
occurs.

1. The random two-sided controller-aware allocation installs the simultaneous
   saturated no-three macro patch.
2. A finite pool-compatible repair package produces another
   permanent-infrastructure state `(S',E')` satisfying

   ```text
   Theta_(E')(S')<Theta_E(S).
   ```

Every newly activated same-slot entry in item 2 has zero anchor mass at `S'`.

#### Proof

The fixed-attempt theorem PP3auu and the uniform budgets PP3avh give either successful
allocation or the credited structure of PP3avi.  Apply PP3avd.  Its independent
branch has zero candidate-cell insertion and zero anchor activation, strictly
reduces the current potential, and preserves the infrastructure by PP3avg.  Its
dense-support branch belongs to the established canonical conversion chain and
terminates in the same paid branch. ∎

No pool coordinate set, row set, numerical label, or candidate-cell universe is
replaced.

## 5. Finite monotone termination

### Theorem PP3avk -- PROVED / CONDITIONAL ESTABLISHED CONVERSION INTERFACES

Starting from one permanent-infrastructure state, repeat PP3avj after every failed
attempt.  After finitely many repairs, an allocation attempt installs the macro patch.

#### Proof

For every state `(S,E)`, `Theta_E(S)` is a nonnegative integer by PP3auy.  PP3avj
compares consecutive values and makes each failed attempt strictly decrease that
integer.  Therefore failed attempts cannot occur indefinitely.  Since PP3avj has no
third outcome, a later attempt must take the successful allocation branch. ∎

An explicit upper bound on the number of repair packages is the initial value
`Theta_(E_0)(S_0)`.

## 6. Slab-optimal completion theorem

### Theorem PP3avl -- PROVED / CONDITIONAL ESTABLISHED PRIME-PATCHING INTERFACES

At the slab-optimal scales

```text
M=m^(1/20+o(1)),
R=m^(19/20+o(1)),
W=m^(19/40+o(1)),
T=MW=m^(21/40+o(1)),
```

fix disjoint slab coordinate pools with `MR<(1-o(1))m` and the actual movement and
refill label sets.  Assume the established local patch, support-conversion, and direct
paid-trade interfaces used through PP3avj.

Then the monotone fixed-infrastructure process installs a saturated no-three patch of
width

```text
Omega(m^(21/40)).
```

#### Proof

The slab pools exist by PP3gr.  The complete fixed infrastructure and helper
reservoirs are supplied by PP3auj--PP3aup.  Apply PP3avk.  A successful allocation
completes by PP3ho, PP3hk, and the patch-only energy theorem. ∎

Restart comparability itself is no longer an additional hypothesis.

## 7. Revised focused frontier

### Corollary PP3avm -- PROVED

Inside the slab-optimal controller-aware chain, none of the following remains an
independent frontier:

1. changing controller pairings between attempts;
2. changing active safe domains after a paid repair;
3. reassigning ownership or label matchings;
4. replenishment of same-slot anchor mass;
5. addition of positive-mass candidate entries; or
6. an unbounded sequence of failed fixed attempts.

All attempts use one fixed coordinate-label infrastructure.  New anchor entries are
activated only at zero mass, and every failed attempt strictly decreases the current
nonnegative integer potential.

The remaining work is a proof-audit and assembly task: verify that every conditional
conversion interface used in PP3avi and PP3avd has matching hypotheses, and then
connect the slab patch theorem to the global prime-gap induction.

The no-three-in-line conjecture remains unproved.
