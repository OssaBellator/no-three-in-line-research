# First-host selector-face source import gate

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** reject-by-default import gate for replacing the absent restored-menu scheduler tie-break with source-backed minimizer-face congruence. It compiles the exact proof interfaces but imports no physical theorem.

## Required physical statement

For every response pair used by the face-congruence worklist, the source must establish on one physical occurrence domain and legal menu state:

```text
common persistent owner
congruent legal operation
congruent recurrent child row
congruent payment
congruent closure route.
```

Equal complete score, equal selected label, one operation-signature class, or an installed operation-kind name is insufficient.

## Abstract source audit

Two installed sources were audited by exact theorem markers.

```text
owner/fate lineage and kernel ancestry:
  common-owner schema
  child-row schema
  payment/certificate schema

installed operation registry 1166:
  common-owner preservation schema
  operation schema
  payment class
  continuation/closure-route schema.
```

Their union covers all five required abstract components. Neither source alone covers all five, so the unique minimum abstract cover has size two.

This is only a schema cover. Neither document contains any of the first-host response labels

```text
2031, 2301, 2310, 3201
```

or an occurrence-faithful join for one response pair. The ancestry endpoint still reports zero populated owner/fate rows, while registry exhaustiveness is limited to the declared operation-kind bank.

Exact source census:

```text
source documents audited                    2
abstract components required                5
abstract components covered by union        5
minimum abstract source cover size          2
first-host response labels found            0
occurrence-faithful pair joins found        0.
```

## Three accepted proof modes

### Signature-specific mode

Populate all 32 stable menu/signature/pair records from the face-congruence worklist.

Each record requires nine fields:

```text
physical_occurrence_domain_ref
legal_menu_state_ref
operation_signature_domain_ref
common_owner_ref
operation_congruence_ref
child_row_congruence_ref
payment_congruence_ref
closure_route_congruence_ref
realization_status.
```

Exact burden:

```text
records          32
evidence slots  288
accepted records  0.
```

### Menu-parametric mode

Supply four theorems, one for each menu/pair domain:

```text
restore_02   : 2031 ~ 2310   10 signatures, 32 backgrounds
restore_both : 2031 ~ 2301    2 signatures,  8 backgrounds
restore_both : 2031 ~ 2310   10 signatures, 32 backgrounds
restore_both : 2031 ~ 3201   10 signatures, 32 backgrounds.
```

Each theorem requires ten fields, including signature-domain completeness and one theorem reference.

```text
records          4
evidence slots  40
accepted records 0.
```

### Cross-menu mode

Supply three response-pair theorems. The `2031~2310` theorem must quantify over both `restore_02` and `restore_both`; the other two apply to `restore_both`.

```text
records          3
evidence slots  30
accepted records 0.
```

A cross-menu theorem is not inferred from the response pair being written the same way in two menus.

## Acceptance boundary

A proof mode is accepted only when every record required by that mode is source-populated and internally consistent. Mixing incomplete records across modes does not close the gate.

Current result:

```text
accepted proof modes                       0 of 3
populated evidence slots across all modes  0
accepted import records                    0
face-congruence source import               0
selector tie-break substitution             0.
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_selector_face_source_import_gate.py \
  --check data/exact_recurrent_first_host_selector_face_source_import_gate.json
```

The checker joins the 32-obligation worklist to the two installed source documents, assigns stable record IDs, reconstructs all three proof modes, validates the unique two-source abstract cover, and rejects eighteen deliberate corruptions.

Physical occurrence coverage, restoration legality, persistent owner identity, recurrent child rows, payment and closure-route congruence, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.
