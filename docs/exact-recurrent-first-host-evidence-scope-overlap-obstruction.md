# First-host evidence-scope overlap obstruction

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact audit of scoped evidence obligations versus unsafe de-duplication by repeated field name. No sharing theorem, physical certificate, route, recurrent row, or Lyapunov proof is imported.

## Why this audit is necessary

The hybrid source-certificate antichain counts evidence **slots** per certificate instance. Several certificate contracts reuse field labels such as `realization_status`. That does not mean one populated value automatically satisfies every occurrence of that field.

For example, these are different obligations even when their labels match:

```text
state:00 / realization_status
state:01 / realization_status
edge:00->10 / realization_status
```

A source may reuse one theorem reference in several slots only after proving that the theorem is uniform over the exact certificate instances and preserves every local obligation.

## Contract field sets

```text
state impossibility                         6 slots
uniform action family                      7 slots

individual edge route:
  physical exclusion                       5 slots
  decorated outer reset                    8 slots
  finite unrestorable capacity             9 slots
  terminal or improving output            10 slots
  bounded strict potential                 11 slots
```

Across the state, family, and edge contract classes, the only repeated cross-class field name is

```text
realization_status
```

The other apparent overlaps arise from repeating an entire same-class schema for several distinct states, families, or directed edges.

## Exact antichain audit

The checker reconstructs the complete hybrid antichains:

```text
selected-label patterns                    51
menu-state patterns                       100
route classes audited                       5
```

For each route class and each minimal pattern it records:

```text
scoped_slots
lexical_union_fields
unsafe_lexical_savings
```

`scoped_slots` counts one obligation for every certificate-instance field. `lexical_union_fields` collapses identical strings and is retained only to quantify how badly an unscoped audit can undercount.

Every one of the 51 label patterns and 100 menu patterns contains at least one repeated field name.

## Physical-exclusion extremum

Under physical exclusion, the safe evidence floors remain

```text
label scalar                               11 scoped slots
menu scalar                                12 scoped slots
```

The eleven-slot label patterns are the four state-plus-edge pairs from the hybrid antichain. Each pair has ten distinct field-name strings because both certificates contain `realization_status`, but it still has eleven scoped obligations.

The strongest lexical-collapse failure comes from pure edge patterns:

```text
three physical-exclusion edge certificates
  scoped slots                             15
  distinct field-name strings               5
  unsafe apparent saving                   10

four physical-exclusion edge certificates
  scoped slots                             20
  distinct field-name strings               5
  unsafe apparent saving                   15
```

Thus a five-name lexical union is not a five-obligation recurrence certificate.

## Other route classes

For every non-exclusion route, the safe label and menu floors remain twelve slots. The maximum unsafe savings from field-name collapse are:

```text
route                              label    menu
physical exclusion                   10      15
decorated outer reset                16      24
finite unrestorable capacity         18      27
terminal or improving output         20      30
bounded strict potential             22      33
```

The large numbers occur when several exact edge certificates repeat the same route schema. They do not establish a shared route theorem.

## Sharing theorem gate

Any proposed quotient of certificate-instance fields must populate:

```text
certificate_instance_domain_ref
field_equivalence_map
uniformity_theorem_ref
scope_preservation_ref
local_obligation_preservation_ref
realization_status
```

The theorem must state exactly which certificate instances are covered, which slots share one source fact, and why no state-, family-, or edge-local theorem is lost.

Current state:

```text
accepted sharing theorems                    0
populated sharing fields                     0
```

A common document reference is not by itself a sharing theorem. Likewise, identical field labels do not identify the mathematical statements occupying those slots.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_evidence_scope_overlap_obstruction.py \
  --check data/exact_recurrent_first_host_evidence_scope_overlap_obstruction.json \
  --self-test
```

The checker reconstructs all 151 minimal patterns for each of five route classes, validates the scoped/lexical distributions and registry digests, and rejects eighteen deliberate corruptions.

Physical occurrence coverage, legal transitions, persistent owner identity, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.
