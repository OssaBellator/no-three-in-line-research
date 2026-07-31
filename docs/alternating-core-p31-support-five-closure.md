# Exact support-five closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5on--AC5op for the explicit `p=31`, `n=30` three-triple state. It extends the support-three and support-four closure theorems by exhausting every endpoint obtained from the nine core layer-row addresses together with exactly five additional tagged addresses.

## AC5on -- complete five-extra support census -- PROVED

For `a` red extras and `5-a` blue extras, permute the current retained values on the enlarged supports, fix every outside cell, reject red-blue collisions, and prune a partial assignment as soon as its exact potential exceeds two.

The exact ledger is

\[
\begin{array}{c|r|r|r}
(a,5-a)&\text{support choices}&\text{partial states}&\Phi\le2\text{ endpoints}\\
\hline
(0,5)&53{,}130&6{,}353{,}973&0\\
(1,4)&328{,}900&29{,}331{,}984&0\\
(2,3)&747{,}500&53{,}710{,}877&0\\
(3,2)&780{,}000&50{,}459{,}464&0\\
(4,1)&373{,}750&25{,}043{,}736&0\\
(5,0)&65{,}780&5{,}238{,}193&0.
\end{array}
\]

Thus all

\[
\boxed{2{,}349{,}060}
\]

five-extra support choices close after

\[
\boxed{170{,}138{,}227}
\]

admissible partial states, with no complete collision-free endpoint of potential at most two.

## AC5oo -- no five-extra endpoint improvement -- PROVED

Every collision-free endpoint supported on the nine core addresses plus at most five additional tagged row addresses satisfies

\[
\boxed{\Phi\ge3}.
\]

The earlier support closures handle zero through four extras; AC5on handles exactly five.

## AC5op -- strengthened support-expansion target -- PROVED

Every endpoint of potential two, one or zero differs from the current three-triple state on at least six tagged row addresses outside the nine-address core. Therefore every successful endpoint repair has total tagged layer-row support at least

\[
\boxed{9+6=15}.
\]

This is an endpoint theorem. A switch path may temporarily use more addresses and later restore them.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_five.cpp -o verify_support_five
```

Run all distributions or one red-extra count at a time:

```text
./verify_support_five -1
./verify_support_five 0
./verify_support_five 1
./verify_support_five 2
./verify_support_five 3
./verify_support_five 4
./verify_support_five 5
```

Expected aggregate ledger:

- support choices: `2349060`;
- partial states: `170138227`;
- complete potential-at-most-two endpoints: `0`.

## Remaining frontier

1. Search the six-extra support layer for the first lower-potential endpoint or another exact closure.
2. Finish the independent barrier-nine switch component from the same three-triple state.
3. Convert any wider-support endpoint into a legal low-barrier switch ordering.
4. Extract a structural reason for the closure through total support fourteen.

AC6 and the general no-three-in-line conjecture remain open.
