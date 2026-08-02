# Frontier pass: durable p=31 trajectory through three

## Branch

`agent/ac-p31-recovered-tail`

## Theorem

**AC5oi.** The four committed switch certificates concatenate exactly into a 785-switch path

`75 -> 6 -> 5 -> 4 -> 3`.

Every boundary state agrees exactly, every switch is legal, both layers remain disjoint permutations, and every stored potential is reproduced by determinant counting.

## Segment lengths

- 75 to 6: `154`;
- 6 to 5: `69`;
- 5 to 4: `527`;
- 4 to 3: `35`;
- total: `785`.

Including the initial alternating-star installation, the durable manifest prefix has `786` operations.

## Artifacts

- `scripts/verify_ac_p31_durable_trajectory.py`
- `docs/alternating-core-p31-durable-trajectory-through-three.md`
- the four versioned data files read by the verifier.

## Next task

Extend the same durable chain from three to two, then one and zero. Add each segment to the end-to-end verifier only after its independent barrier and replay certificate is committed.
