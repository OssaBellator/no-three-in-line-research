# All-n product track: causal destruction and strict-sign stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-optimized-spread-stage.md`](all-n-product-optimized-spread-stage.md).
PX232--PX234 optimize the positive cylinder ledger.  PX235--PX248 now separate
old deletion from prospective-recreation suppression, compute the exact
first-generation destruction coefficients, and replace the rank-one first
moment by a heavy-cell avoidance dichotomy.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Old block deletion | **EXACT** | PX235 proves that forbidding every current block position deletes exactly every old certificate meeting the moved block. |
| Fixed-switch cancellation | **EXACT** | PX236 gives `F_star-D_star=Delta_raw-Gamma_A(W)`. |
| Prospective star/radial credit | **EXACT** | PX237 gives one cancellation unit per designated naive switched triple. |
| Packet causal role | **CLARIFIED** | PX238 separates old block deletion from packet recurrence suppression; packet crosses are removed from creation weights. |
| Unified sign criterion | **COMPLETE CONDITIONALLY ON WEIGHTS** | PX239 combines exact deletion with the optimized cylinder ledger. |
| Old clean-star destruction | **EXACT LINEAR** | PX240 gives `D_A>=s`. |
| Loaded-line destruction | **EXACT / SUPERLINEAR** | PX241 gives `binom(ell,3)-binom(ell-s,3)`; PX242 gives at least `s ell^2/32` after type extraction. |
| Radial-core destruction | **EXACT LINEAR** | PX243 gives one unit per injectively assigned old radial certificate. |
| Loaded-line strict sign | **PROVED AGAINST ANY FIXED LINEAR LEDGER** | PX244 shows `ell>sqrt(32b)` beats creation `<=b s`. |
| Heavy rank-one cells | **DETERMINISTICALLY AVOIDABLE WHEN SPARSE** | PX245--PX246 add them to the forbidden graph and retain matching existence/spread. |
| Rank-one failure structure | **EXACT** | PX247--PX248 force a row or column field of linearly many large star centres. |
| Linear clean-star/radial sign | **OPEN** | Their guaranteed deletion coefficient is one, so external linear creation still needs a stronger decoder or weighted potential. |
| Small-block packet descent | **OPEN** | Still confined to `t<=N^(1/2+o(1))`. |
| Infinite exact closure | **OPEN** | No terminating all-side doubling theorem follows yet. |

## 1. Causal ledger

For a moved current block `A`, original cells are forbidden.  Every old
certificate meeting `A` is therefore absent from every replacement state:

\[
D_A=\Phi(S)-\Phi(S\setminus A).
\]

For a fixed switch removing `C_0`, inserting `W`, and then rematching `A`, PX236
defines the naive switched load touching `A`,

\[
\Gamma_A(W)
=
\Phi(X\cup A\cup W)-\Phi(X\cup W),
\]

and proves

\[
F_\star-D_\star
=
\Delta_{\rm raw}-\Gamma_A(W).
\]

Thus a prospective clean star of order `s` is not an informal old-destruction
term.  It is an exact subtraction of at least `s` from the naive fixed-switch
creation ledger.

Packet release has a parallel but distinct role.  The moved block deletes old
packet defects because its current positions are forbidden.  The no-two-cycle
constraints then make the entire packet candidate family probability zero,
preventing recreation.

## 2. Exact first-generation destruction

For an old endpoint-disjoint star or injective radial core of order `s`,

\[
D_A\ge s.
\]

For a line containing `ell` selected points, moving `s` of them gives the exact
old line shadow

\[
D_L(\ell,s)
=
\binom\ell3-
\binom{\ell-s}3.
\]

A layer-channel type occurs at least `ceil(ell/(2q))` times.  When `ell>=8`, the
corresponding movable block satisfies

\[
D_L(\ell,s)
\ge
\frac{s\ell^2}{32}
\ge
\frac{\ell^3}{64q}.
\]

Therefore every fixed linear creation coefficient is eventually beaten by a
sufficiently loaded line.  The unresolved sign problem is genuinely the
linear-credit star/radial regime.

## 3. Rank-one heavy-cell avoidance

Let `mu(f)` be the one-cell/two-background weight and

\[
H_m=\{f:\mu(f)\ge m\}.
\]

If `H_m` has row/column degree `lambda_m`, treating it as an additional
forbidden graph gives a spread matching bank whenever

\[
s\ge8(\Delta+\lambda_m).
\]

Every state then has rank-one cost less than `m s`.  Mere executability needs
only

\[
s\ge2(\Delta+\lambda_m).
\]

If no such heavy-avoiding matching exists, PX247 forces some row or column to
contain more than

\[
\frac s2-\Delta
\]

heavy cells.  With background line cap `K`, every one of those cells centres a
star of order at least `m/K`.

## 4. Remaining proof tasks

1. **Coordinate star-field decoder.** From one row or column containing linearly
   many heavy candidate star centres, extract a bounded-overlap simultaneous
   neutralization batch or a loaded background point/line.
2. **Linear clean-star sign.** Use the exact `Gamma_A(W)` credit and the paid-bank
   destruction `d_i` to beat the remaining rank-one and support-three linear
   terms.
3. **Linear radial sign.** Quantify additional old shadow in aligned/radial cores
   beyond the one-certificate-per-endpoint baseline.
4. **Packet causal accounting.** Apply PX238 consistently in the diffuse
   small-block packet regime, separating block deletion from recurrence
   suppression.
5. **Conditioned depth-two assembly.** Insert PX239 into the recursive extraction
   sequence without double counting old certificates across generations.
6. **Closure conversion.** Insert a terminating decoder into PX63.

The immediate frontier is item 1 or item 2.  The exact negative ledger and the
loaded-line sign are no longer missing inputs.

## 5. Verification

```bash
python scripts/verify_product_causal_destruction_ledger.py
python scripts/verify_product_first_generation_destruction.py
python scripts/verify_product_rank_one_heavy_avoidance.py
```

The verifiers check the cancellation identity, packet credit separation, exact
loaded-line deletion, cubic line envelope, star/radial injections, augmented
forbidden matching thresholds, and coordinate concentration.

The classical no-three-in-line conjecture and infinite product closure remain
open.
