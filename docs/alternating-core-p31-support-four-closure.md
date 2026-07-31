# Exact support-four closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5ok--AC5om for the explicit `p=31`, `n=30` three-triple state of AC5od. It extends AC5oe--AC5oj by exhausting every endpoint obtained from the nine core-support layer-row addresses together with exactly four additional tagged row addresses.

This is an endpoint theorem. It does not assert that an arbitrary switch path remains inside one retained support.

## Setup

The current red and blue permutations are

\[
R=(12,15,24,9,27,20,4,17,28,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,25,16)
\]

and

\[
B=(17,10,21,22,7,15,8,28,25,13,9,4,20,26,30,12,27,24,29,23,14,1,2,11,18,6,3,16,5,19).
\]

The three remaining certificate occurrences use the layer-row supports

\[
R_0=\{14,16,20,23\},\qquad B_0=\{9,14,18,20,29\}.
\]

Choose four additional tagged addresses, split as `a` red addresses and `4-a` blue addresses. On the enlarged red and blue supports, permute exactly the current retained values, fix every outside layer-row cell, reject red-blue cell collisions, and retain only complete states of potential at most two.

## AC5ok -- complete four-extra support census -- PROVED

The exact branch-and-bound ledger is

\[
\begin{array}{c|r|r|r}
(a,4-a)&\text{support choices}&\text{partial states}&\text{complete states with }\Phi\le2\\
\hline
(0,4)&12{,}650&937{,}002&0\\
(1,3)&59{,}800&3{,}400{,}092&0\\
(2,2)&97{,}500&4{,}681{,}451&0\\
(3,1)&65{,}000&3{,}010{,}014&0\\
(4,0)&14{,}950&773{,}846&0.
\end{array}
\]

Thus all

\[
\boxed{249{,}900}
\]

four-extra supports close after

\[
\boxed{12{,}802{,}405}
\]

admissible partial states, with no complete endpoint of potential at most two.

### Proof

For each support, fix the 47 outside cells. Assign the retained values to the selected layer-row addresses one at a time. When a new cell sees `k` already selected points on one real line, its exact potential increment is `binom(k,2)`. Reject a branch immediately when its partial potential exceeds two or when it collides with the opposite layer. Every remaining leaf is a complete collision-free assignment. The exhaustive ledger above contains no such leaf. QED.

## AC5ol -- no four-extra endpoint improvement -- PROVED

Every collision-free endpoint supported on

\[
R_0\sqcup B_0
\]

plus at most four additional tagged row addresses satisfies

\[
\boxed{\Phi\ge3}.
\]

Indeed AC5oi closes zero through three additional addresses, and AC5ok closes exactly four.

## AC5om -- strengthened support-expansion target -- PROVED

Every endpoint of potential two, one or zero differs from the current state on at least five tagged row addresses outside the nine core addresses. Hence every successful endpoint repair has total tagged layer-row support at least

\[
\boxed{|R_0|+|B_0|+5=14}.
\]

This is an endpoint lower bound. A switch trajectory may use more rows temporarily and restore them later.

## Deterministic audit

Compile and run:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_four.cpp -o verify_support_four
./verify_support_four -1
```

The optional argument `0,1,2,3,4` audits one red-extra distribution separately. The expected total ledger is:

- support choices: `249900`;
- partial states: `12802405`;
- complete potential-at-most-two endpoints: `0`.

## Remaining frontier

1. Search supports with five additional tagged addresses for the first lower-potential endpoint or another exact closure theorem.
2. Finish the exact barrier-nine component from the same three-triple state.
3. Convert any wider-support endpoint into a legal low-barrier switch ordering.
4. Explain structurally why support sizes through thirteen cannot lower the potential.
5. Generalize the support lower bound beyond this explicit `p=31` state.

AC6 and the general no-three-in-line conjecture remain open.
