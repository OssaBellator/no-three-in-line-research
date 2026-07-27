# Immediate Hamilton causality and the locality--charge tradeoff

The coordinate-overlap graph in `docs/305` is too dense, but it is static: it
joins flaws whenever their prescribed coordinates overlap, regardless of what
one repair can actually create.  The complete local deletion rule from
`docs/307` has a much smaller immediate causal neighborhood.

This chapter proves that one local deletion can create only `O(n^2 log n)`
atomic flaws.  It then compares that locality with the constant immediate
charges and with the globally mixed near-probability charges from `docs/308`.
The two endpoints pull in opposite directions, isolating partial mixing as a
new quantitative frontier.

## 1. Grid triples through one fixed point

### Proposition PP3bkq -- PROVED

For a fixed cell `q` of `[n]^2`, the number of collinear grid-cell triples
containing `q` is

```text
O(n^2 log n).
```

The same bound holds for triples containing at least one cell of a fixed
four-cell quarter-turn orbit block.

#### Proof

Group primitive line directions `(a,b)` through `q` by

```text
d = max(|a|,|b|).
```

There are `O(d)` primitive directions at scale `d`.  A line in such a direction
contains `O(n/d)` grid cells, so after fixing `q` it contributes at most
`O((n/d)^2)` choices of two other cells.  Summing gives

```text
sum_(d<=n) O(d) O(n^2/d^2)
 = O(n^2) sum_(d<=n) 1/d
 = O(n^2 log n).
```

A quarter-turn orbit has four cells, changing only the constant. ∎

A geometric quarter-turn orbit has at most two directed signed-pair encodings,
corresponding to the two source--target directions.  Thus passing from geometric
triples to atomic signed-assignment flaws changes the bound by only a constant.

## 2. Immediate causal neighborhoods

For atomic flaws `A,B`, say that `A` immediately causes `B` when some state
containing `A` has a labelled targeted deletion outcome in which `B` is present
but was absent before the deletion.

### Theorem PP3bkr -- PROVED / SPARSE IMMEDIATE CAUSALITY

Every atomic flaw has immediate causal outdegree

```text
O(n^2 log n)
```

under the complete support-one/support-three deletion rule.

#### Proof

A two-owner deletion replaces one orbit block.  A three-owner deletion replaces
three orbit blocks.  Every unchanged orbit block contributes exactly the same
four cells before and after the move.

If a flaw `B` is newly present, at least one of its cells therefore lies in one
of the newly inserted blocks; otherwise all of its owner blocks and all three
cells were already present.  By PP3bkq, each inserted block belongs to only
`O(n^2 log n)` geometric collinear triples and hence only that many atomic flaws
up to a constant encoding multiplicity.  There are at most three inserted
blocks. ∎

This is a factor `n` smaller than the `Omega(n^3 log n)` source-coordinate clique
from PP3bjq.

## 3. Exact immediate deletion charges

Use the uniform-measure flaw charge

```text
gamma_A(R)
 = max_y sum_(x in A) R(x,y).
```

### Proposition PP3bks -- PROVED

For the uniform labelled deletion kernels from PP3bkj,

```text
two-owner flaw:   gamma_A = 1/2,
three-owner flaw: gamma_A = 1/8.
```

#### Proof

PP3bkj proves that the labelled deletion maps are injective.  Every two-owner
input has two equiprobable outputs and every three-owner input has eight.
Therefore every output column receives either zero mass or exactly `1/2` or
`1/8`, respectively. ∎

These charges are much larger than the atomic flaw probabilities
`Theta(n^-2)` and `Theta(n^-3)`.  Pure locality alone therefore does not recover
the probability scale needed by standard charge criteria.

## 4. Full mixing destroys locality

### Proposition PP3bkt -- PROVED / ENDPOINT TRADEOFF

Consider delete-then-mix actions `R_A K_m^t`.

1. At `t=0`, immediate causal outdegree is `O(n^2 log n)`, but charges are the
   constants from PP3bks.
2. Once `t` is at least the diameter of the lazy connected chain, every state
   has positive transition probability from every deletion output.  The causal
   neighborhood then contains every atomic flaw.
3. The three-owner atomic flaw family has size `Theta(n^4 log n)`.  Even when
   the mixed charge is reduced to `(1+o(1))Theta(n^-3)`, multiplying by the full
   causal family recovers the `Theta(n log n)` first-moment scale.

#### Proof

The first statement is PP3bkr and PP3bks.  For the second, connectedness gives a
path of length at most the diameter between any two states; laziness pads it to
any larger time.  Hence every transition entry is positive and every flaw can
appear.

For the third, PP3bje gives `Theta(n^4 log n)` strongly generic three-owner
flaws, and PP3bki gives probability `Theta(n^-3)` for each. ∎

Thus neither endpoint simultaneously supplies small charge and sparse
causality.  The missing object is an intermediate-time estimate describing how
quickly charge contracts compared with how quickly the causal light cone
spreads.

## 5. Exact finite causality audit

### Proposition PP3bku -- VERIFIED FINITELY

Exhaustive immediate-causality enumeration for `m=4,5,6` gives:

| `m` | atomic flaws | labelled deletion transitions | maximum new flaws in one transition | maximum causal outdegree |
|---:|---:|---:|---:|---:|
| 4 | 224 | 3,456 | 12 | 48 |
| 5 | 2,032 | 65,024 | 40 | 176 |
| 6 | 8,160 | 1,060,864 | 76 | 704 |

The total directed causal-edge counts are

```text
7,296,
172,352,
2,196,736.
```

#### Verification

Run

```bash
python scripts/check_hamilton_immediate_flaw_causality.py \
  experiments/hamilton-immediate-flaw-causality-audit.json
```

The checker groups every atomic flaw, evaluates every labelled deletion from
every containing state, and records exactly the flaws newly created by each
outcome. ∎

## 6. Revised dependency frontier

The static coordinate graph is too large, while the immediate causal graph is
geometrically sparse but carries constant action charges.  The next precise
target is an interpolation theorem.

Useful forms would include:

1. a bound `D(t)` on the number of flaws reachable after `t` unconditioned
   steps following one deletion;
2. a simultaneous charge bound `gamma(t)` with
   `gamma(t)D(t)=o(1)` or a suitable cluster analogue;
3. a slope- or distance-sensitive light cone rather than raw reachability;
4. a witness graph that records only likely, not merely possible, collateral
   flaws.

This locality--charge interpolation is now the central dependency problem.  No
asymptotic existence theorem is claimed.
