# Ambient unary positive support: exact avoidance and witness conversion

PP3age leaves a linear ambient foreign-unary star through one typed endpoint
resource.  As with binary support, event weight or candidate-incidence
multiplicity is irrelevant when the selected state avoids the underlying positive
support cell.

For a conditioned single-cycle state, the subbank-retention factor and the
one-arc cylinder probability cancel exactly.  Sparse positive support can
therefore be avoided.  Dense support gives a linear fixed-resource forbidden-cell
star; its retained-source witness pairs yield a square-root source star or a
square-root endpoint-disjoint credited bank.

## 1. Distinct positive unary signatures

Fix one typed ambient endpoint resource `v` in a tied bank of `Q` indices.  Let

```text
S_1(v)
```

be the number of distinct positive foreign-unary support cells whose endpoint-
index support has rank two and contains `v`.  Count each cell once regardless of
its insertion weight or the number of candidate incidences it blocks.

Condition on retaining the index of `v`, choose the other `q-1` indices uniformly,
and choose a uniform single-cycle state on the selected block.

### Proposition PP3amk -- PROVED

Every fixed non-diagonal positive unary signature incident with `v` is selected
with probability

```text
p_1=1/(Q-1).
```

#### Proof

The other endpoint index is retained with probability `(q-1)/(Q-1)`.  Conditional
on the selected block, the prescribed directed arc occurs in a uniform
single-cycle state with probability `1/(q-1)` by PP3yy.  Multiply and cancel. ∎

The probability is independent of the adaptive filler size `q`.

## 2. Complete positive-support avoidance

Let `R_c>0` be the marked removal credit and let `Z_other` be the normalized
nonnegative objective containing all source-invalid events and all paid insertion
classes except the complete positive unary support through `v`.

### Theorem PP3aml -- PROVED / CONDITIONAL RESIDUAL-SLACK INTERFACE

Suppose

```text
E Z_other <= 1-tau
```

for one fixed `tau in (0,1)`.  If

```text
S_1(v)<tau(Q-1),
```

then some conditioned single-cycle state is source-valid, selects no positive
unary support cell through `v`, and has remaining insertion cost below `R_c`.
It gives a strict paid improvement.

#### Proof

Let `X_1` count selected distinct positive unary cells.  Proposition PP3amk gives

```text
E X_1=S_1(v)/(Q-1)<tau.
```

The expectation of `Z_other+X_1` is below one.  In an outcome of value below one,
the integer source-invalid and support counts vanish, while the remaining
normalized paid cost is below one.  Every unary weight supported on an avoided
cell is zero in that state. ∎

### Corollary PP3amm -- PROVED

Failure of unary positive-support avoidance under residual slack `tau` forces

```text
S_1(v)>=tau(Q-1)=Omega(Q).
```

Thus a large unary event multiplicity on a small support is never a separate
obstruction.

## 3. Witness graph of a dense fixed-resource star

All cells counted by `S_1(v)` share one typed endpoint row or column resource.
Choose one retained-source witness pair for every positive unary cell.

### Proposition PP3amn -- PROVED

The chosen witness pairs are distinct edges of a simple graph on retained source
points.

#### Proof

In the fixed-column form, the replaced endpoint in that old column is deleted
before insertion, so a unary witness line through two retained source points is
nonvertical.  It meets the fixed column in at most one selected cell.  The fixed-
row form is transposed.  This is the nonaxis argument PP3wd. ∎

### Theorem PP3amo -- PROVED

For every integer `D>=1`, a dense unary support star of size `S_1(v)` contains
either

1. one retained source point in at least `D` witness pairs; or
2. a vertex-disjoint witness-pair matching of size at least `S_1(v)/(2D)`.

Taking `D=ceil(sqrt(S_1(v)))` gives a source star or witness matching of size
`Omega(sqrt(S_1(v)))`.

#### Proof

Apply the maximal-matching star--matching argument PP3we to the simple witness
graph from PP3amn. ∎

## 4. Endpoint-bank conversion and adaptive scale

In the witness-matching branch, pigeonhole the ordered source-layer type and one
endpoint position.  The selected endpoints lie in one permutation layer, have
distinct old rows and columns, and each destroys one designated unary incidence
when moved.  Puncture any selected endpoint that is an active controller elsewhere;
endpoint-disjointness preserves every designated incidence.

### Theorem PP3amp -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

A non-paid ambient unary support star through `v` has one of the following
outcomes.

1. A conditioned single-cycle state avoids its complete positive unary support
   and gives a strict paid improvement.
2. A free or one-controller-punctured source-star centre of size
   `Omega(sqrt(Q))`.
3. A controller-disjoint credited endpoint bank of size `Omega(sqrt(Q))`.
4. Robust final-state direct completion.
5. A positive-density ambient binary support core.
6. Residual marked source/paid load already consumes the centre credit.
7. Source, transition, anchor, Hall, alternating, distinguished-endpoint, or
   endpoint-host preparation fails explicitly.

#### Proof

Use PP3aml.  On failure apply PP3amm--PP3amo, the layer refinement PP3wg, batch
puncturing PP3akl, and the marked-star/recapture-free/final-state conversion
chains. ∎

Under the adaptive condition `q^3/Q=o(1)`, one has

```text
q=o(Q^(1/3))=o(sqrt(Q)).
```

Hence the extracted unary star or bank is asymptotically larger than the selected
state scale.

### Corollary PP3amq -- PROVED

Raw multiplicity and an unstructured linear ambient unary support star are no
longer independent paid frontiers.  The remaining unary objects are a converted
source star, a credited witness bank, residual marked collateral, or explicit
host failure.

The no-three-in-line conjecture remains unproved.
