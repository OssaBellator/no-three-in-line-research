# Multiplicity-blind allocation bypass for current-row grids and fans

The dense current-support row has been reduced to typed weighted objects.  Two of
its largest objects are a complete two-resource choice grid and a fixed-cell heavy
partner fan.  Their weights count candidate incidences with multiplicity, whereas
the final controller-aware allocation depends only on which controller-edge--label
entries are unavailable.

At the actual fixed-attempt call site this distinction is decisive.  If the base
controller domains do not have fixed linear margin, PP3aur already extracts a
separate credited star or bank.  Otherwise one or two fixed endpoint cells, together
with a residual endpoint matching of size `n=o(R)`, create only `O(n)` simple domain
loss, independently of candidate multiplicity.  The weighted grid or fan may then be
ignored while choosing a source-valid endpoint state and absorbed by the surviving
allocation margin.

This chapter removes weighted grid multiplicity, projective candidate covering, and
uniform heavy partner multiplicity as independent current-row frontiers.  It does
not remove an explicit source-validity concentration or failure of the non-grid base
allocation criteria.

## 1. Simple line traces from a bounded fixed local state

Let `F={a_1,...,a_k}` be a compatible fixed local endpoint state, where `k` is one
for a fixed-cell fan and two for a choice-grid state.  Let

```text
M={b_1,...,b_n}
```

be a residual endpoint matching compatible with every cell of `F`.  The
**fixed-state line family** consists of

```text
ell(a_i,b_j), 1<=i<=k, 1<=j<=n,
```

and the lines `ell(a_i,a_j)` between fixed cells.  Duplicate lines are retained only
once.

### Proposition PP3bbh -- PROVED

The fixed-state line family contains at most

```text
L_k(n)=kn+binom(k,2)
```

nonaxis lines.  Viewed as a simple bipartite incidence graph between controller
edges and one movement label, or between controller edges and one refill label, its
maximum degree on either side is at most `L_k(n)`.

#### Proof

There are `kn` fixed--residual pairs and `binom(k,2)` fixed--fixed pairs.  Every
pair of compatible endpoint cells determines a nonvertical, nonhorizontal line.
For one such line, PP3agu shows that a prescribed movement label, refill label, or
controller edge supports at most one candidate entry of the corresponding type.
Summing over at most `L_k(n)` lines gives the degree bound.  Coincident lines only
reduce the simple union. ∎

For `k=1` this recovers PP3agv.  For `k=2` it is the union of two fixed-cell fans and
the one line joining the two local cells.

## 2. Exact paired-domain loss

Let `H_i^base(A,B)` be one refined controller domain after all source, anchor, and
non-fixed-state insertion exclusions have been imposed.  Let `H_i^F(A,B)` be the
domain after also deleting every movement or refill entry lying on the fixed-state
line family.

### Proposition PP3bbi -- PROVED

For every macro and label pair,

```text
|H_i^base(A,B)\H_i^F(A,B)| <= 2L_k(n).
```

This bound is independent of the number or weight of candidate incidences assigned
to any one line.

#### Proof

At the movement label `A`, Proposition PP3bbh removes at most `L_k(n)` controller
edges.  At the refill label `B`, it removes at most another `L_k(n)`.  Taking their
union gives the displayed bound.  Repeated candidate incidences on one deleted
entry do not create additional domain loss. ∎

### Corollary PP3bbj -- PROVED

At the slab-optimal scale, for `k<=2` and every residual matching size used in the
current row,

```text
2L_k(n)=o(R).
```

Consequently, for every fixed `xi>0`,

```text
2L_k(n)<=xi R
```

for all sufficiently large `m`.

#### Proof

The current endpoint hosts have `n=m^(kappa+o(1))` with `kappa<19/80`, while
`R=m^(19/20+o(1))`.  For fixed `k<=2`, `L_k(n)=O(n)=o(R)`. ∎

## 3. The fixed-attempt margin disjunction

### Proposition PP3bbk -- PROVED / CONDITIONAL EXISTING PAID CONVERSIONS

At every current-row grid or fan call inside one fixed allocation attempt, exactly
one of the following is available before the weighted fixed-state incidences are
charged.

1. Some movement or refill label has lost the fixed base margin; PP3aur extracts a
   target credited star or resource-disjoint bank and the direct paid chain applies.
2. Every relevant base domain has size at least `(gamma+xi)R` for fixed
   `gamma,xi>0`, and all balanced ownership and global label criteria are supported
   by the corresponding base margin graphs.

#### Proof

This is the individual-label-margin split of PP3aur followed by the fixed-attempt
allocation theorem PP3aus--PP3auu.  The fixed-state grid or fan entries are omitted
from the base domains in item 2 and inserted only after the endpoint state is
selected. ∎

Thus lack of base margin is already a different paid current structure, not a
failure caused by weighted grid or fan multiplicity.

## 4. Source-valid selection may ignore multiplicity

For every compatible fixed local state `s`, let `G_s` be its residual endpoint host
and choose the common spread matching law supplied by PP3bat--PP3bav.  Let `Y_s(M)`
be the number of source-invalid canonical patterns in the completed endpoint state.
All non-grid or nonfan deterministic endpoint conditions are included in this
count or in the base domains.

### Proposition PP3bbl -- PROVED

If

```text
(1/|S|) sum_(s in S) E_M Y_s(M) < 1,
```

then one fixed local state and residual matching give a source-valid endpoint trade.
No weighted grid or fan term is needed in this selection objective.

If the inequality fails, the caller has explicit source-validity mass at unit scale;
this is a typed source concentration rather than host or multiplicity failure.

#### Proof

Average the nonnegative integer `Y_s(M)` over a uniform local state and its common
spread residual matching.  An expectation below one gives an outcome with value
zero.  The negation is precisely a positive averaged source-pattern mass.  Uniform
residual-host existence and spread are PP3bat--PP3bav. ∎

## 5. Direct allocation after source-valid selection

### Theorem PP3bbm -- PROVED / CONDITIONAL BASE ALLOCATION CRITERIA

Suppose item 2 of PP3bbk holds and PP3bbl supplies a source-valid endpoint state
with `k<=2` fixed cells and residual matching size `n`.  Then, for all sufficiently
large `m`, inserting every candidate incidence supported by the fixed-state line
family preserves the controller-aware allocation graphs at threshold `gamma R`.
The same balanced ownership and global label matching therefore install the patch.

The conclusion is independent of:

- total weighted choice-grid multiplicity;
- the number of distinct candidates in a projective grid cover;
- fixed-cell partner multiplicities;
- the existence or size of a uniform heavy partner pencil.

#### Proof

By PP3bbi--PP3bbj, every paired domain loses at most `2L_k(n)<=xi R`.  Starting from
size at least `(gamma+xi)R`, it retains size at least `gamma R`.  Hence the base
margin graph is contained in the post-fixed-state margin graph, exactly as in
PP3agx.  Retain the same ownership and global label matching and apply PP3ho and
PP3hq.  Candidate multiplicity does not affect the simple domain deletion bound. ∎

## 6. Revised dense current-support endpoint

### Corollary PP3bbn -- PROVED

For the complete second-host dense current row, complete two-resource grids,
rank-three middle grids, fixed-cell fans, projective candidate covers, and heavy
partner pencils have only the following outcomes.

1. Base domain margin fails and a separate credited current structure is extracted.
2. Explicit source-validity or non-grid/base-domain concentration is produced.
3. A source-valid endpoint state is selected and the weighted grid or fan is absorbed
   by the fixed allocation margin, installing the patch.

Weighted multiplicity, candidate count, and heavy-pencil size are not independent
frontiers inside the slab-optimal fixed-attempt architecture.

The remaining current-row work is concentrated source/non-grid structure and the
arc/path-petal centre-core terms not represented solely by a bounded fixed-state line
family.  The dense source row and the global prime-minus-one seed theorem remain
separate.  The no-three-in-line conjecture remains unproved.

## 7. Finite diagnostic

Run

```bash
python scripts/check_current_row_multiplicity_bypass.py \
  experiments/current-row-multiplicity-bypass-example.json
```

The checker constructs the simple fixed-state line union for one fixed-cell fan and
one two-cell choice-grid state, verifies the line-count and controller-edge--label
degree bounds, computes exact paired-domain loss, and checks that the supplied base
margin survives.  It is a finite regression check for the multiplicity-blind domain
accounting.
