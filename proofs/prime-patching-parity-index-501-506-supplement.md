# Prime-patching parity index supplement: `docs/501--506`

This supplement continues the cumulative parity index after `docs/500`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cih--PP3cij | Rational stationary marker flows have exact Eulerian periodic implementations, finite prefix-discrepancy tables, and localized flow-walk audits | PROVED | `docs/501-eulerian-realization-of-rational-marker-flows.md` |
| PP3cik--PP3cim | Repeated binary Hall syndrome blocks are exact xor convolutions diagonalized by Walsh characters, with count reconstruction and reverse-load transfer | PROVED | `docs/502-walsh-acceleration-for-binary-hall-syndromes.md` |
| PP3cin--PP3cip | Downward-closed threshold designs admit feasible denominator rounding, explicit objective loss, and exact finite grid optimization | PROVED | `docs/503-quantized-realization-of-threshold-designs.md` |
| PP3ciq--PP3cis | Risk-decorated prefix codes have survival-preserving canonical signatures, isomorph-free orbit recurrences, and finite optimum lifting certificates | PROVED | `docs/504-canonical-signatures-for-risk-decorated-prefix-codes.md` |
| PP3cit--PP3civ | Shell cycle covers admit feasible upward quantization, additive cost guarantees, and exact integer covering certificates | PROVED | `docs/505-quantized-shell-attenuation-schedules.md` |
| PP3ciw--PP3ciy | Repeated interaction motifs have an exact asymptotic circulation-rate polytope, periodic realizations, and minimum-cycle-mean separation | PROVED | `docs/506-asymptotic-cycle-rate-polytopes-for-interactions.md` |

## Frontier update

### Boundary recleaning

A complete rational marker-state flow can now be executed by one deterministic
Euler circuit rather than independent local counters.  The stored ten-step word
is `ABABACABAB`, with exact frequencies `(1/2,2/5,1/10)`.  Fixed-phase action
indicator discrepancies are `(1/2,4/5,1/2)`, and arbitrary cyclic phases have
ranges `(1/2,6/5,9/10)`.

### Localized Hall transport

Repeated binary Hall blocks now reduce to xor convolution on the syndrome group.
The Walsh transform diagonalizes every block exactly.  The stored rank-four,
twelve-block audit counts `1,049,760,000` compatible assignments; the maximum
and zero-syndrome counts are both `65,622,784`, with exact reconstruction of a
syndrome-seven witness.

### Fractional direct-clean layers

Rational threshold designs now have denominator-controlled implementations.  In
nonnegative downward-closed systems, componentwise flooring preserves every load
constraint and loses less than `||c||_1/M` under a nonnegative objective.  The
stored optimum `(4/5,3/10)` rounds at denominator seven to `(5/7,2/7)` with loss
`13/70`, while denominator ten is exact.

### Support-chord repair words

Risk classes and prefix-tree shape are now canonicalized together.  In the
stored six-leaf equal-survival audit, 630 ordered decorated trees collapse to 41
survival-preserving orbits.  Their value histogram is `8:2,16:16,32:18,64:5`;
exactly two orbits are optimal and have six ordered lifts.

### Clean-macro shells

Rational shell attenuation now converts to a finite quantum schedule by upward
rounding.  Every cycle inequality remains valid, and cost overhead is less than
`||c||_1/M`.  The stored triangle optimum `(1/3,1/6,1/2)` has cost one;
denominator four has exact grid optimum `5/4`, while denominator six is exact.

### Integration

Repeated interaction motifs now have an asymptotic rate polytope equal to the
projection of normalized circulations, or equivalently the convex hull of simple
cycle means.  The stored two-state graph has means
`(1,2,0)`, `(1,0,2)`, and `(3/2,1/2,1/2)`.  The last cycle is uniquely selected by
its coordinate cap, has scalar mean `5/2`, is exact at every even length, and has
odd-length overhead `1/(2N)`.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_501_506.py
```

or individually with

```bash
python scripts/check_eulerian_marker_flow_realization.py
python scripts/check_walsh_hall_syndrome_convolution.py
python scripts/check_quantized_threshold_designs.py
python scripts/check_risk_decorated_prefix_signatures.py
python scripts/check_quantized_shell_attenuation.py
python scripts/check_asymptotic_interaction_cycle_rates.py
```

The local audits verify the ten-edge Euler circuit, all sixteen Walsh syndrome
counts, one hundred threshold denominators, all 630 ordered decorated code trees,
twenty shell denominators, and every closed interaction walk through length
sixteen.

The next available theorem identifier is `PP3ciz`.
