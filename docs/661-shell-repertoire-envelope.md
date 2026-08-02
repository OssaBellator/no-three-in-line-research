# Shell repertoire envelope

The heterogeneous shell law permits varying period burdens, but variation alone
does not create savings. This chapter gives the exact optimization envelope for a
finite macro repertoire, including quotas, compatibility constraints, and robust
worst-case scheduling.

For macro type or transition `j`, write

```text
b_j = 6*delta_j + c_j,
```

where `delta_j` is per-use overhead and `c_j` is recurring collateral.

## PP3dat — Static repertoire and quota envelope

For a `K`-period schedule with type counts `n_j`, recurring burden is
`sum_j n_j b_j`. Without frequency constraints, its minimum is exactly

```text
K*min_j b_j.
```

Thus unconstrained mixing cannot beat repeating the least-burden type.

If type `j` must occur at least `ell_j` times and `L=sum_j ell_j<=K`, the sharp
minimum is

```text
sum_j ell_j b_j + (K-L)*min_j b_j.
```

Including one-time setup `S`, strict improvement is equivalent to this burden
being less than `3K-S`.

## PP3dau — Compatibility graph and positive-cycle criterion

When macro compatibility is represented by a finite directed transition graph,
assign edge saving

```text
w(e)=3-b(e).
```

Starting from the designated initial state, every fixed setup is amortizable if
and only if a reachable directed cycle has positive total saving, equivalently if
a reachable cycle has mean burden below three.

### Proof

A positive cycle may be repeated until its accumulated saving exceeds any fixed
setup. Conversely, if every reachable cycle has nonpositive saving, removing a
cycle from a walk never decreases total saving. Every walk then has a simple
representative with at least as much saving, and the finite graph supplies a
uniform finite upper bound. ∎

The best asymptotic saving rate is the maximum reachable cycle mean of `w`, or
three minus the minimum reachable cycle-mean burden. If an entry path has saving
`A` and reaches a cycle of gain `G>0`, the least number of complete repetitions
needed to beat setup `S` is

```text
max(0, floor((S-A)/G)+1).
```

Entry paths and individual cycle edges may lose controls; only the positive total
cycle gain controls indefinite amortization.

## PP3dav — Robustness against arbitrary schedules

For an unconstrained repertoire let `b_max=max_j b_j`. Every `K`-period schedule
improves against setup `S` exactly when

```text
K*(3-b_max) > S.
```

Consequently some finite length is uniformly improving for every schedule if and
only if `b_max<3`. In that case the least robust length is

```text
floor(S/(3-b_max)) + 1.
```

Exact checkers:

- `scripts/check_shell_repertoire_envelope.py`
- `scripts/check_shell_repertoire_cycle_mean.py`

## Evidence boundary

No geometric `(1,1,1)` macro repertoire has supplied certified transition burdens,
compatibility edges, mandatory frequencies, or a reachable sub-three mean cycle.
These are exact cost and scheduling interfaces, not source realizations.
