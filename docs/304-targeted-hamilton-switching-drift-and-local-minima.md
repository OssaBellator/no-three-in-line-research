# Targeted Hamilton switching: average drift and local-minimum barriers

The support-three Hamilton switching from `docs/303` is symmetric when source
triples are chosen without reference to the current defects.  To turn it into a
repair algorithm one instead chooses a present bad triple and rotates its three
orbit owners.  This chapter separates those two regimes and audits the most
natural line-defect potentials exactly.

## 1. Reversible kernels have zero stationary drift

### Proposition PP3bjm -- PROVED

Let `Omega_m` be the signed Hamilton state space and let `K` be the unconditioned
three-edge switching kernel from PP3bjj.  For every real function `Phi` on
`Omega_m`,

```text
E_[X uniform, Y sampled from K(X,.)] [Phi(Y)-Phi(X)] = 0.
```

#### Proof

PP3bjj makes `K` symmetric and reversible for the uniform measure `mu`.  Hence

```text
sum_(x,y) mu(x) K(x,y) (Phi(y)-Phi(x))
```

is its own negative after exchanging `x` and `y`, and is therefore zero. ∎

Thus any negative drift must come from defect-dependent targeting, a nonuniform
measure, or an augmented potential containing scheduling information.

## 2. Four natural defect potentials

For a selected set `P`, define

```text
B_3(P) = number of selected collinear triples,
B_L(P) = number of lines L with |L cap P|>=3,
E_L(P) = sum_L max(0,|L cap P|-2),
B_T(P) = number of collinear triples with three distinct orbit owners.
```

A triple counted by `B_T` can be targeted by the support-three kernel.

### Proposition PP3bjn -- VERIFIED FINITELY / NEGATIVE MEAN DRIFT

Exhaustive enumeration of every signed Hamilton state for `m=4,5,6`, every
present targetable triple occurrence, and all eight fresh-sign choices gives the
following occurrence-weighted mean drifts for `B_3`:

```text
m=4: -28/13,
m=5: -567/118,
m=6: -2057/494.
```

The corresponding mean drifts of `B_L`, `E_L`, and `B_T` are also negative at
all three pair sizes.

#### Verification

Run

```bash
python scripts/check_hamilton_targeted_switching_drift.py \
  experiments/hamilton-targeted-switching-drift-audit.json
```

The checker reconstructs every signed orbit set, groups selected cells by exact
integer line equation, and evaluates every target occurrence and sign outcome.
∎

This is evidence for a weighted-drift route, but it is not a pointwise theorem.

## 3. Best-sign nonmonotonicity

### Proposition PP3bjo -- VERIFIED FINITELY / MONOTONE-POTENTIAL BARRIER

None of `B_3`, `B_L`, `E_L`, or `B_T` is monotonically decreased by choosing the
best of the eight fresh-sign outcomes after every targeted rotation.

For `B_3`, explicit witnesses are:

```text
m=5:
rho          = [1,4,3,0,2]
orientations = [0,0,1,1,0]
sources      = {1,3,4}
old B_3      = 4
new B_3      = 24,20,24,20,20,20,24,24
```

and

```text
m=6:
rho          = [1,4,3,5,2,0]
orientations = [0,1,0,0,0,1]
sources      = {1,2,5}
old B_3      = 8
new B_3      = 48,48,48,48,48,44,48,44.
```

Hence the best available sign choice increases `B_3` by `16` and `36`,
respectively.  The maximum best-sign increases found for `(B_L,E_L,B_T)` are
`(6,8,12)` at `m=5` and `(16,12,40)` at `m=6`. ∎

## 4. Greedy local minima and targetability gaps

### Proposition PP3bjp -- VERIFIED FINITELY / LOCAL-SEARCH BARRIER

For total triple count, the exhaustive state classifications are:

| `m` | states | valid | improvable | nonvalid local minima | defective with `B_T=0` |
|---:|---:|---:|---:|---:|---:|
| 4 | 96 | 16 | 44 | 36 | 0 |
| 5 | 768 | 16 | 532 | 188 | 32 |
| 6 | 7,680 | 0 | 6,600 | 1,048 | 32 |

A state is called improvable when some targetable source set and some fresh-sign
choice strictly lowers the potential.  A local minimum has a targetable defect
but no such improving outcome.  The final column consists of defective states
with no three-owner bad triple at all, so the targeted support-three rule has no
legal flaw to select.

The other three potentials have analogous local minima.  In particular, merely
replacing `B_3` by line count, line excess, or targetable-triple count does not
remove the obstruction. ∎

## 5. Revised drift frontier

The support-three kernel has useful negative average drift in the first complete
finite range, but raw defect potentials do not prove termination.  A successful
drift theorem must therefore add at least one of:

1. geometric weights that charge prospective collateral lines;
2. a multi-step or look-ahead schedule that escapes one-step local minima;
3. a second repair primitive for bad triples with fewer than three orbit owners;
4. a nonuniform stationary measure that suppresses high-collateral states.

No asymptotic existence or termination theorem is claimed here.
