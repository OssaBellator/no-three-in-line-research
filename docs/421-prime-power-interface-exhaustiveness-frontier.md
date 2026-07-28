# Prime-power interface-row exhaustiveness frontier

This chapter records CMR2566--CMR2573. It makes

```text
INTERFACE_RETURN_ROWS_EXHAUSTIVE
T15_INTERFACE_EXHAUSTIVENESS
```

an exact documentary proof surface over the fixed T04, T07, T11, T12, T13 and T14 banks.

The executable endpoint is:

```text
scripts/check_prime_power_interface_exhaustiveness_frontier.py
```

It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2566: supplied-interface defect

The older interface checker validates nonnegative weighted row margins and a strict-or-ranked
classification, but it accepts its own component multipliers, state ranks and interface-row list.
Consequently it can certify a parallel row family unrelated to the exact T04 population, T07 claims,
T13 state quotient, T14 component weights or T12-eliminated exits.

T15 removes that freedom. The row census is reconstructed before any T15 semantic or proof data is
read.

## CMR2567: corrected dependency root

Complete interface exhaustiveness consumes the final nonauxiliary exits remaining after T12. The exact
proof flow is therefore:

```text
T04_BLOCK_INTERFACE_POPULATION
T07_FATE_TRANSITION_STATE
T12_AUXILIARY_SEMANTICS
T14_COMPONENT_SCALES
    -> T15_INTERFACE_EXHAUSTIVENESS
```

The semantic obligation has the corresponding immediate roots:

```text
FATE_TRANSITION_STATE_SEMANTICS
AUXILIARY_EXPANSIONS_SEMANTIC
COMPONENT_SCALE_SEMANTIC
    -> INTERFACE_RETURN_ROWS_EXHAUSTIVE
```

The fixed obligation and atomic-target definitions have been corrected accordingly. Certificates whose
definition digests were generated under the former roots must be regenerated.

## CMR2568: exact T04-derived row census

Every T04 unit of kind `interface-row` contributes exactly one T15 record. The canonical identity binds:

```text
unit_id
row_id
row_kind
unit_identity_sha256
parent_global_state_id
operation_slot_id
t04_population_payload_sha256
```

Records are `open` or `proved`. Missing, duplicated, reordered or independently supplied rows are
rejected against the exact T04 order. A proved row uses:

```text
interface-row-registry://<row ID>
```

and requires the exact T04 payload.

## CMR2569: primitive intercomponent scaling

T14 deliberately leaves disconnected components independently normalized. T15 supplies one positive
integer `interface_multiplier` for every exact T14 component. The complete multiplier vector must have
greatest common divisor one.

For a T14 global component weight `W_g`, T15 reconstructs the final weight

\[
\widehat W_g=m_{C(g)}W_g.
\]

One internal artifact of kind

```text
global-interface-component-scale-proof
```

binds the multiplier bank and cites every T14 component artifact. This finite normalization does not
prove that the supplied interface equations determine the intended external relative scales.

## CMR2570: exact row semantics and arithmetic

Every proved row must bind the exact T07 semantic certificate and artifact of its T04 operation slot.
Its parent and every target must be exact proved T13 global classes with exact T14 component weights.
Auxiliary targets are forbidden after T12.

The semantic record binds the literal T04 fields through separate digests:

```text
target_states
route_data
transition_data
source_clause_binding
```

It supplies an integer fixed offset, target multiplicities, exact state/transition claim support,
statements and evidence. The checker reconstructs

\[
L=B+\sum_g a_g\widehat W_g,
\qquad
M=\widehat W_p-L.
\]

Negative margins are rejected. Positive margins are `strict`; zero margins are
`critical-unranked`. T15 does not accept a free rank witness: every zero-margin row remains explicit
work for T16.

## CMR2571: exact final-exit coverage

The checker reconstructs the selected nonrecurrent exits from every available T12 eliminated-row
certificate. It verifies that:

1. no auxiliary target remains after T12;
2. a recurrent target remains inside its T11 recurrent core;
3. every T11 auxiliary exit occurs in the T12 expansion closure;
4. every T11 nonauxiliary exit survives in the final T12 selected rows; and
5. every final source and target has an exact T13 global-state identity.

Every final exit receives exactly one disposition:

```text
interface-row
terminal-sink
```

An `interface-row` disposition must name a proved T15 row with the exact global parent and sufficient
target multiplicity. A `terminal-sink` disposition is allowed only for an exact T13 sink class.

While T12 remains open, currently unavailable block eliminations contribute no final-exit subjects.
Later T12 population can therefore enlarge the worklist and require affected T15 verification bundles
to be regenerated.

## CMR2572: typed proof sealing and synchronization

Every proved row requires one internal artifact of kind:

```text
interface-row-semantic-proof
```

Its exact support contains:

- the row's T04 population artifact;
- its slot's T07 semantic artifact;
- every relevant T12 auxiliary artifact;
- every parent/target T13 class artifact;
- every parent/target T14 component artifact; and
- the aggregate interface-component-scale artifact.

The per-row verification digest seals the record core, semantic certificate, assigned exit dispositions
and artifact.

The aggregate noncircular bank commits to the independent T04/T07/T11/T12/T13/T14 bank digests, the
component multipliers, row records, row semantics, final-exit subjects, dispositions and proof bundles.
It excludes certificates that contain T15's own completion digest.

When ready, the obligation artifact has kind `interface-exhaustiveness-proof`, locator

```text
interface-exhaustiveness-frontier://INTERFACE_RETURN_ROWS_EXHAUSTIVE
```

and exact support from the T07, T12 and T14 obligation artifacts. The T15 target uses the same kind and
locator

```text
interface-exhaustiveness-frontier://T15_INTERFACE_EXHAUSTIVENESS
```

with the aggregate proof-bank digest.

## CMR2573: honesty boundary and executable endpoint

Passing the checker establishes exact finite row census, ancestry, componentwise rescaling, weighted
row arithmetic, final-exit coverage, typed support and readiness synchronization relative to the
supplied certificates.

It does not prove that:

- the T04 interface population is genuinely exhaustive;
- the T07 state or transition statements are true;
- the T12 exit semantics are correct;
- the T13 identities or T14 scale equations have their intended mathematical meaning;
- a zero-margin row has a genuinely decreasing well-founded rank;
- the interface row statements are mathematically true;
- all exceptional chambers close; or
- the quotient implies `D(n)=2n` for every `n`.

The next exact frontier is T16 global-rank well-foundedness. T16 must derive its critical-edge census
from T15's `critical-unranked` rows and prove a genuine well-founded decrease rather than accepting an
independent rank table.
