# Complete radius-two obstruction for the side-seven `(3,2,2)` class

PX533--PX536 exhaust radius-two support through fourteen in all four canonical
classes.  The `(3,2,2)` class has only three remaining support strata:

\[
16,\qquad18,\qquad20.
\]

They contain `478`, `132`, and `4` selectors.  This chapter exhausts all three
and thereby closes the entire radius-two layer of this relative class.

## 1. Support sixteen

### Theorem PX537 -- PROVED FINITE

All

\[
\boxed{478}
\]

radius-two `(3,2,2)` selectors with

\[
|F\triangle F_0|=16
\]

fail the coordinate CSP.  Four deterministic shards visit exactly

\[
81{,}347{,}148,\quad
49{,}661{,}110,\quad
84{,}567{,}840,\quad
95{,}127{,}226
\]

nodes, for total

\[
\boxed{310{,}703{,}324}.
\]

## 2. Final two support strata

### Theorem PX538 -- PROVED FINITE

All `132` support-eighteen selectors fail after exactly

\[
\boxed{75{,}025{,}562}
\]

coordinate-CSP nodes.

### Theorem PX539 -- PROVED FINITE

All four support-twenty selectors fail after exactly

\[
\boxed{1{,}214{,}916}
\]

coordinate-CSP nodes.

These four selectors are the maximal-support states in the exact radius-two
histogram of PX521.

## 3. Complete class obstruction

The `(3,2,2)` radius-two histogram is:

| Support | Selectors | CSP nodes |
|---:|---:|---:|
| 8 | 725 | 434,069,304 |
| 10 | 904 | 611,789,795 |
| 12 | 1,202 | 708,051,312 |
| 14 | 988 | 639,620,973 |
| 16 | 478 | 310,703,324 |
| 18 | 132 | 75,025,562 |
| 20 | 4 | 1,214,916 |
| **Total** | **4,433** | **2,780,475,186** |

### Corollary PX540 -- PROVED FINITE

No selector at alternating-cycle distance two from the certified `(3,2,2)`
centre has a no-three coordinate embedding in any radix orientation.

Consequently any successful full-selector template for the `(3,2,2)` relative
class has selector-cycle distance at least three from the current centre.

This closes one canonical class at radius two.  It does not prove that the
class, or universal side-seven doubling, is globally infeasible.

## 4. Verification

The generic exact radius-two support search regenerates the requested selector
stratum and applies the PX515 dangerous-point CSP.  Run the four support-sixteen
shards and the complete support-eighteen and support-twenty cases.  The theorem
verifier records the exact selector and node totals displayed above.
