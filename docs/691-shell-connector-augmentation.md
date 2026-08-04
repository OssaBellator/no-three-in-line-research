# Shell connector augmentation

`docs/685` proves that a positive rational circulation with connected support
clears directly to one Eulerian closed walk, while disconnected positive support
requires connectors. This chapter gives the exact finite optimization problem for
those connectors.

## PP3def — Minimum balanced connected augmentation

Suppose a positive shell circulation has connected support components
`C_1,...,C_t`. Let `ell_ij>=0` be the certified worst-case loss of a directed
connector from component `i` to component `j`.

A connector multiset is described by nonnegative integers `y_ij`. It produces one
Eulerian tour through all components exactly when

```text
sum_j y_ij = sum_j y_ji                 for every i,
sum_{i in S, j not in S} y_ij >= 1      for every nonempty proper S.
```

The first constraints enforce balance. The cut constraints enforce weak
connectivity; for a balanced directed multigraph this is equivalent to strong
connectivity on the active components and hence to the existence of one Euler
tour.

Therefore the exact minimum connector loss is the integer program

```text
L* = min sum_{i!=j} ell_ij y_ij
```

subject to the balance, cut, and nonnegativity constraints above.

## PP3deg — Directed metric closure and tour reduction

Replace `ell_ij` by the directed shortest-path distance `d_ij` in the connector
macro graph. Any connected balanced augmentation gives a closed walk visiting all
components. Shortcut repeated visits in the directed metric closure; the cost does
not increase. Conversely, expand each metric edge of a Hamiltonian tour into its
shortest connector path.

Hence

```text
L* = minimum directed Hamiltonian-tour cost in the metric closure.
```

The metric closure is essential: a cheapest Eulerian connector may traverse an
intermediate component on the way between two nominal tour vertices and can be
strictly cheaper than a Hamiltonian cycle using only direct connector edges.

## PP3deh — Exact setup repayment after optimal connection

Let one repetition of all positive disconnected component tours have total robust
gain `G>0`. Charge the optimal connector loss `L*` once and let the setup burden be
`S>=0`.

The least number of bundle repetitions yielding saving strictly greater than setup
is

```text
floor((S+L*)/G)+1.
```

Indeed, `r` repetitions have net saving `rG-L*`, so the condition is exactly
`rG-L*>S`.

`scripts/check_shell_connector_augmentation.py` exhausts all 729 complete directed
three-component connector cost matrices with arc costs in `{1,2,3}`. For every
matrix it compares the minimum balanced connected integer augmentation with the
minimum Hamiltonian tour in the directed metric closure; the two values agree in
all cases.

Metric closure is strictly better than a direct-edge Hamiltonian tour in three
cases, by one unit. In a recorded example, the direct tour costs five while the
optimal balanced connector multiset costs four. The checker also verifies the
repayment example

```text
G=3, L*=4, S=7  =>  least repetitions = 4.
```

## Evidence boundary

This is an exact connector optimization interface. It still requires a coordinate
macro graph whose positive components, directed connectors, and robust connector
losses are geometrically certified. No shell row is promoted without that data.
