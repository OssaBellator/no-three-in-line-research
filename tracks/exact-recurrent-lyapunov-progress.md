# Exact recurrent Lyapunov progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

## ERL1 finite seed — PROVED LOCALLY

The exact side-four host compiler reconstructs all 86 feasible hosts and 206
response incidences. It isolates 11 residual hosts, proves the three minimal
blockers

```text
{02,20}, {02,31}, {13,31},
```

and identifies `{02,13,20,31}` as the unique local reopening-depth-two state.
All global provenance, legal-reopening, recurrent-row, Lyapunov and all-`n`
flags remain zero.

Artifacts:

```text
scripts/check_exact_recurrent_side_four_kernel.py
data/exact_recurrent_side_four_kernel.json
docs/exact-recurrent-side-four-kernel.md
.github/workflows/exact-recurrent-side-four-kernel.yml
```

## ERL1a raw lineage projection — PROVED EXACTLY

The eleven residual states join bijectively to stable upstream raw-fibre host
IDs and the three blocker IDs. The audit checks deletion sets, response spectra,
blocker dispatch and contained blocker classes, rejecting nine mutation
corruptions.

The raw lineage layer leaves null:

```text
physical deletion-cause assignments                 32
background records                                  11
raw owner/fate/collision/line/interface/CRT slots    66
legal operation families                            11
recurrent child rows                                11
```

These counts describe the raw lineage file only.

Artifacts:

```text
scripts/check_exact_recurrent_side_four_lineage_projection.py
data/exact_recurrent_side_four_lineage_projection.json
docs/exact-recurrent-side-four-lineage-projection.md
.github/workflows/exact-recurrent-side-four-lineage-projection.yml
```

## ERL1b selected-response provenance — PROVED EXACTLY

A separate upstream manifest fills normalized selector provenance for every
residual host. All eleven minimizer faces are singletons:

```text
selector 3012, minimum energy 1, next gap 3      9 hosts
selector 3210, minimum energy 4, no higher face  2 hosts
```

The normalized key is

```text
owner scope       side-four-raw-host
fate              B
collision key     host deletion trace
line class        minimum-response-energy
interface         target-01
CRT scope         not-applied
```

Thus the earlier 66 raw-layer null slots are now populated by exact normalized
classes. They are not complete physical provenance: actual backgrounds,
deletion causes, owner identities, collision ancestry, legal operations and
child rows remain open.

Artifacts:

```text
scripts/check_exact_recurrent_side_four_selected_provenance_projection.py
data/exact_recurrent_side_four_selected_provenance_projection.json
docs/exact-recurrent-side-four-selected-provenance.md
.github/workflows/exact-recurrent-side-four-selected-provenance.yml
```

The selected-provenance audit rejects twelve corruption classes and retains all
global proof flags at zero.

## ERL1c selected-line geometry — PROVED EXACTLY

Every canonical residual response has all of its collinear triples on a single
affine line. There are only two exact line classes:

```text
selector 3012 -> x-y-1=0, primitive key (1,-1,-1), energy 1, 9 hosts
selector 3210 -> x+y-3=0, primitive key (1,1,-3), energy 4, 2 hosts
```

Hence all eleven selected residual states are single-line supported. The total
selected triple incidence count is `9*1 + 2*4 = 17`.

Artifacts:

```text
scripts/check_exact_recurrent_side_four_selected_line_geometry.py
data/exact_recurrent_side_four_selected_line_geometry.json
docs/exact-recurrent-side-four-selected-line-geometry.md
.github/workflows/exact-recurrent-side-four-selected-line-geometry.yml
```

The geometry audit rebuilds response points, enumerates all triples, normalizes
primitive line equations and rejects twelve corruption classes. Physical line
ownership, background interactions, legal repairs and recurrent rows remain
open.

## First active host

```text
upstream ID  s4-75b04c45c1c8eac2
deletions    {02,20}
selector     3012
energy       1
line         x-y-1=0
triple       {(1,0),(2,1),(3,2)}
next gap     3
blocker      b4-8a44614df456
```

The local repair alternatives are exact:

```text
restore 02 -> zero-energy responses 2031 and 2310
restore 20 -> zero-energy response 3201
```

The remaining question is no longer which response or line is bad. It is whether
the exact selected line can be legally destroyed or either blocked cell can be
legally reopened in every physical provenance fibre.

## Active work queue

- Issue #18: enumerate every physical background and cause assignment over
  `s4-75b04c45c1c8eac2`, then enumerate only installed legal transitions.
- Issue #19: publish any realizable non-strict SCC or failed row rather than
  hiding it behind another conditional interface.
- Issue #20: classify the unique depth-two overlap under installed operations.
- Issue #21: compile exact offspring rows and solve or refute the strict rational
  Lyapunov system.

## Next acceptance test

A compiler for `s4-75b04c45c1c8eac2` must output:

1. every physically realizable background fibre over deletion trace `{02,20}`;
2. the physical cause and owner of unavailable cells `02` and `20`;
3. the refinement of the normalized fate/collision/line/interface/CRT key;
4. the status of exact line `x-y-1=0` in the surrounding background;
5. every installed legal operation and intermediate state;
6. exact resulting child labels and multiplicities;
7. either a complete row suitable for `check_exact_recurrent_manifest.py` or a
   source-backed witness that the current repository data are insufficient.

No progress entry may set `all_n_proved_by_checker` to one.
