# Same-edge anchor domain diagnostics

This experiment accompanies
[`docs/72-same-edge-anchor-domain-pruning.md`](../docs/72-same-edge-anchor-domain-pruning.md)
and
[`docs/75-oversampled-refined-label-matching.md`](../docs/75-oversampled-refined-label-matching.md).

Run

```bash
python scripts/analyze_same_edge_anchor_domains.py \
  certificates/prime-patching-small.json \
  --labels 12 --gamma 1/3 --epsilon 1/6 \
  --output /tmp/refined-labels.json

python scripts/check_oversampled_label_matching.py \
  /tmp/refined-labels.json
```

For each stored certificate and each perfect-matching layer, the analyzer uses the
chosen layer as the source-edge pool and the opposite layer as the fixed retained
source. It constructs the refined label graph `J_{gamma,epsilon}`, checks the
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

Each pair lists layers zero and one. The important feature is that the graph is
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
edges in these small cases. These sizes are too small for the asymptotic PP3ff
local-lemma inequality, so this is a label-allocation diagnostic rather than a
finite completion certificate.

## Exact PP3ft guarantees

Using the exact bad-label incidence

\[
 \mathcal U=\sum_{A,B}|U_{A,B}|
\]

rather than its divisor-energy upper bound gives the following rigorous edge and
matching lower bounds at `L=12`, `gamma=1/3`, `epsilon=1/6`:

| Side/layer | PP3ft edge lower bound | PP3ft matching lower bound | Actual matching |
|---|---:|---:|---:|
| 8/0 | 40 | 4 | 12 |
| 8/1 | 35 | 3 | 12 |
| 9/0 | 24 | 2 | 12 |
| 9/1 | 4 | 1 | 12 |
| 10/0 | 8 | 1 | 12 |
| 10/1 | 0 | 0 | 12 |

The exact-incidence theorem is still conservative, but it gives nontrivial
certified matchings in five of the six larger stored layers. Replacing
`mathcal U` by the raw divisor energy gives zero in all six cases. This quantifies
the value of compressing duplicate anchor witnesses before applying arithmetic
bounds.

## Divisor-energy check

For every tested layer, the exact sum `mathcal U` is at most the pool-anchor
divisor energy from PP3fe. The inequality is usually loose: one source edge can
have several anchor witnesses for the same bad label pair, while `U_(A,B)` counts
the edge once.

## Interpretation

The finite data support the global-label-oversampling route from PP3eh, PP3ff,
and PP3fu:

1. expose a boundary reservoir substantially larger than the installed macro
   width;
2. construct the fixed-pair and same-edge-anchor refined graph on that reservoir;
3. compress duplicate anchor witnesses into the exact bad-label incidence;
4. select only a large matching of labels;
5. apply PP3ff and then the weighted global endpoint PP3fk.

The remaining asymptotic issue is proving, for almost every large macro pool,
that the normalized boundary-shadow and exact bad-label losses leave a matching
of size `Theta(sqrt(R))` with constant-density edge domains.