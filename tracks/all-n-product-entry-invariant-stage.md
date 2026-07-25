# All-n product track: audited entry and rectangle-invariant stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`all-n-product-weighted-return-splice-stage.md`](all-n-product-weighted-return-splice-stage.md).
PX397--PX450 recover and audit the actual PX63 entry theorem, replace the hidden
subpower line/channel hypotheses by exact rectangle-label arguments, lift every
large-block decoder sector to factor-compatible `t/r` label permutations, and
obtain an asymptotic exact-doubling reduction subject to one common cutoff and a
dependency audit.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| PX63 source statement | **RECOVERED** | The random rectangle state has explicit expected defect bound and `O(n log n)` potential. |
| Entry dichotomy | **AUDITED** | PX397--PX403 give a large/nested label block or a weighted terminal source with good-bank destruction `D/18` and cylinder factor nine. |
| Seed line occupancy | **AUDITED** | PX404 gives `K=n^(1/3+o(1))`; PX407--PX410 show three return amplifications still cross the square-root threshold. |
| Layer/channel hypothesis | **REMOVED FOR TERMINAL RETURN** | PX411--PX419 replace endpoint channels by the two exact rectangle label variables `t,r`. |
| First-generation host invariants | **LIFTED** | PX420--PX427 implement clean-star, radial, and loaded-line banks as paired label permutations. |
| Packet correction host invariants | **LIFTED** | PX428--PX436 give typed packets, paired correction graphs, and factor-compatible Bernoulli strict sign. |
| Mixed-shadow host invariants | **LIFTED** | PX437--PX441 retain the exact two-bank destruction inequality in paired label space. |
| Packet recurrence | **LIFTED** | PX442--PX443 identify packet complements with label two-cycle events and apply joint release in label space. |
| Unified rectangle invariant | **AVAILABLE AS REDUCTION** | PX444 keeps all indexed decoder moves inside the PX43/PX61 factor-compatible rectangle state space. |
| Paired support-four constant | **CORRECTED** | PX445 uses `32768 e^(4Delta)/eta` to leave relative margin `eta/8`. |
| Paired large-block sign | **AVAILABLE AS REDUCTION** | PX446--PX447 retain internal gap and strict-sign-or-child after constant-copy lifting. |
| Re-entry after each decrease | **AVAILABLE** | PX448 applies the one-hit label construction to every positive rectangle state, not only the initial PX63 seed. |
| Asymptotic repair loop | **PROVED UNDER LABEL-INTERFACE REDUCTIONS** | PX449 gives a finite host-compatible causal subtree ending in strict decrease for sufficiently large order. |
| Asymptotic exact doubling | **REDUCED** | PX450 iterates integer potential descent to zero, pending common-cutoff and dependency audit. |
| Common finite cutoff | **OPEN** | One numerical threshold must dominate paired spread, divisor, label-degree, and terminal-transposition conditions. |
| Below-cutoff orders | **OPEN** | Finite base orders need exact absorbers, certificates, or an independent path into the asymptotic range. |
| Dependency audit | **OPEN** | Mechanically verify that PX397--PX449 invoke only paired label moves and no obsolete individual-point bank. |
| Exact all-side closure | **OPEN** | The finite-order and audit obligations have not been discharged. |

## 1. Audited entry hierarchy

For every nonzero rectangle state with `D` bad triples:

1. one-third source thinning uniquely hits at least `4D/9` triples;
2. one label family carries weight at least `2D/9`;
3. a derangement good subbank has at least `c!/9` states;
4. every good state destroys at least `D/18` old triples;
5. rank-`r` cylinders cost at most `9/(c)_r`;
6. a source-size threshold gives a large label block or one high-weight source.

Thus the original product induction entry is explicit and repeatable after every
strict decrease.

## 2. Rectangle label hierarchy

A `t`- or `r`-assignment moves two paired points in one scalar column.  Permuting
label values on a source set:

- preserves the exact rectangle normal form;
- preserves factor compatibility and saturation;
- never permits a created triple to use both points of one assignment;
- translates one geometric forbidden partial matching to label degree at most
  two;
- retains ordinary falling-factorial cylinder ranks.

This paired representation replaces layer/channel pigeonholing and prevents the
repair tree from leaving the product state space.

## 3. Quantitative asymptotic hierarchy

The actual seed line cap is

\[
K=n^{1/3+o(1)}.
\]

Channel-free one-variable amplification satisfies

\[
D_j
\ge
\left(\frac n{96}\right)^{1-2^{-j}}D_0^{2^{-j}}.
\]

After three high-source returns,

\[
D_3=n^{7/8-o(1)},
\qquad
D_3/K=n^{13/24-o(1)}>n^{1/2}.
\]

A two-variable return gives a next-generation star of order
`n^(2/3-o(1))`.  Large paired blocks use retuned thinning with

\[
C_{\Delta,\eta}
=
32768e^{4\Delta}/\eta,
\]

so the factor-eight paired support-four increase contributes at most
`eta s/8` and the square-root ambient exponent is unchanged.

## Immediate frontier

1. **Common cutoff.** Combine every explicit inequality into one computable
   `N_0`; record how it depends on the divisor cap and inherited label degree.
2. **Dependency audit.** Build a theorem-dependency manifest for PX397--PX449 and
   flag any edge leading to an unlifted individual-point move.
3. **Finite orders.** Enumerate or symbolically absorb all `n<N_0`, or find a
   construction chain entering the asymptotic range.
4. **Global index update.** Promote PX450 only after the cutoff and dependency
   audits pass.
5. **Closure statement.** Distinguish asymptotic conditional doubling from exact
   all-side closure and from the classical conjecture.

## Verification

```bash
python scripts/verify_product_px63_entry_derangement.py
python scripts/verify_product_px64_return_depth.py
python scripts/verify_product_channel_free_label_return.py
python scripts/verify_product_first_generation_label_lift.py
python scripts/verify_product_paired_label_packet.py
python scripts/verify_product_paired_label_mixed_shadow.py
python scripts/verify_product_paired_large_block_margin.py
```

The new scripts encode the finite combinatorial identities and arithmetic
constants used by PX397--PX450.  A repository-wide dependency/cutoff verifier is
the next implementation target.

Exact all-side product closure and the classical no-three-in-line conjecture
remain open.
