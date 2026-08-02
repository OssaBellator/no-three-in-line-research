# Exact selected-response provenance on the side-four residual kernel

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** deterministic normalized selector provenance proved exactly; physical
and global provenance remain open.

## Theorem ERL-S4.3 — PROVED

Each of the eleven residual side-four hosts has a unique minimum-energy surviving
response under the upstream rule

```text
minimize intrinsic collinear-triple count,
then choose the lexicographically least response.
```

The complete census is

```text
selector 3012, energy 1, next gap 3      9 hosts
selector 3210, energy 4, no higher face  2 hosts
```

Every residual host has fate `B` in the upstream selected-response manifest, and
every selected minimizer face is a singleton. Thus no selector tie remains inside
the eleven-state raw host kernel.

## Exact normalized provenance

The upstream selected-response layer supplies the following normalized fields:

```text
owner scope       side-four-raw-host
line class        minimum-response-energy
interface         target-01
CRT scope         not-applied
collision key     host deletion trace
host fate         B
```

For every residual host, the checker joins these fields to the exact stable host
ID, deletion trace, blocker identifiers, selected response, minimum energy and
next-energy gap.

## Correction to the raw-lineage gap audit

The earlier raw-lineage projection correctly recorded that the raw lineage file
itself did not populate owner/fate/collision/line/interface/CRT slots. A separate
upstream selected-response manifest does populate **normalized** values for those
six coordinates.

Accordingly, those 66 host-field incidences are no longer described as wholly
missing. They are normalized classes, not complete physical provenance.

The unresolved refinements remain:

- actual physical backgrounds;
- physical causes and owners for each unavailable cell;
- owner identity below the scope label `side-four-raw-host`;
- collision and line ancestry beyond the deletion trace and minimum-energy class;
- legal installed operations and intermediate states;
- exact recurrent child rows and weighted coefficients.

## Why this is useful

The canonical selected response is now fixed before any repair accounting begins.
For the first host

```text
upstream ID  s4-75b04c45c1c8eac2
deletions    {02,20}
selector     3012
energy       1
next gap     3
blocker      b4-8a44614df456
```

Any legal repair analysis for this host must therefore account for the single
triple created by response `3012`, or reopen enough blocked cells to expose a
zero-energy response. It may not change the selector through an undocumented tie
or representative choice.

The two energy-four hosts are structurally sharper: `3210` is their only
surviving response, so there is no higher-response alternative inside the raw
host.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_side_four_selected_provenance_projection.py \
  --kernel data/exact_recurrent_side_four_kernel.json \
  --lineage-projection data/exact_recurrent_side_four_lineage_projection.json \
  --selected-projection \
    data/exact_recurrent_side_four_selected_provenance_projection.json
```

The audit rejects twelve corruption classes, including changed selectors,
minimizer faces, energies, gaps, fates, collision keys, normalized owner scope,
honesty flags and all-`n` promotion.

## Remaining theorem target

For host `s4-75b04c45c1c8eac2`, reconstruct every physical background and cause
assignment compatible with deletion trace `{02,20}`. For each fibre, determine
whether the installed operation bank can legally remove the unique selected
triple, reopen `02` or `20`, or route to a strictly smaller labelled state. The
output must be a complete exact transition row or an explicit underdetermination
or recurrence witness.
