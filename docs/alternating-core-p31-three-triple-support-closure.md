# Exact support closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5oe--AC5og for the explicit `p=31`, `n=30` three-triple state of AC5od.

It is a finite endpoint theorem. It classifies configurations obtained by permuting the current row values inside the rows supporting the three remaining triples, together with at most two additional row addresses. It does not assert that an arbitrary switch path stays inside such a support.

## Core rows

The red permutation is

\[
(12,15,24,9,27,20,4,17,28,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,25,16)
\]

and the blue permutation is

\[
(17,10,21,22,7,15,8,28,25,13,9,4,20,26,30,12,27,24,29,23,14,1,2,11,18,6,3,16,5,19).
\]

The three triple occurrences use the red row set

\[
R_0=\{14,16,20,23\}
\]

and blue row set

\[
B_0=\{9,14,18,20,29\}.
\]

The nine layer-row addresses are distinct even when their numerical row labels agree.

## AC5oe -- complete two-extra support census -- PROVED

For disjoint sets

\[
A_R\subseteq[30]\setminus R_0,
\qquad
A_B\subseteq[30]\setminus B_0,
\]

with

\[
|A_R|+|A_B|\le2,
\]

retain every configuration obtained by arbitrarily permuting the current red values on `R_0 union A_R` and the current blue values on `B_0 union A_B`, while fixing every other layer-row value and rejecting red-blue cell collisions.

It is enough to enumerate the three maximal distributions `(1,1)`, `(2,0)` and `(0,2)`, because permutations may fix an added row. The exact ledgers are

\[
\begin{array}{c|r|r|r|c}
(|A_R|,|A_B|)&\text{support choices}&\text{assignments}&\text{collision-free}&\min\Phi\\
\hline
(1,1)&650&56{,}160{,}000&42{,}195{,}600&3\\
(2,0)&325&28{,}080{,}000&20{,}353{,}104&3\\
(0,2)&300&36{,}288{,}000&28{,}146{,}816&3.
\end{array}
\]

Thus the combined census checks

\[
\boxed{120{,}528{,}000}
\]

assignments and

\[
\boxed{90{,}695{,}520}
\]

collision-free two-permutation states.

## AC5of -- no two-extra endpoint improvement -- PROVED

Every collision-free state in the census satisfies

\[
\boxed{\Phi\ge3}.
\]

Hence no endpoint supported on the three-triple core plus at most two additional layer-row addresses has potential two, one or zero.

### Proof

For each support choice, exhaust the full product of the red and blue permutation groups on the retained rows. Every assignment retains one point per layer in each row and column. Reject assignments whose two layers use the same cell. For every remaining state, compute the exact real-line potential by primitive integer line identifiers. The minimum in every support family is three. QED.

## AC5og -- exact support-expansion target -- PROVED

Any lower-potential configuration differs from the current state on at least three layer-row addresses outside

\[
R_0\sqcup B_0.
\]

Equivalently, every successful endpoint repair has total row support at least

\[
\boxed{|R_0|+|B_0|+3=12}
\]

in the layer-tagged row universe.

This is an endpoint lower bound, not a claim that all twelve addresses must move simultaneously or that a successful path cannot temporarily use more addresses and later restore them.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_mixed.cpp -o verify_mixed
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_same_layer.cpp -o verify_same
```

Run:

```text
./verify_mixed
./verify_same rr
./verify_same bb
```

Expected ledgers:

- mixed extras: `650` jobs, `56,160,000` assignments, `42,195,600` valid states;
- two red extras: `325` jobs, `28,080,000` assignments, `20,353,104` valid states;
- two blue extras: `300` jobs, `36,288,000` assignments, `28,146,816` valid states;
- minimum potential in every family: `3`.

## Remaining frontier

1. Search endpoint supports with at least three additional row addresses.
2. Finish the exact barrier-nine switch component from the same three-triple state.
3. Convert a successful wider-support endpoint into a low-barrier switch ordering.
4. Classify why the nine core rows plus two extras cannot discharge the three physical lines.
5. Generalize the support lower bound beyond this explicit state.

AC6 and the general no-three-in-line conjecture remain open.
