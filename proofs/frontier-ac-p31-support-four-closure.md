# Frontier pass: exact p=31 support-four closure

## Active branch

`agent/ac-p31-support-four-closure`

Parent: `agent/ac-p31-support-closure`.

Only AC is active.

## New theorem block

- **AC5ok:** complete four-extra support census.
- **AC5ol:** no endpoint improvement with at most four additional tagged rows.
- **AC5om:** every potential-at-most-two endpoint requires at least five extra tagged rows, hence total tagged support at least fourteen.

## Exact ledger

\[
\begin{array}{c|r|r|r}
(a,4-a)&\text{supports}&\text{partial states}&\Phi\le2\text{ leaves}\\
\hline
(0,4)&12{,}650&937{,}002&0\\
(1,3)&59{,}800&3{,}400{,}092&0\\
(2,2)&97{,}500&4{,}681{,}451&0\\
(3,1)&65{,}000&3{,}010{,}014&0\\
(4,0)&14{,}950&773{,}846&0.
\end{array}
\]

Totals:

- support choices: `249900`;
- admissible partial states: `12802405`;
- complete collision-free endpoints with potential at most two: `0`.

## Verification

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_four.cpp -o verify_support_four
./verify_support_four -1
```

The verifier reconstructs the explicit three-triple state, enumerates every four-extra support distribution, assigns retained values occurrence-faithfully, rejects collisions and branches whose exact partial potential exceeds two, and asserts the committed ledger.

## Consequence

The support-three theorem required at least four extra rows. This pass closes the entire four-extra layer and strengthens the necessary endpoint support to at least five additional layer-row addresses outside the nine-address core.

## Remaining frontier

1. Search the five-extra support layer for the first potential-at-most-two endpoint or another closure.
2. Finish the barrier-nine switch component from the same three-triple state.
3. Convert any wider-support endpoint into a legal switch path.
4. Seek a structural explanation for the support closure.

AC6 and the general conjecture remain open.
