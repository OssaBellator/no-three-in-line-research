# Exact side-four residual lineage projection

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact coordinate-lineage join proved; this chapter audits the raw
lineage layer only.

## Result

The eleven states in `data/exact_recurrent_side_four_kernel.json` join
bijectively, by deletion set, to eleven stable host identifiers in the
composite-modulus raw-fibre lineage manifest.

The three local blocker classes likewise join to stable upstream identifiers:

```text
{02,20} -> b4-8a44614df456
{02,31} -> b4-557232b8e56a
{13,31} -> b4-4b72675a7313
```

For every residual host, the checker verifies the deletion set, surviving
response spectrum, blocker-alternative dispatch, contained blocker identifiers,
and uniqueness of the join.

## Raw-layer gap certificate

The raw lineage file certifies coordinate host/response linkage but does not
itself contain background records, physical deletion causes, legal operation
families or recurrent child rows. Its owner/fate/collision/line/interface/CRT
slots are also absent at this layer.

Across the eleven residual hosts, the raw-layer null inventory is

```text
physical deletion-cause assignments                 32
background records                                  11
raw owner/fate/collision/line/interface/CRT slots    66
legal operation families                            11
recurrent child rows                                11
```

The first count is the sum of deletion-set sizes. The other counts follow from
the declared schema per host.

## Subsequent normalized layer

A separate upstream selected-response manifest supplies normalized values for
all six owner/fate/collision/line/interface/CRT coordinates. Those values are
integrated and checked in
`docs/exact-recurrent-side-four-selected-provenance.md`.

Therefore the 66 slots above must not be described as globally absent after the
selected-response layer is included. They are absent from the raw lineage file,
then populated by normalized classes. Those normalized classes still do not
identify physical owners, backgrounds, deletion causes, collision ancestry or
legal repairs.

## Why this matters

The local blocker theorem identifies which cells would have to be reopened to
expose a triple-free response. The raw lineage join gives stable host and blocker
addresses. Neither fact says why a cell is unavailable, whether it can legally
be reopened, what collateral is created, or whether the same host can recur.

The checker prevents a coordinate host from being silently assigned an invented
physical background or owner.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_side_four_lineage_projection.py \
  --kernel data/exact_recurrent_side_four_kernel.json \
  --projection data/exact_recurrent_side_four_lineage_projection.json
```

The audit rejects nine corruption classes. All global proof and strict-Lyapunov
flags remain zero.

## Next theorem target

For upstream host `s4-75b04c45c1c8eac2`, deletion set `{02,20}`, combine the
stable raw lineage address with the exact normalized selector record, then
enumerate every physically realizable background and deletion-cause fibre. The
first acceptable output is a complete legal transition row or a source-backed
witness that the present repository data do not determine one.
