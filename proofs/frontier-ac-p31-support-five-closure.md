# Frontier pass: exact p=31 support-five closure

## Active branch

`agent/ac-p31-support-five-closure`

Parent: `agent/ac-p31-support-four-closure`.

Only AC is active.

## Theorem block

- **AC5on:** complete five-extra support census.
- **AC5oo:** no endpoint improvement with at most five additional tagged rows.
- **AC5op:** every potential-at-most-two endpoint requires at least six extra tagged rows, hence total tagged support at least fifteen.

## Exact ledger

\[
\begin{array}{c|r|r|r}
(a,5-a)&\text{supports}&\text{partial states}&\Phi\le2\text{ leaves}\\
\hline
(0,5)&53{,}130&6{,}353{,}973&0\\
(1,4)&328{,}900&29{,}331{,}984&0\\
(2,3)&747{,}500&53{,}710{,}877&0\\
(3,2)&780{,}000&50{,}459{,}464&0\\
(4,1)&373{,}750&25{,}043{,}736&0\\
(5,0)&65{,}780&5{,}238{,}193&0.
\end{array}
\]

Totals:

- support choices: `2349060`;
- admissible partial states: `170138227`;
- complete collision-free endpoints with potential at most two: `0`.

## Verification

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_five.cpp -o verify_support_five
./verify_support_five 0
./verify_support_five 1
./verify_support_five 2
./verify_support_five 3
./verify_support_five 4
./verify_support_five 5
```

The per-distribution counts sum to the committed aggregate ledger.

## Consequence

The exact endpoint support required for any improvement from the explicit three-triple state is now at least fifteen tagged layer-row addresses: the nine current core addresses plus at least six additional addresses.

## Remaining frontier

1. Search the six-extra support layer.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal switch path.
4. Seek a structural explanation for the support closure.

AC6 and the general conjecture remain open.
