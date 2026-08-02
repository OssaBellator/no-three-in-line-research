# Physical p=31 three-triple frontier

## Status

This AC-only note proves AC5og--AC5oh for the explicit three-triple endpoint of AC5of. It identifies the complete current certificate core, audits every legal immediate switch, and proves the lower-bound side of the next minimax step.

## AC5og -- complete three-triple immediate repair atlas -- PROVED

The three current triples are vertex-disjoint and lie on primitive lines

\[
(5,1,64),\qquad (2,1,57),\qquad (1,-1,10).
\]

There are exactly

\[
\boxed{810}
\]

legal two-row switches. None improves the potential. The least successor potential is five, attained by exactly four moves:

\[
b:(3,7),\quad b:(21,26),\quad r:(7,27),\quad r:(7,17).
\]

The first two destroy no current triple and create two; `r:(7,27)` destroys one and creates three; `r:(7,17)` destroys two and creates four.

The number of current triples destroyed by one legal switch has distribution

\[
\begin{array}{c|rrr}
\text{destroyed}&0&1&2\\\hline
\#&583&216&11.
\end{array}
\]

### Proof

Enumerate every two-row swap in both layers, retain exactly those whose inserted cells avoid the opposite layer, and recompute the complete real collinear-triple set. The exact atlas is stored in `data/ac-p31-three-triple-core.json` and independently checked by `scripts/verify_ac_p31_three_triple_core.py`. QED.

## AC5oh -- barrier at least nine from three triples -- PROVED

Complete breadth-first enumeration gives

\[
\begin{array}{c|rrrrrr}
\text{barrier}&3&4&5&6&7&8\\\hline
\text{component states}&1&1&9&42&205&3635.
\end{array}
\]

None of these components contains a state of potential below three. Therefore

\[
\boxed{\mathcal B(v_3,\{\Phi<3\})\ge9.}
\]

### Proof

Generate every legal switch neighbour from its complete layer and row-pair address. Admit a successor only when its exact determinant-count potential is at most the declared barrier. Exhaustion of each queue gives the displayed component size and no lower endpoint. QED.

## Audits

```text
python scripts/verify_ac_p31_three_triple_core.py

g++ -O3 -std=c++20 scripts/verify_ac_p31_three_triple_frontier.cpp -o verify_three
./verify_three
```

## Remaining frontier

Find and replay a path from the explicit three-triple state to potential at most two. A route within barrier nine would combine with AC5oh to prove exact minimax barrier nine; a route requiring a higher barrier would need the corresponding complete lower-component exhaustion.
