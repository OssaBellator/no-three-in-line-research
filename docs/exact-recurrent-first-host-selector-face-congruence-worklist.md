# First-host selector-face congruence worklist

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact finite worklist for replacing an unsourced restored-menu tie-break by complete minimizer-face congruence. It does not prove any physical occurrence, restoration operation, child row, payment, or closure route congruent.

## Why this worklist is needed

The selector-rule compatibility audit found two tied restored menus:

```text
restore_02:
  complete minimizer face {2031,2310}
  32 tied safe backgrounds

restore_both:
  complete minimizer face {2031,2301,2310,3201} on 8 backgrounds
  complete minimizer face {2031,2310,3201} on 24 backgrounds.
```

The installed construction supplies no first-host lexicographic scheduler rule. Therefore selecting `2031` is physically harmless only if every response in the relevant complete-score face is interchangeable for the recurrent certificate.

## Minimum transitive basis

For a face of size `k`, face-wide equivalence can be proved from `k-1` comparisons by anchoring every member to `2031`, the lexicographically least face member.

The raw background-level burden is

```text
restore_02:
  32 backgrounds x 1 comparison = 32

restore_both four-way face:
   8 backgrounds x 3 comparisons = 24

restore_both three-way face:
  24 backgrounds x 2 comparisons = 48

raw anchored comparisons total        = 104.
```

The exact four-coordinate operation signature partitions the 32 safe backgrounds into ten classes. Joining each tied face to those classes compresses the enumerated worklist to

```text
menu/signature cells                    20
signature-level pair obligations        32.
```

This is only a finite indexing compression. The operation signature was derived from complete-score geometry and is not assumed to determine physical owners, legal operations, child rows, payments, or routes.

## Exact pair census

The 32 signature-level obligations use three response-pair types:

```text
2031 ~ 2301:
  2 signature obligations
  8 raw background comparisons

2031 ~ 2310:
  20 signature obligations
  64 raw background comparisons

2031 ~ 3201:
  10 signature obligations
  32 raw background comparisons.
```

The `2031~2310` pair occurs in both tied menus. That does not make its two menu contexts congruent.

## Uniform-theorem alternatives

A source can discharge the worklist at one of three granularities.

### Signature-specific

Populate all 32 menu/signature pair obligations separately.

### Menu-parametric

Supply four theorems, each explicitly uniform over the listed signature domain:

```text
restore_02   : 2031 ~ 2310   10 signatures, 32 backgrounds
restore_both : 2031 ~ 2301    2 signatures,  8 backgrounds
restore_both : 2031 ~ 2310   10 signatures, 32 backgrounds
restore_both : 2031 ~ 3201   10 signatures, 32 backgrounds.
```

### Cross-menu parametric

Supply three response-pair theorems, with `2031~2310` explicitly quantified over both restored menus and their distinct legal states. This is the strongest compression and currently has no source record.

No collapse from 32 to four or three obligations is automatic. It requires a source theorem proving the stated uniformity over signatures and, when applicable, menus.

## Evidence contract

Each signature-level obligation requires nine fields:

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

All fields must refer to the same physical occurrence domain, legal menu state, persistent owner, and response pair.

Exact evidence census:

```text
signature-level obligations              32
evidence fields per obligation             9
total signature evidence slots           288
populated signature evidence slots         0
accepted signature obligations             0
imported menu-parametric theorems           0
imported cross-menu theorems                0.
```

## Source boundary

The worklist proves only that the anchored comparisons are sufficient on the enumerated safe class. It does not prove:

```text
the ten operation signatures physically complete
responses in a face share one owner
operations are legal or congruent
child rows are equal
payment vectors are equal
closure routes are equal
an unsourced tie-break may be substituted.
```

Accordingly, source-backed face congruence remains zero.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_selector_face_congruence_worklist.py \
  --check data/exact_recurrent_first_host_selector_face_congruence_worklist.json
```

The checker joins the selector-rule compatibility and restoration-menu manifests, reconstructs all 32 safe backgrounds and ten operation signatures, compiles the 104 raw comparisons and 32 signature obligations, and rejects sixteen deliberate corruptions.

Physical occurrence coverage, restoration legality, persistent owner identity, child rows, payments, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.
