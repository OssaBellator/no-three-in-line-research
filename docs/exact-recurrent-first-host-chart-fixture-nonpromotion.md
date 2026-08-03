# First-host chart-fixture non-promotion

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact source-boundary theorem. It does not alter the conditional chart-confinement transfer.

## Installed geometric host result

The geometric-fibre chapters place the coordinate-labelled response hosts on the
standard grid

```text
Omega_d={0,...,d-1}^2.
```

This fixes response-edge geometry and line incidence. It does not by itself
place the independent background set inside the same chart.

The host-census theorem defines rank-two coefficients for an arbitrary fixed
background `B` and its endpoint explicitly states that the remaining work is to
attach the actual background and recurrent provenance data.

## What the verifiers test

Two finite verifiers construct synthetic backgrounds by

```python
remaining = sorted(grid - set(response))
background = random sample of remaining
```

This is an appropriate fixture for checking the complete-energy identity and
line-cap inequalities under chart-confined, response-disjoint inputs.

It is not a source trace for a physical occurrence:

- the samples are random test data;
- neither verifier contains the first-host stable ID;
- no occurrence domain or completeness proof is attached;
- the ancestry checker keeps `geometric_fibre_rows_complete_all_provenance=0`;
- the repository status keeps `raw_fibre_backgrounds_cover_all_provenance=0`.

## Exact distinction

```text
coordinate-labelled response hosts on standard grid      yes
synthetic grid-minus-response background fixtures        yes
background treated as independent theorem input          yes
actual physical background attachment completed          no
physical chart-confinement invariant installed           no
physical response-disjointness invariant installed       no
```

Therefore the fixture may validate a conditional identity, but it may not be
promoted to a proof that every physical first-host background is chart-confined
or response-disjoint.

## Consequence for the transfer theorem

The chart-confinement transfer remains a sharp conditional shortcut. To activate
it, a construction source must independently prove both predicates for every
physical `{02,20}` occurrence. Re-running the existing random fixtures cannot
supply that proof.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_chart_fixture_nonpromotion.py \
  --check data/exact_recurrent_first_host_chart_fixture_nonpromotion.json
```

The checker binds two source chapters, two synthetic verifiers, the geometric
ancestry checker, and the repository honesty ledger. It rejects eleven deliberate
corruptions.

Physical chart confinement, response disjointness, occurrence coverage,
recurrent rows, strict Lyapunov slack, and `all_n_proved_by_checker` remain zero.
