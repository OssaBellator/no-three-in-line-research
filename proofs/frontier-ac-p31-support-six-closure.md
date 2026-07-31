# Frontier pass: complete p=31 support-six closure

## Active branch

`agent/ac-p31-support-six-closure`

Parent: `agent/ac-p31-support-six-balanced-closure`.

Only AC is active.

## Theorem block

- **AC5os:** complete six-extra support census.
- **AC5ot:** no endpoint improvement with at most six additional tagged rows.
- **AC5ou:** every potential-at-most-two endpoint requires at least seven extras, hence total tagged support at least sixteen.

## Exact ledger

\[
\begin{array}{c|r|r|r}
(a,6-a)&\text{supports}&\text{partial states}&\Phi\le2\text{ leaves}\\
\hline
(0,6)&177{,}100&35{,}678{,}890&0\\
(1,5)&1{,}381{,}380&202{,}363{,}641&0\\
(2,4)&4{,}111{,}250&467{,}355{,}187&0\\
(3,3)&5{,}980{,}000&577{,}440{,}893&0\\
(4,2)&4{,}485{,}000&416{,}388{,}566&0\\
(5,1)&1{,}644{,}500&169{,}065{,}024&0\\
(6,0)&230{,}230&29{,}657{,}917&0.
\end{array}
\]

Totals:

- support choices: `18009460`;
- admissible partial states: `1897950118`;
- complete collision-free endpoints with potential at most two: `0`.

## Verification

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_six.cpp -o verify_support_six
for shard in $(seq 0 31); do
  ./verify_support_six "$shard"
done
```

Every shard asserts its exact distribution, support interval, support count, partial-state count and zero complete endpoints.

## Consequence

Every endpoint lowering the explicit three-triple state must change at least seven additional layer-row addresses outside the nine-address core, for total tagged support at least sixteen.

## Remaining frontier

1. Search the seven-extra support layer.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal low-barrier switch path.
4. Explain the support closure structurally.

AC6 and the general conjecture remain open.
