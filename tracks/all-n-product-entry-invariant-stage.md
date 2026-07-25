# All-n product track: effective rectangle-label repair stage

**Branch:** `research/all-n-product-construction`

PX397--PX450 audit the PX63 entry and lift every active decoder to exact
rectangle-label moves.  PX451--PX478 make the asymptotic branch effective.
PX479--PX482 use the exact nested-depth plateau, and PX483--PX487 optimize the
divisor witness.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| PX63 entry | **AUDITED** | Every positive rectangle state re-enters through a label block or high source with explicit destruction and spread. |
| Rectangle invariants | **LIFTED** | Terminal, first-generation, packet, mixed-shadow, and recurrence moves are paired `t/r` label permutations. |
| Paired internal sign | **EFFECTIVE** | `A_3=320` and corrected thinning constants force internal rank-three creation below destruction. |
| Dependency DAG | **AUDITED** | The manifest is acyclic and every move-producing block is rectangle-label compatible. |
| Nested depth | **EFFECTIVE** | `d_*(N)=1+ceil(log_2(log_2 max(N,2)+2))`. |
| Packet-family parameter | **REMOVED** | The active path pays support four directly above threshold and uses historical packet corrections below it. |
| First explicit cutoff | **SUPERSEDED** | PX478 gave `10^4000`. |
| Exact-depth cutoff | **SUPERSEDED** | PX482 gave `10^3650`. |
| Optimized divisor cutoff | **ACTIVE** | PX487 gives `N_2=10^2950`. |
| Asymptotic exact doubling | **PROVED AS A REDUCTION** | For every `n>=N_2`, the indexed host-compatible causal loop reaches zero bad triples. |
| Below-cutoff orders | **OPEN** | A non-enumerative bridge or a much smaller interval-sensitive cutoff is required. |
| Exact all-side closure | **OPEN** | No finite-range bridge has been proved. |

## Active constants

\[
T(N)=\lceil N^{3/5}\rceil,
\qquad
A_3=320,
\]

\[
\mathfrak d(N)\le10^{72}N^{1/7},
\qquad
N_2=10^{2950}.
\]

The exact nested-depth plateau remains

\[
d_*(N)=15,
\qquad
\Delta_*(N)=33
\]

through the starting interval.  The improved divisor margin is

\[
\frac{T(N)^2}{N\mathfrak d(N)}
\ge10^{-72}N^{2/35}.
\]

At `N=10^2950`, the divisor-controlled retained-order ratio has logarithmic
margin above `5.9`; the four-return ratio has margin above `13`.

## Integrated repair path

1. Re-enter from every positive rectangle state by PX448.
2. Send large source blocks to the effective paired decoder.
3. Send high sources to channel-free weighted return.
4. Four one-variable returns, or one two-variable return, cross `N^(3/5)`.
5. Pay support four directly on large blocks.
6. Correct selected packet defects by unique label transpositions and forbid
   their historical assignments.
7. Keep every strict decrease inside the factor-compatible rectangle state
   space and iterate the integer potential to zero.

## Immediate frontier

1. **Divisor-witness optimization table.** Compare exact finite Euler products
   `C_(1/k)` and resulting cutoffs for all viable integer `k`; PX487 shows that
   `k=14` beats `k=12`.
2. **Interval-specific divisor bounds.** Replace a universal `m^(1/14)` bound by
   exact maximal divisor data over finite logarithmic intervals.
3. **Finite-range bridge.** Find a construction or absorber that enters the
   effective range without enumerating every order below `10^2950`.
4. **Practical census boundary.** Only after compression reaches a feasible
   cutoff should exact rectangle/template enumeration resume.

## Verification

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_explicit_cartesian_triples.py
python scripts/verify_product_explicit_nested_depth.py
python scripts/verify_product_explicit_divisor_witness.py
python scripts/verify_product_packet_family_free_path.py
python scripts/verify_product_explicit_common_cutoff.py
python scripts/verify_product_compressed_common_cutoff.py
python scripts/verify_product_fourteenth_divisor_cutoff.py
```

Exact all-side product closure and the classical no-three-in-line conjecture
remain open.
