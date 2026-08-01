# Minimal coset-crossing shell action

`docs/589` proves that the three stored shell actions span exactly the even-coordinate-sum sublattice of cycle-resource space. This chapter adds the smallest possible conditional action that crosses the missing coset and recomputes the exact periodic cost.

## 1. Minimal lattice completion

### Theorem PP3ctd -- PROVED / UNIT COSET ACTION COMPLETES THE LATTICE

Each nonnegative unit cycle vector

```text
(1,0,0), (0,1,0), (0,0,1)
```

has odd coordinate sum and therefore lies outside the source action lattice. Adding any one of them as a fourth action makes the augmented integer column lattice equal to all of `Z^3`.

#### Proof

The original determinant is two. For each augmented four-column system, one of the `3 x 3` minors has determinant one. Hence the gcd of maximal minors is one and the generated lattice is `Z^3`. Unit vectors have minimum positive nonnegative `l_1` norm, so the completion is minimal. ∎

## 2. Exact target-service cost

### Theorem PP3cte -- PROVED / PARITY FORCES TWO USES

The twenty-slot target cycle total is

```text
(12,10,8),
```

which has even coordinate sum. Therefore any added odd-sum action must occur an even number of times in an exact target decomposition.

For each of the three unit actions, the smallest positive exact use count is two. The corresponding original-action counts are

```text
unit 1: (4,6,4),
unit 2: (6,6,2),
unit 3: (4,8,2).
```

Each augmented period has sixteen active controls and four idle slots, compared with fifteen active controls and five idle slots in the source period. The exact throughput cost is therefore

```text
1/20
```

per period.

#### Proof

Subtract `z` copies of the added unit vector and apply the exact half-integral inverse of the original incidence matrix. Integrality is equivalent to even `z`; direct evaluation gives the displayed smallest nonnegative solutions at `z=2`. ∎

## 3. Buffer frontier is unchanged

### Theorem PP3ctf -- PROVED / COSET COMPLETION DOES NOT REDUCE STARTUP BUFFER

For all three unit-action choices, exact Pareto optimization of the twenty-slot ordering gives minimum cycle-buffer `l_1` norm

```text
2/5.
```

Thus the minimal lattice completion costs one additional active slot and does not improve the best startup buffer.

#### Proof

A finite dynamic program over the exact action multiplicities stores the Pareto-minimal componentwise prefix-deficit vectors. Each augmented action set has the same three minimum frontier vectors as the source system, with least `l_1` value `2/5`. ∎

## 4. Exact audit

Run

```bash
python scripts/check_shell_coset_crossing_action.py
```

The checker verifies the determinant-one augmented minors, the parity rule, all smallest exact count vectors, and the complete prefix-buffer Pareto frontiers.

## 5. Prime-patching consequence

The index-two obstruction has a sharp conditional repair: one unit cycle action suffices algebraically, but exact service uses it twice and pays a nonvanishing `1/20` throughput cost. No source-level clean-macro action with such an odd cycle vector is currently identified.
