# Explicit p=31 four-triple frontier and route to three

## Status

This AC-only note proves AC5od--AC5of for the four-triple endpoint of AC5oc.

## AC5od -- complete four-triple immediate repair atlas -- PROVED

The four current triples lie on primitive lines

\[
(3,5,56),\quad(2,-1,-1),\quad(1,1,35),\quad(1,-1,9).
\]

Exactly two triples share a selected point, namely blue `(22,13)`; the other two are vertex-disjoint from that pair and from each other.

There are exactly 810 legal immediate two-row switches and none improves the potential. Their least successor potential is six, attained by exactly three moves:

\[
b:(19,24),\qquad r:(19,26),\qquad r:(5,7).
\]

The first two destroy no current triple and create two; the third destroys one and creates three.

### Proof

Enumerate every two-row swap in each layer, retain exactly the disjoint-layer successors, and recompute every real collinear triple. The complete distributions are stored in `data/ac-p31-four-triple-core.json` and checked by `scripts/verify_ac_p31_four_triple_core.py`. QED.

## AC5oe -- exact minimax barrier nine from four triples -- PROVED

Complete sublevel enumeration gives

\[
\begin{array}{c|ccccc}
\text{barrier}&4&5&6&7&8\\\hline
\text{component states}&1&1&5&29&465.
\end{array}
\]

None contains a state below potential four.

The 35-switch path in `data/ac-p31-four-to-three.json` reaches potential three and never exceeds potential nine. Therefore

\[
\boxed{\mathcal B(v_4,\{\Phi<4\})=9.}
\]

### Proof

The displayed finite components give the lower bound. Direct physical replay of the stored switches gives the upper bound. QED.

## AC5of -- explicit three-triple endpoint -- PROVED

The endpoint red permutation is

\[
(14,15,9,18,8,25,29,3,4,13,19,2,23,28,1,12,7,24,6,17,11,26,30,5,22,27,20,16,21,10)
\]

and the blue permutation is

\[
(18,10,24,6,14,15,23,20,25,1,9,4,7,29,30,27,28,19,2,5,3,13,21,11,8,26,12,22,17,16).
\]

They are disjoint permutation layers whose union has exactly three real collinear triples.

The candidate path was found after 1996 expanded states and 11463 seen states, but those counts are not proof inputs.

## Audits

```text
python scripts/verify_ac_p31_four_triple_core.py

g++ -O3 -std=c++20 scripts/verify_ac_p31_four_triple_frontier.cpp -o verify_four
./verify_four

python scripts/verify_ac_p31_four_to_three.py
```

## Remaining frontier

1. Build the physical three-triple core atlas.
2. Exhaust its lower sublevels.
3. Find and replay a route to two triples, then continue to one and zero.
