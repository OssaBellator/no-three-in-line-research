# Frontier pass: robust p=31 ratio-23 AN obstruction

## Active branch

`agent/ac-p31-ratio23-robust-obstruction`

Parent: `agent/ac-p31-seed-orbit-census` at `27f22c305a86cd31f499d6e32b9512abb145a8a0`.

Only AC is active.

## New theorem block

- **AC5nv:** complete seven-of-eight pair and endpoint-orientation bank.
- **AC5nw:** exhaustive robust nonimprovement.
- **AC5nx:** half-turn conjugacy of the two inserted candidates.
- **AC5ny:** exact AC1 certificate record for the best bank state.
- **AC5nz:** heavy-line decomposition and filter persistence.

## Exact results

- current potential: `82`;
- full secant pairs: `8`;
- occurrence-addressed bank states: `1,376,614`;
- class minima: `90,89,89,87,87,91,91,89`;
- improving states: `0`;
- global bank minimum: `87`;
- AC1 certificate counts at the best orientation: `208,122,13`;
- unique normalized heavy rank: `1`;
- heavy anchor: `(5,19)`, degree `14`;
- heavy-line split: `6,6,1,1`;
- rich-line-filter minima at fixed-line thresholds `3,4,5`: `87,87,87`.

The executable audit directly verifies each class minimizer. This corrects an earlier scratch note which listed omitted-pair classes five and six with minimum 87; their exact minima are 91.

## Validation

Run:

```text
python scripts/verify_ac_p31_ratio23_robust_bank.py
```

The verifier uses an exact fixed/unary/pair/triple decomposition for speed and independently recomputes the global minimum state by direct triple enumeration. It also checks the 180-degree candidate conjugacy and the high-line filters.

## Next frontier

The returned physical AC1 target is the 14-occurrence rank-one family through `(5,19)`. It must be converted into a conflict-safe paid star, quotient/carry/BDA structure, or a precise incompatibility/source Hall witness. The full state may also be attacked by larger matching blocks or the unrestricted two-row switch graph.

AC6 and the general conjecture remain open.
