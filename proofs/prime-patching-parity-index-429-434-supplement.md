# Prime-patching parity index supplement: `docs/429--434`

This supplement continues the cumulative parity index after `docs/428` and
crosses the theorem suffix boundary from `PP3bzz` to `PP3caa`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bzz--PP3cab | Source-dependent stopping depths combine with no level-count loss when the stopping level is intrinsic; conditioned prefix reservoirs retain their per-level load bounds and failure localizes to one overmerged level target | PROVED | `docs/429-intrinsic-stopping-depths-for-marker-trees.md` |
| PP3cac--PP3cae | Every two-sided Hall rectangle contains both controlled-order target bicliques and a matching bounded below by its edge count and endpoint degrees | PROVED | `docs/430-bicliques-and-matchings-inside-hall-rectangles.md` |
| PP3caf--PP3cah | Source-dependent multiplicity thresholds have an exact column formula; classwise envelopes permit heterogeneous stripping and overload localizes to one target and one tail class | PROVED | `docs/431-source-adaptive-multiplicity-stripping.md` |
| PP3cai--PP3cak | Variable-length prefix-free corridor schedules have risk `max_i rho_i p^{-ell_i}`; a proposed risk is feasible exactly when its maximum allowed lengths satisfy Kraft's inequality | PROVED | `docs/432-variable-length-corridor-schedule-codes.md` |
| PP3cal--PP3can | Multiplicative Bellman--Ford relaxation returns either a rational shell potential after `|V|` rounds or an explicit expansive simple cycle | PROVED | `docs/433-multiplicative-bellman-ford-shell-certificates.md` |
| PP3cao--PP3caq | The transient type resolvent is an exact finite sum over condensation-DAG paths; scalar and entrywise local SCC bounds propagate monotonically through that sum | PROVED | `docs/434-condensation-dag-resolvent-expansion.md` |

## Frontier update

### Boundary recleaning

Sequential marker repair no longer needs one common stopping depth.  Partition
sources by the depth at which their prefix remains geometrically safe.  If the
stopping level is recoverable from the final target, the combined load is
exactly the maximum level load, not their sum.  With level prefix degree `Q_i`,
predecessor ambiguity `h_i`, and retained mass `p_i`,

```text
lambda<=max_i h_i/(p_i Q_i).
```

Failure returns one stopping depth and one overmerged prefix target.  The local
search may therefore halt before the first bad continuation instead of
discarding the whole marker word.

### Localized Hall transport

A dense Hall rectangle now supplies two simultaneous objects.  For every
`q<=d`, some `q` targets are common to at least

```text
ceil(s binom(d,q)/binom(t,q))
```

sources.  Under source and target degree caps `D,Delta`, it also contains a
matching of size at least

```text
ceil(sd/(D+Delta-1)).
```

The shared target core supports conditioned repairs, while the matching gives
an edge-disjoint bank.

### Fractional direct-clean layers

Multiplicity stripping may now use a different threshold `h_x` at every
source.  The resulting uniform retained-action kernel has exact load

```text
max_y sum_(x:y retained from x) 1/d_h(x).
```

This strictly improves the best global threshold on the stored audit graph,
from `5/6` to `2/3`.  Failure is localized to one target and one threshold
class, making heterogeneous multiplicity tails directly auditable.

### Support-chord repair words

Unequal corridor banks may use variable-length prefix-free schedules.  If one
schedule symbol retains mass at least `p`, bank `i` with load `rho_i` and code
length `ell_i` contributes at most

```text
rho_i p^(-ell_i).
```

For a proposed risk `R`, define

```text
L_i(R)=floor(log_(1/p)(R/rho_i)).
```

The risk is feasible exactly when every `L_i(R)>=1` and

```text
sum_i b^(-L_i(R))<=1.
```

Thus optimal schedule lengths follow from a finite exact Kraft test.

### Clean-macro shells

The shell audit now has a direct relaxation algorithm.  Normalize every edge by
a proposed rate `q` and run `|V|` multiplicative Bellman--Ford rounds.  If the
last round stabilizes, the path maxima form a rational positive potential.  If
it improves, predecessor tracing exposes a simple cycle with product larger
than `q` to the cycle length.  Exhaustive simple-cycle enumeration is no longer
required.

### Integration

For transient SCC blocks in topological order, the exact global resolvent block
from component `i` to component `j` is the finite sum over condensation paths

```text
R_i A_(i i_1) R_(i_1) ... A_(i_(r-1) j) R_j.
```

There is no infinite intercomponent series because the condensation graph is
acyclic.  Exact, truncated, and potential-bounded local SCC resolvents can be
mixed component by component and propagated as a rigorous global interval.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_429_434.py
```

or individually with

```bash
python scripts/check_intrinsic_marker_stopping.py
python scripts/check_hall_rectangle_bicliques_matchings.py
python scripts/check_source_adaptive_multiplicity_stripping.py
python scripts/check_variable_length_corridor_codes.py
python scripts/check_multiplicative_bellman_ford.py
python scripts/check_condensation_dag_resolvent.py
```

The local audits verify exact intrinsic-depth loads, 10,000 Hall rectangles,
every adaptive threshold assignment of a stored action graph, 4,507 feasible
monotone binary length vectors for seven unequal banks, both Bellman--Ford
branches with a nonconstant rational potential, and exact condensation-path
resolvent intervals.

The next available theorem identifier is `PP3car`.
