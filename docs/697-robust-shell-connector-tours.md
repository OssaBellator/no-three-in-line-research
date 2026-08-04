# Robust shell connector tours

`docs/691` solves scalar connector augmentation by directed metric closure and a
minimum tour. In the robust shell problem, however, connector burdens depend on
the uncertainty vertex. This chapter records the correct vector-valued tour and
repayment objectives.

## PP3dex — Minimax vector connector tour

Let `U` be the finite set of burden vertices. Every directed connector path `P`
between positive-support components has a burden vector

```text
L(P) = (L_u(P))_{u in U}.
```

Discard every path vector dominated coordinatewise by another path with the same
endpoints. A connector tour `T` chooses one retained path at every tour step and
has total vector

```text
L(T) = sum_{P in T} L(P).
```

The exact robust one-tour connector loss is

```text
L_rob = min_T max_{u in U} L_u(T).
```

Two tempting scalarizations are generally wrong:

1. `max_u min_T L_u(T)` is only a lower bound, because the statewise optimal tours
   may be different;
2. replacing every edge vector by its coordinatewise maximum and then summing can
   overcharge, because different edge maxima may occur at incompatible uncertainty
   vertices.

Thus vector summation must precede the worst-state maximum.

## PP3dey — Exact three-component uncertainty census

For three support components and two uncertainty vertices, assign each of the six
directed connector edges a burden vector in `{1,2}^2`. There are

```text
4^6 = 4,096
```

complete burden tables and two directed Hamiltonian tours.

`scripts/check_shell_robust_connector_tours.py` exhausts all tables. The gap between
the true minimax optimum and the statewise lower bound has histogram

```text
0:3452, 1:582, 2:60, 3:2.
```

Hence statewise optimal tours are incompatible in 644 tables. A smallest example
has the two tour vectors

```text
(3,4) and (4,3).
```

Each uncertainty vertex separately admits loss three, but every single tour has
worst loss four.

The edgewise-worst scalarization agrees in 2,980 tables and overcharges by one in
1,116 tables.

## PP3dez — Joint tour and repetition optimization

Suppose one disconnected positive bundle has gain vector

```text
G=(G_u)_{u in U},  G_u>0,
```

and setup charge `S`. For a fixed connector tour `T`, strict positivity at every
uncertainty vertex requires

```text
r G_u - L_u(T) > S
```

for every `u`. Therefore the exact repetition count for `T` is

```text
r(T) = max_u ( floor((S+L_u(T))/G_u) + 1 ),
```

and the correct optimization is

```text
min_T r(T).
```

This need not select a tour minimizing `max_u L_u(T)`, because burden at a
high-gain uncertainty vertex is cheaper to repay.

The checker tests all 4,096 burden tables, all gain vectors in `{1,2,3}^2`, and
setups `S=0,1,2,3`:

```text
4,096 * 9 * 4 = 147,456
```

formula comparisons with direct repetition search. All agree. In 5,640 cases,
every robust-loss-minimizing tour is disjoint from the repetition-minimizing tour
set.

For example, tour burdens `(3,5)` and `(4,3)` have worst losses five and four,
respectively. With gains `(1,2)` and setup zero, they require four and five
repetitions, so the larger worst-loss tour repays first.

## Evidence boundary

This is the exact finite robust connector interface. It still requires a coordinate
macro graph supplying positive-support components, Pareto connector-path burden
vectors, and positive bundle-gain vectors. No such coordinate macro graph is
constructed here.

The all-`n` theorem remains open, and the next theorem identifier is `PP3dfa`.
