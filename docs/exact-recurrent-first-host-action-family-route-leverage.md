# First-host action-family route leverage

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional classification of uniform source certificates for the four directed action families. It does not prove that any family is physically legal, impossible, capacity-bounded, or otherwise route-closed.

## Directed action families

The restoration square has four natural two-edge families:

```text
restore_02: 00->10, 01->11
delete_02:  10->00, 11->01
restore_20: 00->01, 10->11
delete_20:  01->00, 11->10.
```

A family is source-closed only when one uniform physical theorem closes both context edges through accepted closure routes. Evidence for one member cannot be copied to the other member merely because the changed cell and action agree.

Examples of admissible family-level proofs include:

```text
both edges are physically impossible;
both consume one source-defined finite capacity coordinate;
both strictly decrease the same bounded source potential;
both terminate or improve through one proved operation schema;
both traverse source-defined decorated outer edges with repetition control.
```

Each edge must still satisfy the underlying closure-route source gate.

## Exact two-family criterion

There are four directed families and therefore sixteen possible family subsets. A family subset contains a label-scalar or menu-scalar residual cover exactly at the minimum level when it contains:

```text
one directed family for bit 02
and
one directed family for bit 20.
```

The four minimum complete sets are

```text
restore_02 + restore_20
restore_02 + delete_20
delete_02  + restore_20
delete_02  + delete_20.
```

Each union consists of four directed edges and contains exactly one label-scalar cover and one menu-scalar cover.

Thus both monotone action choices are valid:

```text
all restore directions
all delete directions,
```

but they are not the only choices. The two mixed-action orientations are also scalar-compatible menu covers.

## Same-bit failure

Closing both action directions for only one changed cell does not suffice:

```text
restore_02 + delete_02
restore_20 + delete_20.
```

Each set covers both directions of two parallel square edges while leaving both reversal pairs of the other bit untouched. Consequently neither contains a label nor a menu cover.

Exact remaining deficits are:

```text
family evidence                 extra label edges   extra menu edges
restore_02 only                 1                   2
delete_02 only                  1                   2
restore_20 only                 2                   2
delete_20 only                  2                   2
both directions of bit 02       1                   2
both directions of bit 20       2                   2.
```

## Complete family census

```text
directed action families                    4
edges in each family                        2
family subsets                             16
two-family subsets                          6
two-family label shortcuts                  4
two-family menu shortcuts                   4
minimum families for label closure          2
minimum families for menu closure           2
minimum complete family sets                4.
```

Adding any third family preserves closure and increases the number of contained covers. All four families contain all six label covers and all fourteen menu covers.

## Physical ingestion consequence

This theorem reduces a possible source-facing proof from four unrelated edge certificates to two uniform family certificates. It does not weaken the evidence required within a family.

For example, a theorem stating “restoration of `02` is bounded” must prove the same exact route contract for both

```text
00->10
01->11,
```

including their physical occurrence, owner, endpoint, operation, trace and route-specific fields. A statement about only `00->10` is an edge certificate, not a family certificate.

The current transition-domain audit supplies no physical edge record, so the current source-closed family set is empty.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_action_family_route_leverage.py \
  --check data/exact_recurrent_first_host_action_family_route_leverage.json
```

The checker reconstructs the six label covers and fourteen menu covers, enumerates all sixteen family subsets, proves the four minimum cross-bit shortcuts and rejects fifteen deliberate corruptions.

Physical occurrence coverage, transition legality, persistent owner identity, route evidence, child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
