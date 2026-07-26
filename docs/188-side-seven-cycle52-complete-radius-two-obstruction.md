# Complete radius-two obstruction for the side-seven `(5,2)` class

PX562--PX564 reject support eighteen in the `(5,2)` relative class.  The
remaining radius-two strata have supports

\[
20,22,24,26,28,30,32,34,36,40.
\]

There is no support-thirty-eight stratum.  This chapter records the completed
exact coordinate census and closes the entire `(5,2)` radius-two layer.

## 1. Support twenty

### Theorem PX565 -- PROVED FINITE

All

\[
\boxed{6{,}762}
\]

radius-two `(5,2)` selectors with

\[
|F\triangle F_0|=20
\]

fail the coordinate CSP in every radix orientation.  Ten deterministic shards
visit exactly

\[
\boxed{5{,}423{,}810{,}214}
\]

nodes in total.  Their node totals are

\[
316{,}808{,}398,
401{,}284{,}589,
489{,}020{,}677,
572{,}742{,}409,
510{,}382{,}544,
\]

\[
533{,}140{,}022,
573{,}035{,}141,
582{,}252{,}474,
649{,}854{,}512,
795{,}289{,}448.
\]

## 2. Supports twenty-two and twenty-four

### Theorem PX566 -- PROVED FINITE

All `3,544` support-twenty-two selectors fail after exactly

\[
\boxed{2{,}767{,}130{,}810}
\]

CSP nodes, and all `1,930` support-twenty-four selectors fail after exactly

\[
\boxed{1{,}535{,}927{,}535}
\]

nodes.

The support-twenty-two shard totals are

\[
299{,}064{,}507,
423{,}592{,}289,
489{,}300{,}346,
432{,}845{,}495,
490{,}193{,}167,
632{,}135{,}006,
\]

and the support-twenty-four totals are

\[
221{,}467{,}808,
320{,}176{,}946,
283{,}375{,}514,
329{,}941{,}224,
380{,}966{,}043.
\]

## 3. Final support strata

### Theorem PX567 -- PROVED FINITE

Every remaining radius-two `(5,2)` selector fails.  The exact ledger is:

| Support | Selectors | CSP nodes |
|---:|---:|---:|
| 26 | 776 | 631,399,744 |
| 28 | 288 | 229,218,191 |
| 30 | 56 | 34,757,139 |
| 32 | 45 | 30,055,392 |
| 34 | 8 | 4,827,528 |
| 36 | 4 | 2,750,582 |
| 38 | 0 | 0 |
| 40 | 1 | 508,527 |

No complete coordinate assignment occurs in any stratum.

## 4. Complete class obstruction

Combining PX523--PX536, PX555, PX562, and PX565--PX567 gives:

| Support | Selectors | CSP nodes |
|---:|---:|---:|
| 8 | 533 | 346,044,962 |
| 10 | 232 | 172,039,249 |
| 12 | 1,584 | 1,103,440,538 |
| 14 | 1,768 | 1,225,466,432 |
| 16 | 5,315 | 4,080,834,197 |
| 18 | 3,704 | 2,766,686,696 |
| 20 | 6,762 | 5,423,810,214 |
| 22 | 3,544 | 2,767,130,810 |
| 24 | 1,930 | 1,535,927,535 |
| 26 | 776 | 631,399,744 |
| 28 | 288 | 229,218,191 |
| 30 | 56 | 34,757,139 |
| 32 | 45 | 30,055,392 |
| 34 | 8 | 4,827,528 |
| 36 | 4 | 2,750,582 |
| 40 | 1 | 508,527 |
| **Total** | **26,550** | **20,354,897,736** |

### Corollary PX568 -- PROVED FINITE

No selector at alternating-cycle distance two from the certified `(5,2)` centre
has a no-three coordinate embedding in any radix orientation.

### Corollary PX569 -- PROVED REDUCTION

Any successful `(5,2)` full-selector template has selector-cycle distance at
least three from the current centre.

Together with PX540 and PX545, three of the four canonical side-seven relative
classes are now completely obstructed through radius two.  Only the long
seven-cycle class remains open at distance two.

This remains a finite obstruction around the certified centre and does not
prove that the `(5,2)` class, universal `2 x 7 -> 14`, or exact all-side closure
is impossible.

## 5. Verification

Run

```bash
python scripts/verify_product_side_seven_cycle52_complete_radius_two.py
```

The wrapper compiles the generic exact range solver, regenerates every requested
support layer, replays the deterministic intervals, checks each recorded node
total, and rejects any run that prints a feasible coordinate assignment.
