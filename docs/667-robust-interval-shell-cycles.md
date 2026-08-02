# Robust interval shell cycles

`docs/661` gives the exact positive-cycle criterion when every macro-transition
burden is known. Coordinate geometry may initially provide only certified burden
intervals. This chapter gives the exact robust and possible cycle criteria under
independent interval uncertainty.

For each directed transition `e`, let its burden satisfy

```text
lower_e <= b(e) <= upper_e,
```

and let saving be `w(e)=3-b(e)`.

## PP3dbl — Possible positive-cycle criterion

There exists some admissible burden realization that amortizes every fixed setup
if and only if a reachable directed cycle `C` satisfies

```text
sum_{e in C} (3-lower_e) > 0.
```

Equivalently, some reachable cycle has best-case mean burden below three.

### Proof

The best possible total saving of a fixed cycle is obtained by assigning every
edge its lower burden. If no reachable cycle is positive under those simultaneous
lower assignments, no other admissible realization can create a positive cycle.
Conversely, a positive lower-burden cycle is itself an admissible witness. ∎

## PP3dbm — Robust positive-cycle criterion

Every admissible burden realization amortizes every fixed setup if and only if a
reachable directed cycle `C` satisfies

```text
sum_{e in C} (3-upper_e) > 0.
```

Equivalently, some reachable cycle has worst-case mean burden below three.

### Proof

Such a cycle remains positive after every independent choice inside the intervals.
Conversely, if no cycle is positive at simultaneous upper burdens, that admissible
realization has no positive reachable cycle, so robust amortization fails. ∎

Thus the interval problem has three exact regimes:

1. **robust:** a worst-case positive cycle exists;
2. **possible but not robust:** a best-case positive cycle exists but no worst-case
   positive cycle exists;
3. **impossible:** even the simultaneous lower-burden graph has no positive cycle.

## PP3dbn — Worst-case setup repetition bound

Suppose an entry path has worst-case saving `A_minus`, and a reachable cycle has
worst-case gain `G_minus>0`. For setup `S`, the least number of complete cycle
repetitions guaranteed to give strict improvement is

```text
max(0, floor((S-A_minus)/G_minus)+1).
```

For the checker example, the entry burden interval gives `A_minus=-2`, the cycle
has worst-case gain two, and setup seven requires exactly five repetitions.

## Verification

`scripts/check_shell_interval_cycle_robustness.py` enumerates simple reachable
cycles, checks all interval corners of robust and possible-only examples, verifies
an impossible example, and checks the exact repetition formula with rational
arithmetic.

## Evidence boundary

This is an exact uncertainty interface. No coordinate-level `(1,1,1)` macro
repertoire currently supplies certified edge intervals and compatibility data
with a reachable worst-case mean burden below three.
