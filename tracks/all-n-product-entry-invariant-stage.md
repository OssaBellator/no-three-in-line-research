# All-n product track: effective rectangle-label repair stage

**Branch:** `research/all-n-product-construction`

PX397--PX450 audit the PX63 entry and lift every active decoder to exact
rectangle-label moves. PX451--PX478 make the asymptotic branch effective.
PX479--PX487 compress the cutoff using exact depth and reciprocal divisor
witnesses. PX488--PX492 use the rational exponent `8/109`.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| PX63 entry | **AUDITED** | Every positive rectangle state re-enters through a label block or high source with explicit destruction and spread. |
| Rectangle invariants | **LIFTED** | Terminal, first-generation, packet, mixed-shadow, and recurrence moves are paired `t/r` label permutations. |
| Paired internal sign | **EFFECTIVE** | `A_3=320` and corrected thinning constants force internal rank-three creation below destruction. |
| Dependency DAG | **AUDITED** | The manifest is acyclic and every move-producing block is rectangle-label compatible. |
| Nested depth | **EFFECTIVE** | `d_*(N)=1+ceil(log_2(log_2 max(N,2)+2))`. |
| Packet-family parameter | **REMOVED** | The active path pays support four directly above threshold and uses historical packet corrections below it. |
| Earlier cutoffs | **SUPERSEDED** | PX478: `10^4000`; PX482: `10^3650`; PX487: `10^2950`. |
| Active cutoff | **EXPLICIT** | PX492 gives `N_3=10^2900`. |
| Asymptotic exact doubling | **PROVED AS A REDUCTION** | For every `n>=N_3`, the indexed host-compatible causal loop reaches zero bad triples. |
| Below-cutoff orders | **OPEN** | A non-enumerative bridge or interval-specific maximal-divisor theorem is required. |
| Exact all-side closure | **OPEN** | No finite-range bridge has been proved. |

## Active constants

\[
T(N)=\lceil N^{3/5}\rceil,
\qquad
A_3=320,
\]

\[
\mathfrak d(N)\le10^{59}N^{16/109},
\qquad
N_3=10^{2900}.
\]

The retained-order exponent is

\[
\frac65-1-\frac{16}{109}
=
\frac{29}{545}>0.
\]

At the starting order the exact nested values remain

\[
d_*(N_3)=15,
\qquad
\Delta_*(N_3)=33.
\]

The divisor-controlled retained-order ratio has logarithmic margin above `3.0`,
and the four-return ratio has margin above `12`.

## Integrated repair path

1. Re-enter from every positive rectangle state by PX448.
2. Send large source blocks to the effective paired decoder.
3. Send high sources to channel-free weighted return.
4. Four one-variable returns, or one two-variable return, cross `N^(3/5)`.
5. Pay support four directly on large blocks.
6. Correct selected packet defects by unique label transpositions and forbid
   their historical assignments.
7. Keep every strict decrease inside the factor-compatible rectangle state space
   and iterate the integer potential to zero.

## Immediate frontier

1. **Structural finite-range bridge.** Produce larger exact factors from every
   smaller order without assuming the desired doubling theorem at intermediate
   orders.
2. **Interval-specific maximal-divisor bounds.** Universal power bounds now show
   diminishing returns; exploit the exact range `m< N^2` on logarithmic
   intervals instead.
3. **Divisor witness optimization.** Determine whether any rational exponent
   materially beats `8/109`; improvements of only tens of decimal orders do not
   change the need for a bridge.
4. **Practical census boundary.** Resume exact finite enumeration only after the
   cutoff has been reduced to a computationally meaningful range.

## Verification

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_explicit_cartesian_triples.py
python scripts/verify_product_explicit_nested_depth.py
python scripts/verify_product_packet_family_free_path.py
python scripts/verify_product_explicit_common_cutoff.py
python scripts/verify_product_compressed_common_cutoff.py
python scripts/verify_product_fourteenth_divisor_cutoff.py
python scripts/verify_product_rational_divisor_cutoff.py
```

Exact all-side product closure and the classical no-three-in-line conjecture
remain open.
