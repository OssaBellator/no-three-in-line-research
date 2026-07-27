# Parity-fibre regeneration, the forest transition, and `m=9` mobility

`docs/315` and `docs/316` maintain the two-owner-clean manifold by solving a
signed parity graph after each cycle rotation.  The full clean orientation fibre
of one Hamilton cycle has additional exact structure: its component roots can be
randomized independently.

This chapter proves that fibre kernel, audits the constraint-graph topology
through `m=10`, and extends owner-intersecting clean mobility through `m=9`.
No asymptotic nonemptiness or termination theorem is claimed.

## 1. Exact component-root randomization

Let `G_rho` be the satisfiable signed parity graph of a Hamilton cycle `rho`, with
connected components `C_1,...,C_c`.  Fix one satisfying orientation vector
`e^(0)`.

### Proposition PP3bmd -- PROVED / EXACT FIBRE REGENERATION

Choose independent uniform bits `z_1,...,z_c` and complement every orientation
bit in component `C_j` when `z_j=1`.  The resulting vector is uniform on the
complete set of clean orientations of `rho`.

Every clean orientation occurs with probability

```text
2^(-c).
```

#### Proof

Parity propagation fixes all bits in one connected component after choosing one
root bit.  Complementing every bit in the component preserves every XOR edge,
and these are the only two satisfying assignments on that component.  Different
components have independent root choices.  Hence the map

```text
(z_1,...,z_c) -> clean orientation
```

is a bijection from `{0,1}^c` to the `2^c` satisfying vectors. ∎

Unlike nearest recleaning, this kernel is randomized and may change many signs,
but it restores exact uniformity inside the target orientation fibre in one
step.

## 2. Constraint count and atom bound

Let `q(rho)` be the number of parity edges of a satisfiable constraint graph.

### Corollary PP3bme -- PROVED

The number of connected components satisfies

```text
c(rho) >= m-q(rho),
```

and therefore every atom of the exact fibre kernel is at most

```text
2^(q(rho)-m).
```

If the constraint graph is a forest, equality holds:

```text
c(rho)=m-q(rho),
|clean fibre|=2^(m-q(rho)).
```

#### Proof

A graph on `m` vertices with `q` edges has at least `m-q` connected components.
Apply PP3bmd.  Equality in the component bound is equivalent to every component
being a tree or an isolated vertex. ∎

This is a single-input output-atom bound.  It is not automatically an action
charge bound, because different flaw-containing inputs may send mass to the same
clean output.

## 3. Exact topology through `m=10`

### Theorem PP3bmf -- VERIFIED FINITELY / FOREST TRANSITION LOCATED

Every Hamilton-cycle parity system was reconstructed exactly for `4<=m<=10`.
The clean fibre totals are:

| `m` | cycles | satisfiable cycles | clean orientation vectors | minimum components | maximum components |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 80 | 3 | 4 |
| 5 | 24 | 22 | 376 | 2 | 5 |
| 6 | 120 | 112 | 3,576 | 2 | 6 |
| 7 | 720 | 664 | 36,736 | 2 | 7 |
| 8 | 5,040 | 3,542 | 404,080 | 2 | 8 |
| 9 | 40,320 | 31,688 | 6,727,728 | 2 | 9 |
| 10 | 362,880 | 297,886 | 115,586,396 | 1 | 10 |

Every satisfiable constraint graph through `m=9` is a forest.  At `m=10` the
satisfiable cyclomatic-rank distribution is

```text
rank 0: 296,298 cycles,
rank 1:   1,588 cycles.
```

No satisfiable graph of rank at least two occurs in the audited range.

#### Verification

Run

```bash
python scripts/check_hamilton_parity_fibre_regeneration.py \
  experiments/hamilton-parity-fibre-regeneration-audit.json
```

The checker precomputes both XOR predicates for every compatible pair of signed
directed assignments, classifies every Hamilton cycle, solves each signed graph,
and records its edge count, component count, clean-fibre size, impossible-pair
count, and cyclomatic rank. ∎

The finite forest pattern is therefore genuine through `m=9` but not universal.
A future asymptotic argument must control consistent signed cycles rather than
assuming they do not exist.

## 4. Exact clean mobility at `m=9`

### Theorem PP3bmg -- VERIFIED FINITELY

At `m=9`:

```text
Hamilton cycles:                              40,320
parity-satisfiable cycles:                    31,688
directed successor rotations:             3,386,880
clean induced components:                         1
minimum clean degree:                            43
maximum clean degree:                            84
maximum distance from inconsistent to clean:      1
```

Moreover, for every clean cycle and every three-owner set, at least

```text
26
```

clean successor rotations intersect that owner set.

The directed transition counts are

```text
clean -> clean                2,273,712
clean -> inconsistent          388,080
inconsistent -> clean          388,080
inconsistent -> inconsistent   337,008.
```

#### Verification

The same checker constructs all source-triple rotations, uses exact tuple lookup
for their target cycles, computes the clean induced components, and counts clean
rotation triples meeting every possible owner triple. ∎

Thus the owner-intersecting macro targetability theorem from PP3blr extends from
`m<=8` to `m=9`.

## 5. A fibre-randomized parity-clean macro

### Corollary PP3bmh -- PROVED / NEW MACRO KERNEL

Let `(rho,e)` be parity clean and let `A` be a present three-owner flaw.  Suppose
`rho'` is any parity-satisfiable successor rotation whose source triple meets an
owner of `A`.  Perform that rotation and then apply the component-root kernel of
PP3bmd on `G_rho'`.

Then:

1. the old flaw `A` is deleted;
2. the output remains Hamilton, pair-2-cycle-free, and duplicate-orbit valid;
3. the output has no two-owner flaw;
4. conditional on the target cycle `rho'`, the output orientation is exactly
   uniform on its clean fibre;
5. every single-output atom has probability `2^(-c(rho'))` and hence at most
   `2^(q(rho')-m)`.

#### Proof

Owner intersection deletes the old flaw by PP3blo.  The cycle remains Hamilton by
PP3bjg.  PP3bmd samples exactly the satisfying orientation vectors of the target
parity graph, so all two-owner flaws are absent and the stated atom bounds hold. ∎

This kernel complements nearest recleaning:

```text
nearest recleaning:  bounded Hamming change, deterministic;
fibre regeneration: exact conditional uniformity, potentially global sign change.
```

## 6. Revised regeneration frontier

### Corollary PP3bmi -- PROVED / FRONTIER SHARPENED

The parity-clean process now has an exact one-step regeneration mechanism in the
orientation direction.  The remaining charge problem lies in the cycle
coordinate and in predecessor multiplicity, not in mixing the clean sign fibre.

The next targets are:

1. bound the distribution of `q(rho)` under a useful clean-cycle measure;
2. control how many flaw-containing predecessors can merge into one
   fibre-randomized output;
3. combine exact fibre regeneration with the `t=Theta(log n)` trajectory window
   from `docs/317`;
4. classify consistent signed parity cycles, which first appear at `m=10`;
5. prove asymptotic clean owner-intersecting mobility.

The exact fibre kernel and finite mobility do not prove asymptotic seed
existence.
