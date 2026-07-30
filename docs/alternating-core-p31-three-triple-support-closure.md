# Exact support closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5oe--AC5oj for the explicit `p=31`, `n=30` three-triple state of AC5od.

It is a finite endpoint theorem. It classifies configurations obtained by permuting the current row values inside the rows supporting the three remaining triples, together with at most three additional tagged row addresses. It does not assert that an arbitrary switch path stays inside such a support.

## Core rows

The red and blue permutations are

\[
R=(12,15,24,9,27,20,4,17,28,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,25,16)
\]

and

\[
B=(17,10,21,22,7,15,8,28,25,13,9,4,20,26,30,12,27,24,29,23,14,1,2,11,18,6,3,16,5,19).
\]

The three occurrences use

\[
R_0=\{14,16,20,23\},
\qquad
B_0=\{9,14,18,20,29\}.
\]

These are nine distinct layer-row addresses.

## AC5oe -- complete two-extra support census -- PROVED

For

\[
A_R\subseteq[30]\setminus R_0,
\qquad
A_B\subseteq[30]\setminus B_0,
\qquad
|A_R|+|A_B|\le2,
\]

permute the current red values on `R_0 union A_R` and the current blue values on `B_0 union A_B`, fix every other layer-row value, and reject red-blue cell collisions.

The maximal distributions give

\[
\begin{array}{c|r|r|r|c}
(|A_R|,|A_B|)&\text{supports}&\text{assignments}&\text{collision-free}&\min\Phi\\
\hline
(1,1)&650&56{,}160{,}000&42{,}195{,}600&3\\
(2,0)&325&28{,}080{,}000&20{,}353{,}104&3\\
(0,2)&300&36{,}288{,}000&28{,}146{,}816&3.
\end{array}
\]

Thus 120,528,000 assignments and 90,695,520 collision-free states are checked.

## AC5of -- no two-extra endpoint improvement -- PROVED

Every collision-free state in the preceding census satisfies

\[
\boxed{\Phi\ge3}.
\]

Hence no endpoint supported on the core plus at most two additional tagged rows has potential two, one or zero.

## AC5og -- first support-expansion bound -- PROVED

Every lower-potential endpoint requires at least three additional tagged rows and hence total tagged support at least twelve.

## AC5oh -- complete three-extra support closure -- PROVED

The first support size not covered by AC5oe has four layer distributions. A branch-and-bound search fixes every outside cell and assigns the retained row values one at a time. When a proposed cell sees `k` already selected points on one real line, the exact potential increment is

\[
\binom{k}{2}.
\]

A partial assignment is rejected immediately when its potential exceeds two. The exact ledgers are

\[
\begin{array}{c|r|r|r}
(|A_R|,|A_B|)&\text{support choices}&\text{partial states}&\text{complete states with }\Phi\le2\\
\hline
(0,3)&2300&109{,}579&0\\
(1,2)&7800&295{,}821&0\\
(2,1)&8125&276{,}343&0\\
(3,0)&2600&92{,}218&0.
\end{array}
\]

In total, all

\[
\boxed{20{,}825}
\]

three-extra supports close after

\[
\boxed{773{,}961}
\]

exact partial states, with no potential-at-most-two endpoint.

## AC5oi -- no three-extra endpoint improvement -- PROVED

No collision-free endpoint supported on the core plus at most three additional tagged rows has potential below three.

The proof is exhaustive: each branch either violates layer disjointness, exceeds potential two at a finite prefix, or reaches a complete assignment. The complete-assignment count under the potential-at-most-two constraint is zero.

## AC5oj -- strengthened support-expansion target -- PROVED

Every endpoint of potential two, one or zero differs from the current state on at least four tagged row addresses outside

\[
R_0\sqcup B_0.
\]

Therefore every successful endpoint repair has total tagged-row support at least

\[
\boxed{|R_0|+|B_0|+4=13}.
\]

This is an endpoint lower bound. A switch path may temporarily use more rows and later restore them.

## Deterministic audit

Compile and run:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_mixed.cpp -o verify_mixed
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_same_layer.cpp -o verify_same
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_three.cpp -o verify_three
./verify_mixed
./verify_same rr
./verify_same bb
./verify_three
```

The three-extra verifier may also be run with arguments `0`, `1`, `2`, or `3` to audit one red-extra distribution separately.

## Remaining frontier

1. Search endpoint supports with at least four additional tagged rows.
2. Finish the exact barrier-nine component from the same three-triple state.
3. Convert a successful wider-support endpoint into a low-barrier switch ordering.
4. Extract a structural explanation for the support-three closure.
5. Generalize the support lower bound beyond this explicit state.

AC6 and the general no-three-in-line conjecture remain open.
