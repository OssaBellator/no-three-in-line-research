# ERL evidence-scope overlap review gate

Apply this gate to any claim that reduces the source burden of a state, family, or individual-edge certificate pattern by reusing evidence.

## Required acceptance conditions

A sharing claim is admissible only when all of the following are explicit:

1. the exact certificate instances covered by the claim;
2. the source-defined occurrence domain for those instances;
3. a field-equivalence map naming every slot proposed for sharing;
4. a theorem proving uniformity over the entire mapped domain;
5. a scope-preservation proof showing that state-, family-, and edge-local statements remain valid;
6. a local-obligation preservation proof showing that no theorem field disappears merely because two labels match;
7. realization status for the sharing theorem itself.

## Mandatory distinctions

Reviewers must distinguish:

```text
field label                 textual schema name
field slot                  one certificate-instance obligation
source reference            document, theorem, row, or checker reference
sharing theorem             proof that one source fact satisfies several slots
```

One source reference may populate several slots, but only after a sharing theorem proves that it satisfies each scoped statement.

## Automatic rejection conditions

Reject any argument that:

- counts only distinct field-name strings;
- removes duplicate `realization_status` slots without a uniform realization theorem;
- treats two state certificates as one six-field contract because their schemas match;
- treats several edge routes as one route contract because their field names match;
- identifies `physical_occurrence_domain_ref` with `physical_source_ref` without an explicit bridge;
- replaces exact edge-local exclusion proofs with one generic exclusion label;
- reports five lexical fields as a complete three- or four-edge physical-exclusion certificate;
- promotes a source-document count into a proof-obligation count;
- lowers the eleven-slot label floor or twelve-slot menu floor while the sharing gate is empty.

## Current accepted boundary

```text
minimal safe label burden                  11 scoped slots
minimal safe menu burden                   12 scoped slots
accepted sharing theorems                   0
populated sharing fields                    0
```

The unsafe lexical floors are five field names under physical exclusion. They are diagnostic undercounts, not admissible certificates.

## Required checker

```bash
python scripts/check_exact_recurrent_first_host_evidence_scope_overlap_obstruction.py \
  --check data/exact_recurrent_first_host_evidence_scope_overlap_obstruction.json \
  --self-test
```

No review acceptance may imply physical occurrence coverage, legal transition realization, recurrent child rows, strict Lyapunov closure, global termination, or the no-three-in-line conjecture.
