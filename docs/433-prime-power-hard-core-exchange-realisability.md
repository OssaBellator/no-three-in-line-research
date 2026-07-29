# Sharp background-cardinality realisability of the hard-core exchange chambers

## Scope

CMR2722--CMR2733 reduce all nine nontrivial side-four hard-core selector comparisons to one integer functional

\[
\Delta=d_{32}-d_{12}+3h_{K_-}+h_{K_{30}}+h_{K_{03}}-5h_{K_+}-3,
\]

where

\[
K_-:x-y-1=0,
\quad
K_+:x+y-3=0,
\quad
K_{30}:3x+y-3=0,
\quad
K_{03}:x+3y-9=0.
\]

This chapter determines the least number of outside-grid background points needed to enter the strict `Q4` halfspace.

The executable checker is:

```text
python scripts/check_prime_power_hard_core_exchange_realisability.py
```

This is finite scalar-selector geometry. It does not supply a genuine recurrence fibre or labelled chamber semantics and permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2734--CMR2741

### CMR2734 — exact background evaluation

For a finite background `B` disjoint from the side-four response grid, define

\[
c_z(B)=\#\{\{u,v\}\subseteq B:z,u,v\text{ are collinear}\}.
\]

The gauge-reduced rank-one difference in the hard-core exchange functional is

\[
\boxed{d_{32}-d_{12}=c_{(3,2)}-c_{(3,0)}-c_{(1,2)}+c_{(1,0)}.}
\]

Together with the four exact line occupancies this reconstructs `Delta` directly from `B`.

### CMR2735 — pair terms vanish below two points

If `|B|<=1`, there is no unordered pair of background points. Hence

\[
c_z(B)=0
\]

for every grid point `z`, and therefore

\[
d_{32}-d_{12}=0.
\]

Thus empty and one-point backgrounds are governed only by the weighted line-incidence part and the constant `-3`.

### CMR2736 — all relevant-line intersections are forbidden grid points

Every pairwise intersection among

\[
K_-,K_+,K_{30},K_{03}
\]

is an integer point in the side-four response grid. The distinct intersections are among

\[
(1,0),(2,1),(3,2),(0,3),(3,0).
\]

A legal background point is outside that grid, so it lies on at most one relevant line.

The largest positive single-line coefficient is `3`, attained only on `K_-`. Therefore one legal background point contributes at most three units to the line term.

### CMR2737 — empty background is strict `Q1`

For `B=emptyset`, all cross and line coordinates vanish, so

\[
\boxed{\Delta(\varnothing)=-3.}
\]

Hence the empty background lies strictly in the `Q1` chamber.

### CMR2738 — one-point backgrounds never select `Q4`

By CMR2735 and CMR2736, every legal one-point background satisfies

\[
\Delta(B)\le 3-3=0.
\]

Consequently

\[
\boxed{|B|\le1\Longrightarrow Q_1\text{ is selected}.}
\]

The bound is sharp. The outside-grid point `(-1,-2)` lies on `K_-`, so its one-point background has

\[
\Delta=0.
\]

Lexicographic tie-breaking still selects `Q1`.

### CMR2739 — two points realise strict `Q4`

Take

\[
B_*=\{(-1,-2),(4,3)\}.
\]

Both points lie outside the response grid and both lie on `K_-`. Their connecting line is `K_-`, giving

\[
h_{K_-}=2,
\qquad
h_{K_+}=h_{K_{30}}=h_{K_{03}}=0.
\]

The unique background pair lies on `K_-`, which contains `(3,2)` and `(1,0)` but not `(3,0)` or `(1,2)`. Therefore

\[
d_{32}-d_{12}=1-0-0+1=2.
\]

Hence

\[
\boxed{\Delta(B_*)=2+3\cdot2-3=5>0.}
\]

The deterministic full selector is `Q4`.

### CMR2740 — sharp cardinality threshold and two-sided realisability

CMR2738 gives the lower bound `|B|>=2` for strict `Q4` selection, and CMR2739 attains it. Therefore

\[
\boxed{\min\{|B|:\Delta(B)>0\}=2.}
\]

Both scalar halfspaces are genuinely realizable by legal outside-grid backgrounds:

```text
strict Q1: empty background, Delta=-3
tie Q1: {(-1,-2)}, Delta=0
strict Q4: {(-1,-2),(4,3)}, Delta=5
```

Thus background feasibility alone cannot remove either nontrivial hard-core chamber. Any semantic proof system must handle both selected responses.

### CMR2741 — executable census, seal and honesty boundary

The checker verifies the universal algebra above and also performs two finite stress censuses:

```text
609 one-point backgrounds in [-12,12]^2 outside the response grid
3,486 unordered two-point backgrounds in [-3,6]^2 outside the response grid
```

The one-point census has maximum `Delta=0`. The two-point census contains 37 strict-`Q4` cases, with range

```text
-15 <= Delta <= 5.
```

The sealed manifest digest is

```text
2b4d743fc4e98d39d63c2c7415ec33639692f8bd7b484dcb630ddb2aefd8896c
```

and eight independent corruptions are rejected.

The bounded censuses are regression evidence. The universal one-point impossibility and two-point witness are proved symbolically and do not depend on those boxes.

## Consequence for the T21 frontier

The hard-core selector problem cannot be closed by arguing that genuine background feasibility automatically forces the rank-three-minimal response `Q1`: legal backgrounds already realize strict `Q4` with two points.

The remaining chamber work must therefore prove the actual survivor signatures arising from the genuine recurrence and establish the destroyed-threshold, labelled-child, return, interface and recurrent consequences separately on both sides of the exchange threshold.

The no-three-in-line conjecture remains open.
