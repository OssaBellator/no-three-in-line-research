# Twenty-second boundary: exact budget-seven search protocol

## Status

This chapter records search infrastructure only. It does **not** assert a repair,
an obstruction, or a new `PP3` theorem. The next theorem identifier therefore
remains `PP3dfj` until all 178 canonical minimum-six cores have been covered and
the resulting witness or obstruction has been independently checked.

## Canonical frontier

The selected twenty-one-block state has 168 points. Its raw twenty-second
spectrum has minimum transversal six, with 26 minimum attempts and 178 minimum
cores. The complete deletion-budget-six layer rejects all 68,580 preserving
replacement permutations.

The next exact question is whether any of those 178 cores admits a
row/column-preserving correction after one additional deletion.

## Resumable runner

Use:

```bash
python scripts/run_boundary_twentysecond_budget_seven_shard.py \
  --shard-index I --shard-count K \
  --output certificates/budget-seven/shard-I-of-K.json
```

where `0 <= I < K`. Core assignment is deterministic: canonical global core
index `g` belongs to shard `g mod K`. Every output record includes:

- the global core index;
- the raw-attempt and local-core indices;
- the primitive and vertical offset;
- the exact six-point core;
- whether a budget-seven repair was found; and
- the number of replacement permutations tested before termination.

The runner reconstructs the canonical twenty-one-block state and raw
 twenty-second spectrum through
`scripts/check_boundary_continuation_694.py`, compiles the exact correction
kernel, and invokes it at deletion budget seven.

## Completion gate

A completed census must satisfy all of the following before any theorem is
stated.

1. The union of shard records contains each global core index `0,...,177`
   exactly once.
2. Every record has budget seven and refers to the canonical minimum-six
   frontier.
3. If a repair is found, its deletion and replacement sets must be emitted by a
   witness-producing kernel, replayed against the reconstructed predecessor,
   and subjected to a complete exact no-three audit.
4. If no repair is found, the aggregate permutation count and per-core count
   histogram must be frozen in a certificate and independently reproduced.
5. Any repaired states must be compared by their exact raw twenty-third spectra
   before selecting a continuation path.

## Current limitation

The existing legacy kernel is exact but does not yet share geometric candidate
precomputation between cores. The shard runner makes the census resumable and
reviewable; it does not by itself remove the principal computational cost.
A specialized shared-precomputation kernel remains the preferred next
engineering step.

The all-`n` prime-patching theorem remains open.
