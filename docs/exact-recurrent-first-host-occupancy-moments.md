# Exact occupancy moments for the first residual host

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact host-only upper certificate proved. Actual background profile,
parent budget and strictness remain open.

## Host and response family

```text
upstream ID  s4-75b04c45c1c8eac2
deletions    {02,20}
responses    3012, 3210
ambient host standard 4x4 grid
```

For every nonhorizontal, nonvertical real line through at least two grid cells,
let

\[
\tau(\ell)=\max_{q\in\{3012,3210\}}|q\cap\ell|.
\]

The checker enumerates all such lines and both responses exactly.

## Theorem ERL-S4.7 — PROVED

The first host has 54 nonaxis grid lines. Its 35 active line capacities have
census

```text
capacity 1: 31 lines
capacity 2:  2 lines
capacity 3:  1 line
capacity 4:  1 line
```

The higher-capacity lines are

```text
(1,-1,-1)  capacity 3   x-y-1=0
(1, 1,-3)  capacity 4   x+y-3=0
(1, 3,-9)  capacity 2
(3, 1,-3)  capacity 2
```

The exact occupancy moments are

```text
M1=sum tau                  =42
M2=sum C(tau,2)             =11
M3=sum C(tau,3)             = 5
```

## Triple-free-background certificate

When every relevant background line has height at most `H`, the installed moment
bound is

\[
\mathcal C_G(B)
\le \binom H2M_1+HM_2+M_3.
\]

A triple-free background has `H<=2`. Therefore this host has the exact
deterministic upper certificate

\[
E_2=M_1+2M_2+M_3=42+22+5=69.
\]

This is a valid host-level upper bound for the stated background-height class.
It is much larger than the intrinsic selected energy `1`, illustrating why the
selector-only record cannot be substituted for the complete coupled row.

## Why this is not yet strict

The moment certificate maximizes response occupancy separately on each line.
The maxima need not occur in one response, so the value `69` is an upper
certificate rather than an exact score for a specific background and response.

Strict descent additionally requires a destroyed-load or parent-budget value
strictly exceeding the applicable complete weighted row. Neither value is
populated for this host. Consequently this chapter does not prove a legal repair,
a strict Lyapunov row or recurrent subcriticality.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_occupancy_moments.py \
  --manifest data/exact_recurrent_first_host_occupancy_moments.json
```

The checker reconstructs the 54-line universe, all 35 active capacities, the
three moments and the `H=2` certificate, then rejects twelve corruption classes.
All exact-background, parent-budget, strictness and all-`n` flags remain zero.

## Next numerical target

Populate either:

1. the exact line-height superlevel profile for every physical background fibre,
   which evaluates the sharper height-layer identity; or
2. a proved parent budget greater than `69`, which would make this coarse
   triple-free-background certificate strict for the first host.

Absent one of these, the occupancy moments narrow the row but do not close it.
