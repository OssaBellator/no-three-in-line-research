# Frontier pass: p=31 robust heavy-anchor classification

## Active branch

`agent/ac-p31-heavy-anchor-classification`

Parent: `agent/ac-p31-ratio23-robust-obstruction` at `166fd7173c8f863edaa44cf6a3c4347eb4ee1de9`.

Only AC is active.

## New theorem block

- **AC5oa:** complete physical occurrence dictionary.
- **AC5ob:** direction and channel-pair decomposition.
- **AC5oc:** exact product-carry signature census.
- **AC5od:** exact six-edge endpoint-disjoint extraction.
- **AC5oe:** six distinct carry signatures in one maximum matching.
- **AC5of:** payment-safe AC2 continuation.

## Exact results

- heavy anchor: `(5,19)`;
- rank-one occurrences: `14`;
- primitive direction multiplicities: `6,6,1,1`;
- endpoint channel-pair multiplicities: `3,8,3`;
- product-carry signatures: `11`;
- largest signature fibre: `4`;
- endpoint graph: `K4 + K4 + K2 + K2`;
- matching number: `6`;
- distinct carry signatures in a maximum matching: `6`;
- nontrivial slope denominators: none;
- owner route: `PROSPECTIVE`;
- automatic payment: `0`.

## Validation

Run:

```text
python scripts/verify_ac_p31_heavy_anchor_classification.py
```

The verifier reconstructs the robust best orientation, enumerates every heavy-anchor pair, computes physical channel and product-carry labels, exhausts all edge subsets for the exact matching number and checks the prospective payment guardrail.

## Next frontier

Build complete repair objects around the six-edge star, enumerate their full AC2 incompatibility graph and attach actual current owner/source tokens. The valid output must be a paid compatible family, a carry-exposure step, or an exact conflict/source obstruction.

AC6 and the general conjecture remain open.
