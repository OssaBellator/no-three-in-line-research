# All-n product track: sparse exact reservoir stage

**Branch:** `research/all-n-product-construction`

This stage follows the universal low-syndrome theorem PX63 and the protected
matching reductions beginning at PX89. It records an exact all-side object and
reformulates the remaining infinite-closure problem as protected completion.

## Current endpoints

| Endpoint | Status |
|---|---|
| Universal product seed | PX63 gives a saturated factor-compatible side-`2n` rectangle state with `O(n log n)` bad triples. |
| Exact sparse reservoir | PR3 gives `Omega(n/sqrt(log n))` whole rectangles whose union is exactly no-three. |
| Local decoder | PX67--PX71 give transposition improvement-or-shadow alternatives. |
| Neutralization | PX72--PX80 give spread banks for clean stars, loaded lines, and radial cores. |
| Direction control | PX81--PX88 quantify the low-height barrier and construct low-direction-protected states. |
| Structured state space | PX89--PX97 reduce protected nonlinear completion to two sequential simultaneous-rainbow perfect matchings. |
| Nonlinear switching evidence | PX98 gives a four-row strong-complete trade, PX99 proves rank-three spread at order thirteen, and PX100 gives the switching-flow criterion. |
| Infinite exact closure | **OPEN.** |

## Exact reservoir theorem

PR1 chooses one universal rectangle state with

\[
D_2\le48n,
\qquad
D_3\le221184\,nH_{2n-1}.
\]

PR2 applies rank-sensitive alteration to the rectangle defect hypergraph. PR3
retains at least

\[
\frac{n}{8\sqrt{221184\,H_{2n-1}}}
\]

rectangles. Their `4m` corners are no-three and have degree two on every one of
the `2m` used rows and columns.

This is an exact factor-compatible reservoir for every side, not an approximate
or conditional statement.

## Two completion routes

### Route A: protected host extension

Condition on the PR3 reservoir and expose the unused rectangle/product cells.
Prove that after low-direction protection and removal of the reservoir pair
shadow, the remaining row-column host is superregular and has sufficiently
small normalized rank-two/rank-three certificate load.

A successful theorem should feed directly into the existing clone-space or
superregular selection endpoints.

The quantitative subproblems are:

1. bound the unavailable-cell degree created by reservoir secants after height
   filtering;
2. bound candidate-only triple incidence in the unused host using PX82;
3. absorb the low-height exceptional directions using the coset banks PX89--PX95;
4. finish the remaining degree-two completion while protecting the reservoir.

### Route B: simultaneous-rainbow spread

Prove the PX97 hypothesis: in a fixed number of proper linear edge-colourings of
`K_(ell,ell)`, construct a distribution on simultaneous-rainbow perfect
matchings with uniform rank-three cylinder bounds, including the conditional
second stage.

PX98 supplies a concrete nonlinear four-trade, PX99 shows that the full
order-thirteen solution space already has the required rank-three scale, and
PX100 reduces the asymptotic task to bounded-congestion switching flows under
rank-at-most-two conditioning.

PX96 would then yield a protected nonlinear coset distribution, PX82 supplies
the high-direction codegree saving, and PX90 supplies the local-load endpoint.

## Why the reservoir helps

The PR3 reservoir can be installed before either completion mechanism. Because
it is already no-three, the completion only has to avoid:

- lines through two reservoir points;
- lines through one reservoir point and one previously selected completion
  point;
- candidate-only completion triples.

This separates the certificate ranks exactly into unavailable cells, anchored
pairs, and candidate-only triples—the same three ranks controlled by the
existing selection and neutralization theorems.

## Immediate next theorem

Prove a **reservoir-conditioned load lemma** of the following form.

> After retaining a suitably thinned PR3 reservoir and protecting all primitive
> directions through height `H`, the unused host has normalized unavailable-cell,
> anchored-pair, and candidate-triple loads below the PX90 or clone-selection
> threshold.

The theorem must optimize the reservoir size and height cutoff jointly. The
known bounds suggest using a reservoir smaller than the full PR3 guarantee when
necessary; every subset of the reservoir remains exact and no-three.

## Verification

```bash
python scripts/verify_product_low_syndrome_doubling.py
python scripts/verify_product_sparse_rectangle_reservoir.py
python scripts/verify_product_transposition_decoder.py
python scripts/verify_product_protected_rainbow_reduction.py
python scripts/verify_product_strong_complete_four_trades.py
```

The classical no-three-in-line conjecture and infinite product closure remain
open.