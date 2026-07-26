# Inverse-conic layers and the exact one-layer extension CSP

The remaining prime-minus-one seed problem asks for two edge-disjoint
permutation graphs whose union has no Euclidean collinear triple.  A natural
structured first layer comes from the modular conic

```text
xy=a  (mod p).
```

Every nonzero scaled inverse graph is individually no-three-in-line.  This
gives a rigorous nonlinear layer family, but exact extension tests show that
the family is too rigid in several of the first unresolved sizes: no scaled
inverse layer extends to a saturated seed for `p=13,17,19,23,29,31`.

The same extension solver also resolves a one-defect `p=17` near-state.  Both
of its layers are individually no-three and their union has only one bad
line, yet neither layer admits any compatible second permutation.  Hence
repair cannot be confined to one layer; coordinated movement in both
permutations is genuinely necessary.

These are structural and finite results.  They do not prove or disprove the
asymptotic seed theorem.

## 1. Scaled inverse layers are permutation caps

Let `p` be prime and let `a` be nonzero modulo `p`.  For
`x in {1,...,p-1}`, let

```text
f_a(x)
```

be the least positive representative of `a x^(-1) mod p`, and put

```text
P_a={(x,f_a(x)):1<=x<=p-1}.
```

### Theorem PP3bdr -- PROVED

`P_a` is a permutation graph on `[p-1]^2` and contains no three collinear
points over the integers.

#### Proof

Multiplication by `a` and inversion are bijections of the nonzero residues,
so `f_a` is a permutation of `[p-1]`.

Suppose three points of `P_a` were collinear over the integers.  Reducing
their zero determinant modulo `p` would put three distinct points of the
affine conic

```text
xy=a
```

on one affine line over `F_p`.  A vertical line meets the conic in at most
one point.  On a nonvertical line `y=mx+b`, intersection points satisfy

```text
m x^2+b x-a=0,
```

which has at most two roots over a field.  This is a contradiction. ∎

Thus modular conic geometry gives a valid Euclidean one-layer construction,
even though modular cap arguments do not by themselves construct the full
two-layer seed.

## 2. Exact extension by line capacities

Let `P` be any no-three permutation graph on `[n]^2`.  For every maximal
nonaxis grid line `L`, define its residual capacity

```text
c_P(L)=2-|P cap L|.
```

Let `Q` be a second permutation graph, disjoint from `P`.

### Theorem PP3bds -- PROVED

The union `P union Q` is a saturated no-three set if and only if:

1. `Q` is a permutation graph;
2. `Q` avoids the selected cell of `P` in every column; and
3. for every maximal nonaxis line `L`,

   ```text
   |Q cap L| <= c_P(L).
   ```

#### Proof

The two permutation conditions give exactly two distinct points in every row
and column.  A nonaxis line contains at most two points of the union exactly
when its contribution from `Q` is at most `2-|P cap L|`.  Horizontal and
vertical lines already contain exactly two points by saturation.  Apply the
maximal-line equivalence PP3bcy. ∎

This is a one-permutation binary CSP with capacities zero, one, or two.

## 3. Secant pruning and Hall feasibility

A line containing two points of `P` has capacity zero.

### Proposition PP3bdt -- PROVED

Before search, every cell on a secant of `P`, except the two already selected
cells, may be deleted from every second-layer domain.  During search, a
partial assignment may be rejected whenever either:

1. some line capacity is exceeded; or
2. the bipartite graph from unassigned columns to currently legal unused
   rows has no perfect matching.

Both rejections are logically exact.

#### Proof

A third selected point on a secant of `P` would be collinear with its two
`P` points, so secant pruning removes only impossible cells.  A completed
second permutation restricted to the unassigned columns would be a perfect
matching in the current column--row domain graph.  Hence failure of Hall's
condition rules out every completion of the partial assignment. ∎

## 4. Complete MRV--Hall backtracking

### Theorem PP3bdu -- PROVED

The following finite algorithm decides whether a fixed clean layer `P`
extends.

1. Generate every maximal nonaxis line by primitive direction and first
   board point.
2. Apply secant pruning.
3. Choose an unassigned column of minimum current domain size.
4. Try every unused legal row, maintaining every line occupancy.
5. At every node, reject a branch if the remaining domain graph has no
   perfect matching.

The algorithm returns an extension if and only if one exists.

#### Proof

Every candidate returned by the algorithm satisfies the permutation,
disjointness, and line-capacity constraints of PP3bds.  Conversely, after
the sound pruning of PP3bdt, the search branches over every legal value of
every column.  MRV changes only the order.  Hall rejection removes only
branches with no possible permutation completion.  Therefore every feasible
second layer is reached by one surviving branch. ∎

The diagnostic implementation uses exact integer geometry and a complete
augmenting-path matching test.  Its negative results are finite
unsatisfiability certificates produced by exhaustive search, not heuristic
failures.

## 5. Finite scaled-inverse extension classification

### Proposition PP3bdv -- VERIFIED FINITELY

For every nonzero multiplier `a`, the complete extension solver gives:

```text
p=5:  extendable a = 1,2,3,4
p=7:  extendable a = 2,3,4,5
p=11: extendable a = 3,5,6,8
p=13: no extendable a
p=17: no extendable a
p=19: no extendable a
p=23: no extendable a
p=29: no extendable a
p=31: no extendable a
```

Every tested first layer is no-three by PP3bdr.  For the six negative prime
cases, all `p-1` multipliers are exhausted by the complete algorithm
PP3bdu.

The largest search tree among one multiplier in each negative case has,
respectively,

```text
71, 58, 25, 55, 78, 63
```

visited MRV nodes.  Secant pruning and Hall failure make these fixed-layer
instances highly rigid.

#### Verification

Run

```bash
python scripts/check_inverse_layer_extension.py \
  experiments/inverse-layer-extension-example.json
```

The checker verifies every inverse layer directly, constructs all residual
line capacities, and executes the complete extension solver. ∎

This finite classification disproves the simple ansatz “take any scaled
inverse layer and add a suitable permutation” as a uniform construction
through the tested range.  It does not prove failure for later primes or for
other nonlinear first layers.

## 6. One-defect p=17 state requires two-sided repair

Consider

```text
sigma =
[11,7,9,16,2,10,6,1,15,4,13,14,5,12,8,3],

tau =
[6,13,10,14,5,9,4,12,16,1,11,15,8,3,2,7].
```

### Proposition PP3bdw -- VERIFIED FINITELY

Both permutation graphs are individually no-three.  Their union has exactly
one collinear triple,

```text
(1,11), (3,10), (13,5),
```

using one-based coordinates.  Nevertheless:

```text
there is no second layer extending the fixed sigma layer;
there is no second layer extending the fixed tau layer.
```

Consequently no repair changing only one permutation exists, even if all
sixteen values of that permutation may move.  Any repair of this near-state
must alter both layers.

#### Verification

The determinant checker finds one bad triple in the union and none in either
layer.  The exact extension solver exhausts the fixed-`sigma` and fixed-`tau`
CSPs in `86` and `50` MRV nodes, respectively. ∎

This is stronger than the earlier bounded-support audit: the obstruction is
not merely invisible to transpositions or six-column rearrangements.

## 7. Revised structured seed frontier

### Corollary PP3bdx -- PROVED / FINITE BARRIERS RECORDED

The global seed problem now has the following exact structured picture.

1. Scaled inverse graphs provide a uniform family of clean nonlinear
   permutation layers.
2. Completing a fixed clean layer is an exact line-capacity permutation CSP.
3. Secants of the first layer can make this CSP rigid enough for very short
   complete non-extension proofs.
4. Near-feasible two-layer states may require coordinated changes in both
   layers; a one-layer repair theorem cannot be sufficient in general.
5. The remaining asymptotic route must therefore use a more flexible
   structured family, a genuinely two-layer construction, or a coordinated
   repair/absorption theorem.

The prime-minus-one seed theorem and the no-three-in-line conjecture remain
unproved.
