# First-host action-family congruence obstruction

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact geometric audit of the four two-edge action families. It proves that common changed cell and action do not by themselves identify one context-free operation row.

## Family members

```text
restore_02: 00->10, 01->11
delete_02:  10->00, 11->01
restore_20: 00->01, 10->11
delete_20:  01->00, 11->10.
```

Each pair holds the changed cell and action fixed while the other restoration bit changes.

## Exact geometry census

```text
action families                                  4
members per family                               2
families homogeneous in changed cell/action      4
families homogeneous in selector-change flag     2
families homogeneous in ordered selected pair    0
families homogeneous in ordered gap pair         0
families homogeneous in ordered face profile     0
families related by exact host automorphism       0
families touching state 11                       4.
```

Only the `02` families are homogeneous in the coarse selector-change flag. Both members of `restore_02` change the selected response toward `2031`, and both members of `delete_02` change it away from `2031`. Their ordered selected-response pairs still differ:

```text
restore_02:
  3012 -> 2031
  3201 -> 2031

delete_02:
  2031 -> 3012
  2031 -> 3201.
```

The `20` families are not even homogeneous in whether the selector changes:

```text
restore_20:
  3012 -> 3201   changing
  2031 -> 2031   neutral

delete_20:
  3201 -> 3012   changing
  2031 -> 2031   neutral.
```

## Gap and face obstruction

State `00` has next gap three. States `01`, `10`, and `11` have next gap one. Every family pairs one edge whose ordered gap profile differs from its partner.

The complete minimizer-face profiles are also distinct:

```text
00: {3012}
01: {3201}
10: {2031,2310}
11: {2031,2310,3201} on 24 backgrounds
    {2031,2301,2310,3201} on 8 backgrounds.
```

Every family contains one edge incident to state `11`, whose complete minimizer face is background-dependent. Therefore family uniformity cannot be inferred from selected identity or the common positive gap.

## Symmetry obstruction

The exact first-host automorphism group preserving target, deletions and response menu is trivial. No nonidentity symmetry identifies the two member edges of any family.

Thus none of the following is a valid shortcut:

```text
same changed cell and action
same selector-change flag
same selected response at one endpoint
same next gap
same local restoration-menu label
ambient row/column/axis symmetry.
```

## Uniform family contract

A family-level proof is accepted only by one of two routes:

1. provide two complete physical edge records, one for each member; or
2. provide a theorem explicitly quantified over both values of the other restoration bit.

The context-parametric theorem requires ten fields:

```text
family_id
edge_refs
shared_theorem_ref
quantified_context_bit
both_context_values_proved
shared_owner_schema_ref
shared_operation_schema_ref
shared_route_schema_ref
child_payment_compatibility_ref
realization_status.
```

The theorem must prove the same closure conclusion in both contexts while retaining any context-dependent selector, face, operation, child-row or payment data needed by the proof.

Current source-uniformity records populated: **0**.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_action_family_congruence_obstruction.py \
  --check data/exact_recurrent_first_host_action_family_congruence_obstruction.json
```

The checker joins the transition-domain, selector-face, exact-symmetry and family-leverage manifests, reconstructs all member descriptors and rejects fifteen deliberate corruptions.

Physical occurrence coverage, transition legality, owner identity, operation/payment congruence, recurrent child rows, strict Lyapunov closure, global termination and `all_n_proved_by_checker` remain zero.
