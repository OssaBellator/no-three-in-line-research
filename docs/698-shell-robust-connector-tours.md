# Robust connector tours under burden uncertainty

`docs/691` reduces scalar connector augmentation to a minimum directed tour after
metric closure. This chapter keeps the complete burden vector over uncertainty
states and derives the exact repayment objective. Scalarizing too early can select
the wrong connector tour.

## PP3dfa — Robust connector loss is a min-max tour problem

Let `U` be the finite uncertainty-state set. For each directed connector edge `e`
and state `u`, let

```text
b_e(u) >= 0
```

be its burden. A connector tour `T` has statewise burden vector

```text
L_u(T) = sum_{e in T} b_e(u).
```

The exact robust connector-loss objective is

```text
min_T max_{u in U} L_u(T).
```

This is generally larger than the statewise lower bound

```text
max_u min_T L_u(T),
```

because different uncertainty states may prefer incompatible tours. It is also no
larger than charging every edge by its separate worst state,

```text
min_T sum_{e in T} max_u b_e(u),
```

which may combine edgewise maxima that cannot occur in one common state.

For three components, two uncertainty states, and edge burdens in `{1,2}`, the
checker exhausts all

```text
2^12 = 4,096
```

directed burden tables. The statewise lower bound is strict in 644 tables. The
edgewise-worst charge is strict in 1,116 tables, always by one in this census.

## PP3dfb — Exact statewise repayment formula

Suppose one disconnected positive bundle has gain `G_u>0` in uncertainty state
`u`, the setup charge is `S`, and connector tour `T` has burden `L_u(T)`. After
`r` repetitions, strict positivity beyond setup requires

```text
r G_u - L_u(T) > S
```

for every state. Therefore the least repetitions for a fixed tour are exactly

```text
R(T) = max_u ( floor((S+L_u(T))/G_u) + 1 ).
```

The correct connector-selection objective is consequently

```text
min_T max_u ( floor((S+L_u(T))/G_u) + 1 ).
```

The checker verifies this formula by direct repetition search for every one of the
4,096 burden tables, all nine gain vectors in `{1,2,3}^2`, and setup values
`0,1,2,3`, totaling

```text
4,096 * 9 * 4 = 147,456
```

exact repayment checks.

## PP3dfc — Minimum robust burden need not minimize repetitions

When the gains `G_u` differ between states, minimizing

```text
max_u L_u(T)
```

need not minimize `R(T)`. In 5,640 of the 147,456 repayment instances, the set of
robust-loss-optimal tours is disjoint from the set of repetition-optimal tours.

A smallest explicit example has the two tour burden vectors

```text
(3,5) and (4,3),
```

with gain vector `(1,2)` and setup zero. The first tour has larger worst burden,
but requires only four repetitions, while the second requires five. Thus the gain
vector must remain coupled to the connector burden vector until the final integer
repayment optimization.

The exact checker is `scripts/check_shell_robust_connector_tours.py`.

## Evidence boundary

This is an exact finite robust-execution interface. A geometric application must
still supply a coordinate macro graph, certified connector-path burden vectors,
and positive bundle-gain vectors in every uncertainty state. No such coordinate
macro graph is presently known. The theorem is not an all-length construction,
and the all-`n` theorem remains open.
