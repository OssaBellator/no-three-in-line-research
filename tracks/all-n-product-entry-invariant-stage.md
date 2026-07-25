# All-n product track: effective rectangle-label repair stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`all-n-product-weighted-return-splice-stage.md`](all-n-product-weighted-return-splice-stage.md).
PX397--PX450 audit the PX63 entry and lift every active decoder to exact
rectangle-label moves.  PX451--PX478 complete the dependency audit and make the
asymptotic branch effective.  PX479--PX482 use the exact nested-depth plateau to
compress the common cutoff.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| PX63 source statement | **RECOVERED** | Every saturated side-`n` factor has a factor-compatible rectangle state with `O(n log n)` bad triples. |
| Entry dichotomy | **AUDITED** | PX397--PX403 give a repeatable label-block/high-source entry with good-bank destruction `D/18` and cylinder factor nine. |
| Rectangle host invariants | **LIFTED** | PX411--PX444 implement terminal, first-generation, packet, mixed-shadow, and recurrence moves as paired `t/r` label permutations. |
| Actual seed line cap | **AUDITED** | PX404 and PX470 use the explicit `n^(1/3+o(1))` line cap; four one-variable returns cross the effective threshold. |
| Paired internal sign | **EFFECTIVE** | PX445--PX446 use the corrected constants and explicit `A_3=320` to keep internal rank-three creation below destruction. |
| Dependency DAG | **AUDITED** | PX451--PX452 and the JSON manifest certify an acyclic rectangle-label/arithmetic dependency path through PX482. |
| Nested depth | **EFFECTIVE** | PX461--PX465 give an exact depth formula and cumulative spread exponent. |
| Divisor loss | **EFFECTIVE** | PX466--PX468 give `mathfrak d(N)<=10^27 N^(1/6)`. |
| Packet-family parameter | **REMOVED FROM ACTIVE PATH** | PX471--PX473 pay support four directly above threshold and use historical packet corrections below it. |
| Original common cutoff | **SUPERSEDED** | PX478 gives `10^4000`. |
| Compressed common cutoff | **EXPLICIT** | PX479--PX482 improve the active cutoff to `N_1=10^3650`. |
| Asymptotic exact doubling | **PROVED AS A REDUCTION** | For every `n>=N_1`, the host-compatible causal repair loop reaches zero bad triples, subject only to the indexed rectangle-label reductions. |
| Below-cutoff orders | **OPEN** | Direct enumeration remains impossible; a non-enumerative bridge or a far sharper range-sensitive cutoff is required. |
| Exact all-side closure | **OPEN** | The finite-range bridge has not been proved. |

## Effective constants

The active threshold and numerical witnesses are

\[
T(N)=\lceil N^{3/5}\rceil,
\qquad
A_3=320,
\]

\[
d_*(N)=1+\left\lceil\log_2(\log_2\max\{N,2\}+2)\right\rceil,
\]

\[
\mathfrak d(N)\le10^{27}N^{1/6},
\qquad
N_1=10^{3650}.
\]

For paired large blocks use

\[
q_\eta=
\min\left\{
\frac{\eta}{20{,}971{,}520e^{2\Delta}\log(2t)},
\frac{\eta t}{32768e^{4\Delta}N\mathfrak d(N)}
\right\},
\qquad
0<\eta\le\frac1{12}.
\]

The retained-order requirement is

\[
q_\eta t\ge\max\{32,16\Delta+4,256e^{2\Delta}\}.
\]

## Integrated repair path

1. PX448 re-enters from every positive rectangle state.
2. A large source block enters the effective paired large-block decoder.
3. A high source enters channel-free weighted return.
4. Four one-variable returns, or one two-variable return, cross `N^(3/5)`.
5. Above threshold, support four is paid directly; no growing packet family is
   maintained.
6. Below threshold, selected packet defects use unique label corrections and
   historical positions prevent recurrence.
7. Every strict decrease remains inside the same factor-compatible rectangle
   state space, so integer potential descent reaches zero for `N>=N_1`.

## Exact cutoff compression

On

\[
10^{3650}\le N\le e^{9000},
\]

PX479 gives the exact values

\[
d_*(N)=15,
\qquad
\Delta_*(N)=33.
\]

The divisor-controlled retained-order ratio already exceeds `e^(3/2)` at the
left endpoint and increases with derivative `1/30`.  At `log N=9000` the proof
hands off to the smooth PX475/PX477 envelope.

## Immediate frontier

1. **Finite-range bridge.** Find a theorem that maps every positive order below
   `N_1` to an order in the effective range without assuming the desired
   doubling theorem at intermediate orders.
2. **Cutoff compression.** Replace the global divisor witness and worst-case
   label-degree constants by interval-specific exact bounds.  The next useful
   target is a staircase cutoff table indexed by exact depth and divisor exponent.
3. **Small-order exact census.** Extend existing exact rectangle/template
   results only far enough to meet a genuinely practical compressed cutoff.
4. **Global closure conversion.** Promote the asymptotic reduction only after a
   finite-range bridge or complete finite census is proved.

## Verification

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_explicit_cartesian_triples.py
python scripts/verify_product_explicit_nested_depth.py
python scripts/verify_product_explicit_divisor_witness.py
python scripts/verify_product_packet_family_free_path.py
python scripts/verify_product_explicit_common_cutoff.py
python scripts/verify_product_compressed_common_cutoff.py
```

Exact all-side product closure and the classical no-three-in-line conjecture
remain open.
