# Robust connector tours with three uncertainty states

This chapter extends the two-state connector analysis in
`docs/699-robust-shell-connector-tours.md` to three uncertainty states. The macro
graph still has three positive components and therefore two directed Hamiltonian
tours, but every directed connector edge now carries a three-coordinate burden
vector.

## PP3dfv — Exact three-state robust-tour census

Let every edge/state burden lie in `{1,2}`. There are six directed edges and three
uncertainty states, hence

```text
2^(6*3) = 262,144
```

directed burden tables.

For each table, compare the statewise lower bound

```text
max_u min_T L_u(T)
```

with the true robust tour objective

```text
min_T max_u L_u(T).
```

The exact robust-gap histogram is

```text
gap 0: 199,456
gap 1:  57,492
gap 2:   5,112
gap 3:      84.
```

Thus independently minimizing the tour in each uncertainty state is incompatible
with one common executable tour in 62,688 cases. The burden pair

```text
(3,3,6), (3,6,3)
```

has statewise lower bound three but robust optimum six, attaining the maximum gap.

## PP3dfw — Edgewise-worst scalarization loses two units

Replacing each connector burden vector by its coordinatewise maximum before
optimizing gives the edgewise-worst scalar charge. Its exact overcharge histogram
relative to the vector-aware robust optimum is

```text
overcharge 0: 137,740
overcharge 1: 120,324
overcharge 2:   4,080.
```

The scalarization is therefore strict in 124,404 tables and can lose two full
burden units. Connector paths must retain their complete uncertainty vectors; a
single worst-edge weight is not an exact substitute.

## PP3dfx — Joint repetition optimization remains essential

For gain vector `G`, setup `S`, and tour burden vector `L(T)`, the exact required
bundle count is

```text
max_u ( floor((S+L_u(T))/G_u) + 1 ).
```

The audit checks every burden table, every gain vector in `{1,2,3}^3`, and every
setup in `{0,1,2,3}`, totaling

```text
262,144 * 27 * 4 = 28,311,552
```

weighted repetition comparisons. In 1,601,388 cases, every tour minimizing the
worst raw burden is disjoint from the repetition-optimal tour set.

For example, with burdens

```text
(3,3,4), (3,5,3),
```

gains `(1,2,1)`, and zero setup, the raw robust tour is the first one, but the
required repetition counts are `(5,4)`, so the second tour is optimal after gain
scaling.

The exact audit is `scripts/check_shell_three_state_connector_tours_705.py`.

## Evidence boundary

This is an exact finite uncertainty interface. No current coordinate macro graph
supplies three-state connector-path burden vectors together with positive robust
bundle gains. The shell row remains unpromoted and the all-`n` theorem remains
open.
