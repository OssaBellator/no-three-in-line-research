# Exact p=31 five-triple lower frontier

## Status

This AC-only note proves AC5nz for the five-triple endpoint of AC5ny. It establishes the complete lower-barrier side of the next minimax step. It does not yet provide an upper path to four triples.

## AC5nz -- barrier at least ten from the recovered five-triple state -- PROVED

Let `v_5` be the explicit endpoint in `data/ac-p31-recovered-tail.json`. Complete breadth-first enumeration gives

\[
\begin{array}{c|ccccc}
\text{barrier}&5&6&7&8&9\\\hline
\text{component states}&1&2&14&100&6797.
\end{array}
\]

None of these components contains a state of potential below five. Therefore

\[
\boxed{\mathcal B(v_5,\{\Phi<5\})\ge10.}
\]

### Proof

Every legal switch neighbour is generated from its exact layer and row pair. States are admitted only when the two permutation layers remain disjoint and their exact determinant-count potential is at most the declared barrier. Exhausting each queue gives the displayed component size and no lower endpoint. QED.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_five_triple_frontier.cpp -o verify_five
```

Run all components:

```text
./verify_five
```

or one barrier at a time, for example:

```text
./verify_five 9
```

The expected barrier-nine result is `6797` states and zero lower states.

## Remaining frontier

Find a physical path from `v_5` to potential at most four inside barrier ten. Such a path, together with AC5nz, would prove the exact minimax barrier is ten. Search progress without a replayable path remains non-theorem evidence.
