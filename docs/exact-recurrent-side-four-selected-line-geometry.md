# Exact selected-line geometry for the side-four residual kernel

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact coordinate-line support proved; physical ownership and legal
repair remain open.

## Theorem ERL-S4.4 — PROVED

Every canonical selected response on the eleven residual hosts has all of its
collinear triples supported on a single affine line.

There are exactly two selected-line classes.

### Class `3012`

```text
response points  (0,3), (1,0), (2,1), (3,2)
selected triples {(1,0),(2,1),(3,2)}
line             x-y-1=0
primitive key    (1,-1,-1)
energy           1
host count       9
```

### Class `3210`

```text
response points  (0,3), (1,2), (2,1), (3,0)
selected triples all four 3-subsets
line             x+y-3=0
primitive key    (1,1,-3)
energy           4
host count       2
```

Thus all eleven residual hosts are single-line supported at the selected-response
level. The total selected triple incidence count is

```text
9*1 + 2*4 = 17.
```

## Consequence for the first host

For upstream host `s4-75b04c45c1c8eac2` with deletion trace `{02,20}`, the
canonical response is `3012`. Its unique bad triple is

```text
(1,0), (2,1), (3,2)
```

on the exact line `x-y-1=0`.

Any physical repair row for this host must therefore do at least one of the
following:

1. destroy or reroute that exact line occurrence;
2. legally reopen `02`, exposing zero-energy responses `2031` and `2310`;
3. legally reopen `20`, exposing zero-energy response `3201`;
4. move to another labelled state while accounting for all collateral.

There is no second selected bad line hidden inside the local host.

## Scope boundary

The coordinate line signature is exact, but the repository has not yet attached
its physical owner, background incidences, protected-line status, collision
ancestry or legal operation bank. A background point can create additional line
interactions not represented by the four response points alone.

Therefore this theorem narrows the recurrent state but does not prove that the
selected line can be removed, paid, or made strictly subcritical.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_side_four_selected_line_geometry.py \
  --selected-projection \
    data/exact_recurrent_side_four_selected_provenance_projection.json \
  --geometry data/exact_recurrent_side_four_selected_line_geometry.json
```

The checker rebuilds response points, enumerates all response triples, tests
integer collinearity, normalizes primitive line equations, verifies the
host-class join and rejects twelve corruption classes.

All physical-owner, legal-operation, recurrent-row, Lyapunov and all-`n` flags
remain zero.
