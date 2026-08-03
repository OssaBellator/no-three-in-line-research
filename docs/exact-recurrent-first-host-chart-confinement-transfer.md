# First-host chart-confinement transfer

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional source-domain theorem. The physical source has not proved either hypothesis.

## Source predicates

Assume a physical first-host occurrence satisfies both:

```text
all background points are integer cells in [0,3] x [0,3]
the background is disjoint from the five-response union
```

The five candidate responses occupy exactly eleven cells:

```text
02,03,10,12,13,20,21,23,30,31,32.
```

Their response-disjoint chart complement is therefore exactly

```text
F={00,01,11,22,33}.
```

Thus chart confinement and response disjointness force every background into the
previously audited safe five-cell class.

## Exact transfer

All `2^5=32` subsets of `F` were recomputed by direct triple enumeration. Every
one has minimizer face

```text
{2031,2310,3201}.
```

Consequently the two source predicates exclude both:

1. every strict original-response reversal;
2. every non-strict state in which `3012` or `3210` enters the minimizer face.

The global four strict backgrounds are all exterior to the standard chart.
Their exact `L_infinity` cap transfer is

```text
coordinate cap 4: 0 strict backgrounds
coordinate cap 5: 2 strict backgrounds
coordinate cap 6: 4 strict backgrounds.
```

The stronger chart theorem uses `[0,3]^2`, not merely radius four, and also
closes all original-response ties because only the five safe cells remain.

## Scope boundary

This theorem is conditional. The current physical-source coverage audit has no
source reference proving chart confinement or response disjointness. The
installed raw-lineage validator does not enforce either condition.

Even after the source predicates are supplied, legal reopening, deletion causes,
owner ancestry, child rows, positive weights, and parent budget remain separate
obligations.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_chart_confinement_transfer.py \
  --check data/exact_recurrent_first_host_chart_confinement_transfer.json
```

The checker reconstructs the response union, proves its chart complement is
`F`, audits all 32 backgrounds, joins the global strict-reversal list, verifies
the cap table, and rejects eleven deliberate corruptions.

Physical chart confinement, response disjointness, legal reopening, recurrent
rows, strict Lyapunov slack, and `all_n_proved_by_checker` remain zero.
