# Finite source-mass bank for large restoration jumps

**Branch:** `research/bounded-denominator-absorbers`

BDA5bv--BDA5bz pair every large negative floor-restoration jump in a closed numerator word with one positive source edge of comparable size.  This note converts that pair into a quantitative finite bank whenever positive numerator creation is nonreplenishing inside the epoch.

## Source-mass contract

Fix a family of closed numerator words of length at most `L>=2`.  Every decorated positive source edge `e` has a nonnegative integer capacity `C(e)`.  Traversing `e` with positive increment `d` consumes `d` units of that capacity.  Capacity is not replenished until an explicitly declared outer reset.

Fix a restoration threshold `J_0>=1`.  Only canonical negative restoration jumps of size `J>=J_0` are counted in this note.

## BDA5ca -- comparable positive source mass -- PROVED

For every counted closed word of length `P<=L` and canonical negative restoration jump of size `J`, some positive edge has increment

\[
 d\ge \left\lceil\frac{J}{P-1}\right\rceil
 \ge \left\lceil\frac{J_0}{L-1}\right\rceil.
\]

### Proof

The other `P-1` increments sum to `J`.  Their positive parts also sum to at least `J`, so one is at least their average. QED.

## BDA5cb -- finite source-mass count -- PROVED UNDER THE SOURCE-MASS CONTRACT

Let

\[
 C_{\rm tot}=\sum_e C(e).
\]

The number `N_{>=J_0}` of counted restoration cycles satisfies

\[
\boxed{
N_{\ge J_0}
\le
\left\lfloor\frac{(L-1)C_{\rm tot}}{J_0}\right\rfloor.
}
\]

### Proof

Select the canonical compensation edge from BDA5ca and charge its full positive increment to the edge capacity.  Every selected cycle consumes at least `J_0/(L-1)` units.  The total available mass is `C_tot`. QED.

## BDA5cc -- dyadic restoration bank -- PROVED

For scale `s>=0`, consider canonical restoration jumps

\[
2^s\le J<2^{s+1}.
\]

Every such cycle consumes at least

\[
\left\lceil\frac{2^s}{L-1}\right\rceil
\]

positive source units.  Hence its count is at most

\[
\boxed{
\left\lfloor
\frac{C_{\rm tot}}
{\lceil2^s/(L-1)\rceil}
\right\rfloor.
}
\]

The source and restoration scales differ by at most `ceil(log_2(L-1))`, as in BDA5by.

### Proof

Apply BDA5ca at the lower endpoint of the dyadic bin and sum consumed source capacity. QED.

## BDA5cd -- finite decorated pair tickets -- PROVED

If the decorated positive-edge dictionary is finite and every source unit has occurrence-faithful lineage, the bank may be refined to tickets

\[
(e,u,s),
\qquad 1\le u\le C(e),
\]

where `s` is the restoration scale charged to that unit.  No ticket can be reused in the epoch.

### Proof

Expand each integer edge capacity into labelled unit tokens and assign the consumed units in canonical order. QED.

## BDA5ce -- source/restoration router -- PROVED UNDER THE COMPLETE-BANK CONTRACT

Every large canonical floor restoration has one continuation:

1. current payment or strict arithmetic descent;
2. physical impossibility of the selected edge pair;
3. consumption of the finite source-mass bank of BDA5cb--BDA5cd;
4. a change of edge dictionary, source lineage, capacity, word-length bound or numerator interpretation, returned as an outer reset;
5. or genuinely replenishable source creation, retained as the remaining BDA6 obstruction.

Thus multiplicity-limited source recurrence is finite even when jump magnitudes are unbounded.

### Proof

Use BDA5bv--BDA5bz to select the pair and BDA5ca--BDA5cd to charge it. QED.

## Finite check

`scripts/verify_bda_source_mass_bank.py` generates closed numerator words, verifies the compensation inequality, aggregates decorated source capacities and checks the global and dyadic bank bounds.