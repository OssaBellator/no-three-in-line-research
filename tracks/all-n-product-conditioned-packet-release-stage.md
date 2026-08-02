# All-n product track: conditioned packet-release stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-common-product-packet-stage.md`](all-n-product-common-product-packet-stage.md).
PX210--PX212 extract a heavy common-product packet and release every
packet-certified transposition collision with a constant-density matching bank.
PX213--PX214 now make that bank stable under sequential exposure and transfer
all remaining rank-at-most-three collateral to explicit weighted cylinder sums.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Packet release existence | **COMPLETE** | PX212 supplies a no-two-cycle, forbidden-position-avoiding matching family of constant density. |
| Packet-release spread | **COMPLETE** | PX212 gives `e^(4Delta+4)/(h)_r` fixed-rank cylinders. |
| Sequential conditioning | **COMPLETE** | PX213 proves that any exposure adds only one reversed partial matching, so residual spread costs one absolute `e^4` factor. |
| Packet-certified support four | **ELIMINATED EXACTLY** | Every packet transposition has probability zero under the release measure. |
| External load transfer | **COMPLETE CONDITIONALLY ON GEOMETRIC WEIGHTS** | PX214 converts external one-, two-, and three-cell weights into expected collateral. |
| External geometric weights | **OPEN** | No bound yet pays all other anchors and product levels against packet-certified destruction. |
| Absolute recursion depth | **OPEN** | No theorem yet proves bounded-depth termination. |
| Infinite exact closure | **OPEN** | No all-side exact doubling theorem follows yet. |

## 1. Conditioning costs one matching

Fix an exposed partial packet matching

\[
E_0=\{i_r\mapsto j_r:r\in[a]\}.
\]

A future edge `j_r->i_r` would complete a packet two-cycle.  The surviving
reverse positions form a partial matching because exposed sources and targets
are separately distinct.  Thus the residual forbidden degree is at most

\[
\Delta+1,
\]

independently of `a`.

PX213 applies the PX212 mixed-rank local lemma in residual order `n=h-a`.  If

\[
n\ge\max(32,32(\Delta+1)),
\]

then every extendable exposure has at least

\[
e^{-4\Delta-8}n!
\]

released extensions.  Conditional cylinders satisfy

\[
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\le
\frac{e^{4\Delta+8}}{(n)_{|E_1|}}.
\]

The constant does not grow with the exposure rank.

## 2. Exact external-load interface

Delete every certificate containing a forbidden cell or a packet transposition;
its release probability is zero.  Let `W_r^ext` be the remaining weighted
rank-`r` certificate mass.

PX214 gives

\[
\mathbb E\Phi_{\rm ext}
\le
 e^{4\Delta+4}
 \sum_{r=1}^3
 \frac{W_r^{\rm ext}}{(h)_r}.
\]

After exposure, the same formula holds with residual order and constant
`e^(4Delta+8)`.

Therefore the packet-release probability theory is complete for the present
rank range.  Strict improvement follows whenever the guaranteed old mass
removed by every release exceeds this normalized external load.

## 3. Remaining proof tasks

1. **External rank-one load.** Bound one replacement plus two background points
   on packet rows and columns.
2. **External rank-two load.** Bound pairs through anchors other than the
   extracted anchor and through product levels other than the extracted level.
3. **External rank-three load.** Combine square-root thinning and packet
   structure to pay all-candidate triples inside the packet subgrid.
4. **Destroyed packet mass.** Quantify the old selected transposition collisions
   removed by a packet release, rather than only the candidate collision family.
5. **Second-packet decoder.** Show that excessive external rank-two mass extracts
   another low-overlap common-product packet.
6. **Packet packing.** Release several edge-disjoint packets simultaneously while
   preserving bounded forbidden degree and spread.
7. **Small packet absorption.** Exhaust or absorb packets below the PX212 order
   threshold.
8. **Depth-two accounting.** Insert the external load bounds into PX214a and
   prove strict net improvement in bounded depth.
9. **Closure conversion.** Apply the terminating decoder to PX63.

The immediate frontier is item 2 or item 5.  The probabilistic release mechanism
and its conditioned cylinder laws are no longer missing inputs.

## 4. Verification

```bash
python scripts/verify_product_conditioned_packet_release.py
```

The verifier checks the reverse-partial-matching structure, exact conditioned
families at small orders, the residual `Delta+1` local-lemma inequalities, zero
packet-transposition probability, and weighted external-load transfer.

The classical no-three-in-line conjecture and infinite product closure remain
open.