# Twenty-second boundary budget-seven computation protocol

## Status

This chapter records reproducibility infrastructure only. It does not state a new
prime-patching theorem, does not select a canonical twenty-two-block state, and
does not advance theorem numbering beyond `PP3dfi`. The next theorem identifier
remains `PP3dfj` until the complete computation has been executed and reviewed.

The all-`n` theorem remains open.

## Frontier

The canonical twenty-one-block state has 168 points. Its raw twenty-second
spectrum has minimum transversal six, attained by 26 attempts with 178 minimum
cores. Budget six rejects every row/column-preserving correction. The open finite
question is whether any of those 178 cores repairs at deletion budget seven and,
if so, which repaired states have the strongest exact raw twenty-third frontiers.

## Pipeline

The budget-seven computation is split into four independently reviewable stages.

1. `check_boundary_twentysecond_budget_seven_shard_701.py`
   partitions the 178 cores by canonical global index and runs the legacy exact
   replacement-permutation search at budget seven.
2. `merge_boundary_twentysecond_budget_seven_701.py`
   rejects missing, duplicate, inconsistent, or mispartitioned shard payloads.
3. `check_boundary_twentysecond_budget_seven_witnesses_701.py`
   reruns every repair-positive job with the independent exact-cover kernel,
   extracts deleted and replacement point sets, and audits row multisets, column
   multisets, cardinality, distinctness, core containment, and every point triple.
4. `check_boundary_twentysecond_budget_seven_next_spectra_701.py`
   recomputes the exact raw twenty-third spectrum for every audited repaired state
   at next block origin 88. It reports transparent lexicographic low-frontier ranks
   and a cumulative-threshold Pareto set, but does not select a state.

The wrapper `run_boundary_twentysecond_budget_seven_701.py` executes all four
stages and writes a compact summary. Example:

```bash
python scripts/run_boundary_twentysecond_budget_seven_701.py \
  --shard-count 16 \
  --workdir certificates/boundary-budget-seven-701 \
  --resume
```

`--resume` accepts an existing shard only after checking its status, shard index,
and shard count. Merge and all later certification stages are always rerun.

## Required evidence before promotion

A theorem chapter may be written only after the following are available from one
complete run:

- all 178 canonical core indices exactly once;
- the complete repair-positive count;
- an independently audited witness for every positive legacy result;
- exact raw twenty-third spectra for every audited repaired state;
- a stated and mathematically justified state-selection rule;
- a committed certificate containing the merged census, witnesses, spectra, and
  selected-state reconstruction;
- isolated reruns of the selected witness and its complete no-three audit.

A finite selected continuation would still not prove recurrence, periodicity, or
an all-length prime-patching construction.

## Current limitation

The repository API environment used to prepare this protocol cannot execute the
C++ kernels or obtain a full local checkout. Therefore no census result, repair
count, witness, spectrum, or state selection is asserted here.
