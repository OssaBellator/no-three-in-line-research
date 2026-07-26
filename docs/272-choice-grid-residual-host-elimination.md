# Uniform residual-host closure for two-resource choice grids

The complete two-resource grid theorem PP3ze and its rank-three middle-grid
specialization PP3acq are stated with a common-superregular-residual hypothesis.
At their actual call sites this hypothesis is automatic.  Every local state fixes
exactly two compatible endpoint cells, hence deletes exactly two left and two
right resources from one common superregular endpoint host.  The slicing loss is
uniform over all local states, and the resulting matching spread constant may be
chosen uniformly.

This chapter removes residual-host failure as an independent choice-grid output.
It does not pay a weighted grid, a candidate-rich projective cover, or concentrated
source/non-grid insertion mass.

## 1. Uniform finite deletion

Let

```text
G=(L,R;E), |L|=|R|=q,
```

be `(epsilon,delta)`-superregular, where `delta>0` is fixed and `epsilon>0` is
sufficiently small.  A compatible local state `s=(a,b)` consists of two allowed
cells with distinct left and right endpoints.  Let `G_s` be the graph obtained by
deleting those two left and two right endpoints.

### Proposition PP3bat -- PROVED

For every fixed `epsilon'>epsilon`, uniformly over all compatible local states,

```text
G_s is (epsilon',delta-o(1))-superregular.
```

In particular, for all sufficiently large `q`, every `G_s` is
`(epsilon',delta/2)`-superregular and has a perfect matching.

#### Proof

Deleting two vertices on each side changes every surviving degree by at most two
and changes normalized degrees by `O(1/q)`.  For surviving sets
`X,Y` of size at least `epsilon'(q-2)`, adjoining the deleted vertices if needed
changes the tested sets by `O(1)`, while the edge count changes by `O(q)`.  The
normalized density and regularity discrepancy therefore change by `o(1)`,
uniformly in the four deleted endpoints.  The standard superregular perfect-
matching consequence applies. ∎

### Corollary PP3bau -- PROVED

The residual-host conclusion applies simultaneously to every state in:

1. the complete two-resource state set of PP3ze;
2. the rank-three middle state set of PP3acq; and
3. every hereditary restriction obtained by deleting source-invalid local pairs.

#### Proof

All these states fix two compatible cells in the same parent host.  Hereditary
restriction removes states, not host edges, so PP3bat remains uniform. ∎

## 2. Uniform matching spread

### Proposition PP3bav -- PROVED FROM THE EXISTING SUPERREGULAR SPREAD THEOREM

There is a fixed constant `K=K(epsilon',delta)>0`, independent of the local state
`s`, such that every residual host `G_s` admits the fixed-rank spread matching law
used by PP3ze and PP3acq.

#### Proof

By PP3bat, for large `q` every residual host belongs to the single parameter
class `(epsilon',delta/2)`-superregular and has order `q-2`.  Apply the established
superregular spread theorem with these common parameters.  Its constant depends
only on the parameter class and the bounded support rank, not on the identities
of the deleted endpoints. ∎

Thus the phrase “with one common fixed-rank spread constant `K`” in PP3ze and
PP3acq is supplied by the caller rather than an additional conversion interface.

## 3. Exact choice-grid call sites

### Theorem PP3baw -- PROVED

At a complete two-resource choice-grid call inside the superregular branch, the
residual-host and common-spread hypotheses of PP3ze are automatic.  Consequently
exactly one of the following occurs.

1. The averaged paid inequality of PP3ze holds and a source-valid strict decrease
   is selected.
2. Its negation produces the weighted-grid, candidate-rich, deterministic local
   invalidity, source-ranked, or non-grid insertion concentration recorded by
   PP3zg--PP3zi.

There is no residual-host-failure alternative.

#### Proof

Every state in the compatible state set has a uniformly superregular residual
host by PP3bat and the common spread law by PP3bav.  Apply PP3ze.  Negating its
single averaged inequality gives exactly the nonnegative concentrated summands
listed in PP3zg--PP3zi. ∎

### Theorem PP3bax -- PROVED

At the rank-three middle-grid call of PP3aco--PP3acs, the residual-host and common-
spread hypotheses of PP3acq are automatic.  The middle branch therefore reduces
to paid completion, weighted middle multiplicity, a candidate-rich projective
cover, or explicit source/non-middle residual concentration.

#### Proof

The map of PP3aco identifies each middle state with a compatible pair of local
cells in one common superregular host.  Apply PP3bau--PP3bav and then PP3acq--
PP3acr. ∎

## 4. Revised complete-grid endpoint

### Corollary PP3bay -- PROVED

The fifth “host failure” item in the revised complete-grid endpoint of PP3ze--
PP3zi is empty at a superregular choice-grid call.  The exhaustive endpoint is:

1. paid average completion;
2. a quadratic weighted grid at the combined-credit scale;
3. a candidate-rich projective cover or rich candidate matching;
4. deterministic local invalidity, source-ranked collateral, or non-grid
   insertion concentration.

Conditional Hall or alternating-component analysis is not re-entered merely by
fixing a compatible local pair.

#### Proof

This is PP3baw.  PP3bat rules out loss of superregularity after the bounded local
deletion, and PP3bav supplies the matching distribution required by the paid
first moment. ∎

### Corollary PP3baz -- PROVED

For the dense current-support row, residual host feasibility is no longer open
for complete two-resource grids or rank-three middle grids.  The live grid
frontier consists only of weighted multiplicity, projective candidate covering,
and typed source or non-grid paid concentration.

The arc/path-petal, fixed-cell fan, dense source-support, and global prime-minus-
one seed frontiers remain separate.

The no-three-in-line conjecture remains unproved.

## 5. Finite diagnostic

The exact finite deletion check is exercised by

```bash
python scripts/check_choice_grid_residual_hosts.py \
  experiments/choice-grid-residual-hosts-example.json
```

The checker verifies parent and residual minimum degree, exhaustive large-subset
density discrepancy for a small finite graph, compatible two-cell states, and a
single residual superregular parameter class shared by every state.  It is a
finite regression check, not a replacement for the asymptotic slicing theorem.
