# Weighted same-token labelled-fan extraction

**Branch:** `research/geometric-cleaning`

This note strengthens the unweighted labelled-fan output of GC4k. The point is not to count a shared Hall-deficiency token as many independent payments. Instead, it preserves a constant fraction of the *star weight* inside one structural fibre, producing a quantitatively large compatible object for the next geometric router.

## Setup

Let \(\mathcal Y\) be a finite family of star reopenings. Each \(y\in\mathcal Y\) has nonnegative current destroyed-incidence weight \(w(y)\), uses one common paid token \(\pi\), and carries one of at most \(T\) geometric role labels. Put the full installation-conflict graph on \(\mathcal Y\). Write

\[
W=\sum_{y\in\mathcal Y}w(y).
\]

## GC4l — weighted labelled-fan dichotomy — PROVED

For every integer \(\Gamma\ge 0\), one role class \(\mathcal Y_\lambda\) has weight at least \(W/T\), and one of the following holds:

1. some member of \(\mathcal Y_\lambda\) conflicts with more than \(\Gamma\) other members of that same token--role fibre; or
2. the fibre contains an installably compatible family \(\mathcal I\) satisfying
   \[
   \sum_{y\in\mathcal I}w(y)
   \ge
   \frac{1}{\Gamma+1}
   \sum_{y\in\mathcal Y_\lambda}w(y)
   \ge
   \frac{W}{T(\Gamma+1)}.
   \]

### Proof

Pigeonhole the total weight among the at most \(T\) role classes and choose \(\lambda\) with weight at least \(W/T\). If outcome 1 fails, the induced conflict graph on \(\mathcal Y_\lambda\) has maximum degree at most \(\Gamma\). Greedy colouring gives a proper colouring with at most \(\Gamma+1\) colours. Every colour class is an installably compatible family, and one colour class carries at least a \(1/(\Gamma+1)\) fraction of the fibre weight. This proves outcome 2. \(\square\)

## Interpretation

The conclusion is deliberately structural. All members still share \(\pi\), so their weights are not asserted to be independently paid. What is preserved is enough current destroyed-incidence mass to force the next step to explain one of two explicit phenomena:

- a second-order installation overload around one reopening; or
- a broad compatible fan in one geometric role whose collateral can be audited jointly.

Thus a Hall-deficient cluster cannot lose its quantitative scale merely because its star weights are uneven. The remaining open step is geometric: identify the role-specific joint bank or delegation that turns this weighted fan into a paid transition.

## Finite check

`scripts/verify_gc_weighted_labelled_fan.py` exhausts small labelled graphs and positive integer weight assignments. It checks both weight pigeonholing and the maximum-degree weighted independent-set bound.
