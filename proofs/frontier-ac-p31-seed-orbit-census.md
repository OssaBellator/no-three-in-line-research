# Frontier pass: complete p=31 seed-orbit census

## Active branch

`agent/ac-p31-seed-orbit-census`

Parent: `agent/ac-prime-seed-census` at `58a76c65a350ddabf1f35604dabea76bcbe13c87`.

Only AC is active.

## New theorem block

- **AC5nq:** complete 216-address canonical seed census.
- **AC5nr:** exact channel-ratio improvement table.
- **AC5ns:** 54-orbit square-symmetry quotient and mixed-orbit witness.
- **AC5nt:** equivariant representative selector.
- **AC5nu:** corrected uniform seed continuation interface.

## Exact results

- canonical seed addresses: `216`;
- improving addresses: `140`;
- nonimproving addresses: `76`;
- neutral best state: `10`;
- every state strictly worse: `66`;
- best-minus-current range: `-33` through `31`;
- square-symmetry orbits: `54`, each of size `4`;
- raw-rule orbit types: `30` all improving, `14` all nonimproving, `10` mixed `2:2`;
- equivariant representative outcomes: `37` improving and `17` nonimproving;
- unique uniformly nonimproving ratio: `23`;
- uniformly improving ratios: `7,8,9,11,15,17,24,26,30`.

The executable census derives ratio `2` as `2` improving and `6` nonimproving addresses, correcting an erroneous transposed scratch-table entry before it entered a theorem file.

## Validation

Run:

```text
python scripts/verify_ac_p31_seed_orbit_census.py
```

The verifier regenerates every physical seed, exhausts every matching bank, constructs complete role-preserving geometric records, closes their `D_4` orbits, and evaluates the equivariant representative selector.

## Next frontier

The ratio-23 class is now the canonical robust-obstruction target. The next pass exhausts all choices of seven among eight secant pairs and all endpoint orientations, rather than trusting one coordinate-dependent selector.

AC6 and the general conjecture remain open.
