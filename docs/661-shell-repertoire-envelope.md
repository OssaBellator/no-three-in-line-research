# Shell repertoire envelope

The heterogeneous shell law permits varying period burdens, but variation alone
does not create savings.  This chapter gives the exact optimization envelope for
a finite repertoire of geometric macro types.

For macro type `j`, write

```text
b_j = 6*delta_j + c_j,
```

where `delta_j` is its per-use overhead and `c_j` is its recurring collateral.

## PP3dat — Unconstrained mixing cannot beat the best type

For any `K`-period schedule with counts `n_j` satisfying `sum_j n_j=K`, recurring
burden is

```text
sum_j n_j b_j.
```

Without frequency constraints, the minimum is exactly

```text
K * min_j b_j.
```

Hence with one-time setup `S`, some unconstrained `K`-period schedule improves the
baseline exactly when

```text
K*(3-min_j b_j) > S.
```

Mixing macro types never beats repeating the least-burden type.  Heterogeneous
scheduling matters only when geometry or compatibility imposes additional
constraints.

## PP3dau — Exact lower-quota envelope

Suppose type `j` must occur at least `ell_j` times in a `K`-period cycle, with
`L=sum_j ell_j <= K`.  The minimum possible recurring burden is

```text
sum_j ell_j b_j + (K-L)*min_j b_j.
```

The exact strict-improvement condition, including setup `S`, is therefore

```text
3K - sum_j ell_j b_j - (K-L)*min_j b_j > S.
```

This formula is sharp: assign every period beyond the mandatory quotas to a
minimum-burden type.

## PP3dav — Robustness against arbitrary repertoire schedules

Let `b_max=max_j b_j`.  Every `K`-period schedule from the repertoire improves
against setup `S` exactly when

```text
K*(3-b_max) > S.
```

Consequently some finite length is uniformly improving for every schedule if and
only if `b_max<3`.  In that case the least robust length is

```text
floor(S/(3-b_max)) + 1.
```

The checker `scripts/check_shell_repertoire_envelope.py` verifies the formulas by
exact arithmetic and brute count-vector enumeration.

## Evidence boundary

No geometric `(1,1,1)` macro repertoire has yet supplied certified values of
`b_j`, mandatory frequencies, or compatibility constraints.  The result is an
exact cost envelope, not a source realization.
