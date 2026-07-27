# Immediate Hamilton flaw causality and the residual three-owner scale

The static coordinate-overlap graph in `docs/305` is too dense because it joins
all bad events sharing a source or target coordinate. A targeted deletion has a
much smaller deterministic influence region: every unchanged orbit block is
literally the same set of four cells before and after the move.

This chapter proves that a newly created atomic flaw must touch a newly inserted
orbit block. A fixed orbit block belongs to only `O(n^2 log n)` atomic collinear
triple flaws. Consequently the immediate causal outdegree of the complete flaw
kernel is `O(n^2 log n)`, one factor of `n` below the static coordinate clique.

For residual three-owner atomic flaws, whose probability is `Theta(n^-3)`, the
probability--causal-degree product is `O(log n/n)=o(1)`. Two-owner flaws remain
at the logarithmic scale, motivating the parity preprocessing in `docs/312`.
No flaw-walk termination theorem is claimed here.

## 1. New flaws must use new orbit blocks

Consider one labelled deletion transition from a signed Hamilton state `x` to a
state `y`. Let `D` be the set of removed orbit blocks and `I` the set of inserted
orbit blocks. An orientation flip has `|D|=|I|=1`; a successor rotation has
`|D|=|I|=3`.

### Proposition PP3bkq -- PROVED / DETERMINISTIC LOCALITY

Every atomic flaw that is present in `y` but absent from `x` contains at least
one block from `I`.

#### Proof

Every block outside `D` is unchanged, with the same four selected cells and the
same signed owner assignment in both states. Suppose an atomic flaw `B` in `y`
uses no inserted block. All cells and owner descriptors of `B` then belong to
unchanged blocks, so the identical atomic flaw was already present in `x`, a
contradiction. ∎

Thus immediate creation is governed by the inserted blocks, not by all source
and target coordinates touched by a static event description.

## 2. Atomic flaws through one fixed block

### Proposition PP3bkr -- PROVED

On an `n` by `n` grid, the number of atomic collinear-triple flaws containing a
fixed nondegenerate quarter-turn orbit block is

```text
O(n^2 log n).
```

#### Proof

The block contains four cells, so it is enough to count collinear grid triples
containing one fixed cell `q`. Parameterise a line through `q` by a primitive
integer direction `(a,b)` and put

```text
r=max(|a|,|b|).
```

There are `O(r)` primitive directions at scale `r`. Such a line contains at most
`O(n/r)` grid cells, hence at most `O((n/r)^2)` unordered pairs of other cells.
Summing over `1<=r<n` gives

```text
sum_r O(r) O((n/r)^2)
 = O(n^2 sum_r 1/r)
 = O(n^2 log n).
```

For a fixed cell triple, each cell is compatible with only constantly many
signed directed pair-block descriptors, so passing from geometric triples to
atomic flaws changes only the constant factor. Multiply by the four cells of
the fixed block. ∎

The logarithm is the familiar contribution of many primitive slope scales.

## 3. Immediate causal outdegree

Define a directed causal edge `A->B` when some state containing atomic flaw `A`
and some labelled deletion of `A` produces an output in which `B` is newly
present.

### Theorem PP3bks -- PROVED / SPARSE CAUSAL BOUND

Every atomic Hamilton flaw has immediate causal outdegree

```text
O(n^2 log n).
```

#### Proof

By PP3bkq, a newly created flaw contains an inserted block. For a fixed deletion
outcome there are at most three inserted blocks. Across all labels of a fixed
two-owner atomic flaw there are at most two possible inserted blocks. Across
all eight fresh-sign labels of a fixed three-owner flaw, each of the three new
pair edges has two possible orientations, so there are at most six possible
inserted blocks in total.

Apply PP3bkr to each of these constantly many blocks and take their union. ∎

This is smaller by a factor `n` than the `Omega(n^3 log n)` source-coordinate
clique in the static overlap graph.

## 4. Probability--causality separation by owner count

The exact atomic flaw probabilities from PP3bki are

```text
p_2(m)=1/[4(m-1)_2] = Theta(n^-2),
p_3(m)=1/[8(m-1)_3] = Theta(n^-3),
```

where `n=2m`.

### Corollary PP3bkt -- PROVED / RESIDUAL SUBCRITICAL SCALE

Let `d_r(n)` be the maximum immediate causal outdegree of an `r`-owner atomic
flaw under the complete deletion rule. Then

```text
p_2(m) d_2(n) = O(log n),
p_3(m) d_3(n) = O(log n/n) = o(1).
```

#### Proof

Combine PP3bks with the two exact probability orders. ∎

The second product is asymptotically below the symmetric local-lemma scale. This
does not by itself prove a flaw-walk criterion: the directed causal graph and
delete-then-mix charges must still satisfy the hypotheses of an appropriate
algorithmic theorem. It does identify the two-owner family as the only owner
class retaining the logarithmic probability--degree scale.

After solving the two-owner parity CSP from `docs/312`, every remaining flaw has
three owners, so the residual family lies at the `O(log n/n)` immediate-causal
scale.

## 5. Exhaustive finite causality census

### Proposition PP3bku -- VERIFIED FINITELY

For `m=4,5,6`, every atomic flaw, every state containing it, every labelled
deletion output, and every newly present atomic flaw were enumerated exactly.

| `m` | atomic flaws | deletion transitions | maximum new flaws in one transition | maximum causal outdegree | causal edges |
|---:|---:|---:|---:|---:|---:|
| 4 | 224 | 3,456 | 12 | 48 | 7,296 |
| 5 | 2,032 | 65,024 | 40 | 176 | 172,352 |
| 6 | 8,160 | 1,060,864 | 76 | 704 | 2,196,736 |

Separated by owner count, the maximum immediate outdegrees are

```text
m=4: two-owner 24,  three-owner 48,
m=5: two-owner 152, three-owner 176,
m=6: two-owner 364, three-owner 704.
```

#### Verification

Run

```bash
python scripts/check_hamilton_immediate_flaw_causality.py \
  experiments/hamilton-immediate-flaw-causality-audit.json
```

The checker uses atomic flaw keys containing both the cell triple and its signed
owner assignments, and records only flaws absent before but present after each
deletion. ∎

## 6. Revised causal frontier

The static coordinate graph is not the relevant scale for local deletion. The
remaining route is now sharply staged:

1. solve or condition away the two-owner parity subsystem;
2. work with residual three-owner flaws and their `O(n^2 log n)` immediate causal
   neighborhoods;
3. combine this sparse dynamic graph with the near-stationary charges from
   delete-then-mix regeneration;
4. prove a directed flaw-walk, witness-sequence, or partial-rejection criterion.

The probability--causality product is favorable after parity preprocessing, but
no asymptotic termination or seed-existence theorem is claimed.
