# Interval shell cycle robustness

`docs/661` gives exact scheduling criteria when every macro-transition burden is
known. A coordinate construction may initially certify only an interval of
possible repair and collateral costs. This chapter gives the exact finite-state
criterion under independent edge intervals.

For each directed transition edge `e`, let its burden satisfy

```text
lower_e <= b(e) <= upper_e,
```

and write saving `w(e)=3-b(e)`.

## PP3dbl — Possible and robust positive cycles

From the designated initial state, some admissible burden realization amortizes
every fixed setup exactly when a reachable directed cycle `C` satisfies

```text
sum_{e in C} (3-lower_e) > 0.
```

Every admissible realization is guaranteed to amortize every fixed setup exactly
when a reachable directed cycle `C` satisfies

```text
sum_{e in C} (3-upper_e) > 0.
```

Equivalently, possible amortization requires a reachable cycle whose lower-burden
mean is below three, while robust amortization requires a reachable cycle whose
upper-burden mean is below three.

## PP3dbm — Exact three-regime classification

The interval transition graph falls into exactly one of three regimes:

1. **robust:** some reachable cycle has positive worst-case saving;
2. **possible only:** no cycle is worst-case positive, but some cycle is
   best-case positive;
3. **impossible:** no reachable cycle is positive even at lower burdens.

Because cycle gain is affine in the edge burdens, the best and worst values on an
interval box occur at interval endpoints. The checker verifies all corner
realizations in representative robust and possible-only graphs.

For the robust example with edges

```text
0->1: [4,5], 1->2: [1,2], 2->1: [2,2],
```

the unique reachable cycle has best-case gain three and worst-case gain two.

## PP3dbn — Worst-case entry and setup bound

Suppose a path reaches a robust cycle with guaranteed entry saving `A`, and the
cycle has guaranteed gain `G>0`. The least number of complete cycle repetitions
that beats setup `S` in every admissible realization is

```text
max(0, floor((S-A)/G)+1).
```

In the checker example, worst-case entry saving is `-2`, robust cycle gain is `2`,
and setup is `7`; exactly five repetitions are necessary and sufficient.

`scripts/check_shell_interval_cycle_robustness.py` enumerates reachable simple
cycles, checks lower- and upper-endpoint gains, audits all interval-box corners in
representative examples, and verifies the exact repetition formula.

## Evidence boundary

No coordinate-level `(1,1,1)` macro repertoire currently supplies certified
transition burden intervals and compatibility edges with a robust positive cycle.
This theorem identifies the exact interval data required for promotion and
separates optimistic from worst-case scheduling claims.
