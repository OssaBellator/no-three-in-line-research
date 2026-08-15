# Side-four projection does not identify the physical background

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact projection obstruction. It proves neither physical realization nor physical exclusion of the strict-reversal background.

## Current projected first-host record

The deterministic side-four manifest records the first residual host as

```text
host ID            s4-75b04c45c1c8eac2
deletions          02,20
intrinsic responses 3012:1, 3210:4
dispatch           blocker-alternative
blocker            b4-8a44614df456.
```

Its encoding contains the host ID, deletion edges, intrinsic response energies, dispatch and blocker IDs. It does not contain a coordinate-labelled background, physical deletion causes or physical owner/provenance labels.

## Two indistinguishable completions

The checker attaches two different backgrounds to that same projected record.

### Safe completion

```text
background: empty
scores: 3012=1, 3210=4, 2031=0, 2310=0, 3201=0
minimizer face: {2031,2310,3201}.
```

### Strict-reversal completion

```text
background: {(-3,5),(5,-3)}
scores: 3012=1, 3210=4, 2031=2, 2310=2, 3201=2
minimizer face: {3012}.
```

The complete raw-lineage identifiers differ because a complete identifier must retain the background. Nevertheless, both completions have exactly the same current side-four projected record.

Therefore the side-four projection is non-injective with respect to both the complete score vector and the minimizer face. No argument using only that projection can prove that the strict two-point signature is impossible.

## Relation to the upstream contracts

The general raw-fibre lineage theorem requires the background as part of the exact identifier and says kernel rows must be computed on the reconstructed background. The current deterministic side-four manifest builder, however, enumerates only deletion hosts and intrinsic response energies. Its own honesty fields leave global provenance and compulsory weighted rows incomplete.

This is not a contradiction: the side-four artifact is a host/response projection, not a populated complete raw-fibre batch.

## Required promotion data

Physical exclusion or routing now requires an artifact containing at least:

1. the coordinate-labelled background for every first-host occurrence;
2. physical causes and owners of deletions `02` and `20`;
3. owner/fate/collision/line/interface/CRT ancestry;
4. every installed legal operation and intermediate state;
5. labelled child multiplicities and positive weights.

Until those fields are supplied, both the safe and strict completions remain compatible with the current projection.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_side_four_projection_nonidentifiability.py \
  --check data/exact_recurrent_first_host_side_four_projection_nonidentifiability.json
```

The checker reconstructs both score vectors by direct triple enumeration, verifies distinct complete lineage identifiers, verifies the identical projected record, and rejects ten deliberate corruptions.

Physical realizability, physical exclusion, recurrent child rows, strict Lyapunov weights and `all_n_proved_by_checker` remain zero.
