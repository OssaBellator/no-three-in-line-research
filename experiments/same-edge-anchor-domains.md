# Same-edge anchor domain diagnostics

This experiment accompanies
[`docs/72-same-edge-anchor-domain-pruning.md`](../docs/72-same-edge-anchor-domain-pruning.md).

Run

```bash
python scripts/analyze_same_edge_anchor_domains.py \
  certificates/prime-patching-small.json \
  --labels 12 --gamma 1/3 --epsilon 1/6
```

For each stored certificate and each perfect-matching layer, the analyzer uses the
chosen layer as the source-edge pool and the opposite layer as the fixed retained
source.  It constructs the refined label graph `J_{gamma,epsilon}`, checks the
PP3fe divisor-energy bound, and computes an exact maximum bipartite matching.

## Effect of label oversampling

At `gamma=1/2`, `epsilon=1/4`, the maximum refined-label matching sizes are:

| Side | 4 labels | 8 labels | 12 labels |
|---:|---:|---:|---:|
| 4 | `4,4` | `8,8` | `12,12` |
| 5 | `4,2` | `8,7` | `12,11` |
| 6 | `4,3` | `8,8` | `12,12` |
| 7 | `4,2` | `8,6` | `12,11` |
| 8 | `2,2` | `8,8` | `12,12` |
| 9 | `1,0` | `5,5` | `9,9` |
| 10 | `2,1` | `6,6` | `12,10` |

Each pair lists layers zero and one.  The important feature is that the graph is
not intrinsically sparse: enlarging the candidate boundary-label reservoir can
restore a large matching even when a four-label window fails.

## Looser density threshold

With twelve candidate labels and

```text
gamma   = 1/3
epsilon = 1/6
```

the maximum matching has size `12` on both layers for every stored side
`8,9,10`.

The refined graph edge counts are:

| Side | Layer 0 | Layer 1 |
|---:|---:|---:|
| 8 | 139 | 137 |
| 9 | 126 | 123 |
| 10 | 128 | 111 |

The minimum refined domain sizes on graph edges range from two to three source
edges in these small cases.  These sizes are too small for the asymptotic PP3ff
local-lemma inequality, so this is a label-allocation diagnostic rather than a
finite completion certificate.

## Divisor-energy check

For every tested layer, the exact sum

```text
sum_(A,B) |U_(A,B)|
```

is at most the pool-anchor divisor energy from PP3fe.  The inequality is usually
loose, as expected: one source edge can have several anchor witnesses for the
same bad label pair, while `U_(A,B)` counts the edge once.

## Interpretation

The finite data support the global-label-oversampling route from PP3eh and PP3ff:

1. expose a boundary reservoir substantially larger than the installed macro
   width;
2. construct the fixed-pair and same-edge-anchor refined graph on that reservoir;
3. select only a large matching of labels;
4. apply PP3ff and then the weighted global endpoint PP3fk.

The remaining asymptotic issue is not the existence of any refined label edge.
It is proving, for almost every large macro pool, a matching of size
`Theta(sqrt(R))` whose edge domains have constant density.