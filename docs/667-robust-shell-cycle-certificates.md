# Robust shell cycle certificates

The shell repertoire criterion in `docs/661` assumes exact edge burdens. A
coordinate construction will more naturally produce certified burden intervals.
This chapter gives the exact robust, possible, and impossible cycle tests under
independent interval uncertainty.

For a transition edge `e`, suppose

```text
lower(e) <= b(e) <= upper(e),
```

where `b(e)=6*delta(e)+c(e)` is the recurring burden. The saving against the
three-control period margin is `3-b(e)`.

## PP3dbl — Robust common-cycle criterion

A reachable directed cycle `C` is positive-saving for every burden realization in
its intervals exactly when

```text
sum_{e in C} upper(e) < 3|C|.
```

Equivalently, the cycle's worst-case gain

```text
G_min(C) = sum_{e in C}(3-upper(e))
```

is positive. A finite transition graph therefore has a common cycle certificate
that amortizes every fixed setup under all admissible burdens exactly when some
reachable cycle has upper-bound mean burden below three.

## PP3dbm — Possibility, impossibility, and the uncertainty band

Some admissible burden realization makes a reachable cycle positive exactly when
some reachable cycle satisfies

```text
sum_{e in C} lower(e) < 3|C|.
```

Conversely, if every reachable cycle has lower-bound mean burden at least three,
no admissible realization can produce a positive cycle.

Thus interval data divide into three regimes:

1. **robust:** a reachable cycle has upper-bound mean below three;
2. **impossible:** every reachable cycle has lower-bound mean at least three;
3. **unresolved:** lower bounds permit a positive cycle but upper bounds do not
   certify one.

For a nominal cycle of mean burden `beta`, uniform additive edge uncertainty
`epsilon` preserves a strict positive-saving certificate exactly when

```text
beta + epsilon < 3.
```

The sharp uniform tolerance is `3-beta`.

## PP3dbn — Worst-case setup repayment

Suppose an entry path has worst-case saving `A_min`, and a robust cycle has
worst-case gain `G_min>0`. Against fixed setup `S`, the least number of complete
cycle repetitions guaranteed to give strict improvement is

```text
max(0, floor((S-A_min)/G_min)+1).
```

In the checker example, the entry path has worst-case saving `-2`, the two-edge
cycle has burden interval total `[3,4]`, its worst-case gain is `2`, and setup
`7` requires exactly five complete repetitions.

The exact finite-graph and rational-arithmetic audit is
`scripts/check_shell_robust_cycle_certificates.py`.

## Evidence boundary

These are exact robust scheduling interfaces. The repository still lacks a
coordinate-level macro repertoire with certified transition intervals,
compatibility edges, and a reachable cycle whose upper-bound mean burden is below
three.
