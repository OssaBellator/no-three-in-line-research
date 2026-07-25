# All-n product track: exact small-sector constants stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-adaptive-thinning-stage.md`](all-n-product-adaptive-thinning-stage.md).
PX225--PX227 reduce support-four control to the square-root ambient scale.
PX228--PX231 now close the remaining rank-one and minimal-support asymptotic
gaps by direct counting on the retained block.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Adaptive support four | **CONTROLLED ABOVE `N^(1/2+epsilon)`** | PX225--PX227 choose an ambient-dependent thinning probability and obtain expected support four at most `s/2`. |
| Rank-one/two-background geometry | **DECODER-OR-LINEAR** | PX228 extracts an endpoint-disjoint secant star from every heavy candidate cell; PX229 gives linear expected load otherwise. |
| Rank-two support two | **CONSTANT SCALE** | PX230 gives the exact bound `e^(4Delta)L_Z/2`. |
| Rank-two support three | **LINEAR WITH EXACT COUNT** | PX231 gives `e^(4Delta)L_Z(s-2)`. |
| Rank-three support three | **CONSTANT SCALE** | PX230 gives the exact bound `e^(4Delta)/3`. |
| Internal higher-support rank three | **LINEAR** | PX227 gives `O(e^(4Delta)s)` under adaptive thinning. |
| Small-block support four | **OPEN** | Packet and diffuse-defect methods remain necessary for `t<=N^(1/2+o(1))`. |
| Strict net descent | **OPEN** | All sectors are structurally decoded or at most linear, but the present spread constants are too crude for a universal sign. |
| Infinite exact closure | **OPEN** | No terminating all-side doubling theorem follows yet. |

## 1. Rank-one decoder

For one candidate cell `f`, let `mu(f)` count background pairs collinear with
`f`.  If each line contains at most `K` background points, the line cliques
through `f` contain an endpoint-disjoint matching of total size at least

\[
\frac{\mu(f)}K.
\]

Therefore every heavy rank-one cell is already a clean secant-star outcome.
If no star of order `m` exists, then every off-diagonal candidate cell has
weight below `Km`, so

\[
W_{1,2}<Km\,s(s-1)
\]

and

\[
\mathbb E T_{1,2}
<
e^{4\Delta}Km(s-1).
\]

The rank-one frontier is thus quantitative rather than structural.

## 2. Exact short-cycle constants

Direct counting on `s` retained endpoint labels gives:

- `binom(s,2)` transposition pairs;
- `s(s-1)(s-2)` directed two-paths;
- `2 binom(s,3)` directed three-cycles.

Using the rank-two and rank-three cylinder bounds yields

\[
\mathbb E T_{2,2}
\le
\frac12e^{4\Delta}L_Z,
\]

\[
\mathbb E T_{2,3}
\le
e^{4\Delta}L_Z(s-2),
\]

and

\[
\mathbb E T_{3,3}
\le
\frac13e^{4\Delta}.
\]

These replace the much larger constants inherited from pre-thinning weighted
counts.

## 3. Remaining proof tasks

1. **Cylinder constant sharpening.** Use the actual union-of-two-or-three-
   partial-matchings structure to improve `e^(4Delta)`.
2. **Exact destruction constants.** Quantify how many old triples every clean
   star, loaded line, radial core, and packet release destroys per moved point.
3. **Linear-sector sign.** Compare the exact support-three and rank-one
   coefficients against those destruction constants.
4. **Small-block packet descent.** Resolve diffuse selected defects only in the
   reduced range `t<=N^(1/2+o(1))`.
5. **Conditioned constants.** Preserve any improved cylinder constant under the
   sequential exposure interface.
6. **Depth-two theorem.** Assemble all sector constants into a strict negative
   drift statement.
7. **Closure conversion.** Insert the terminating decoder into PX63.

The immediate frontier is item 1 or item 2.  No rank-at-most-three sector now
lacks either an explicit decoder or an at-most-linear expected-load bound.

## 4. Verification

```bash
python scripts/verify_product_adaptive_thinning.py
python scripts/verify_product_rank_one_short_cycles.py
```

The new verifier exhausts line-clique star extraction and the exact
transposition/path/cycle populations and expected-load coefficients.

The classical no-three-in-line conjecture and infinite product closure remain
open.
