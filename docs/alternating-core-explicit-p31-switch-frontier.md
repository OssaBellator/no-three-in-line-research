# Explicit p=31 switch frontier from the strongest AN seed

## Status

This note keeps AC as the sole active research track and proves AC5nt--AC5nw. It starts from the strongest canonical `p=31` alternating-star successor of AC5nr and gives a fully replayable two-row-switch trajectory from 75 real triple occurrences to six.

It does not yet produce a zero-triple configuration on the `30 by 30` board.

## Installed state

Use the `H_1,H_12` seed, switch rows `16,24`, candidate `(16,16)`, and canonical bank permutation

\[
(2,0,6,4,5,3,1).
\]

The installed state consists of two disjoint permutation layers with

\[
\Phi=75.
\]

Every subsequent operation swaps two row images in one layer and is retained only when both inserted cells avoid the opposite layer.

## AC5nt -- explicit 154-switch descent to six triples -- PROVED

There is a legal physical path of

\[
\boxed{154}
\]

two-row switches from the installed state to a state with

\[
\boxed{\Phi=6}.
\]

The first 58 switches reach potential 13. The remaining segment lengths are

\[
12,13,2,14,4,15,36
\]

and reach the checkpoint potentials

\[
13\to12\to11\to10\to9\to8\to7\to6.
\]

The complete move and potential words are stored in

`data/ac-p31-explicit-switch-frontier.json`.

### Proof

Start from the two displayed installed permutation tables. Replay every stored move. At each step the two new cells are distinct from the opposite-layer cells in their rows, so both layers remain disjoint permutations. Exhaustive determinant counting on the 60 selected cells gives the stored potential after every move. The final value is six. QED.

## AC5nu -- exact low-potential checkpoint barriers -- PROVED

For a checkpoint state `v` and target set of lower-potential states, let

\[
\mathcal B(v)=\min_{P:v\leadsto\{\Phi<\Phi(v)\}}
\max_{x\in P}\Phi(x).
\]

Complete sublevel-component enumeration and the stored upper paths give

\[
\begin{array}{c|c|c}
\Phi(v)&\mathcal B(v)&\text{stored lower-component sizes}\
\hline
13&16&1,4,15\text{ at barriers }13,14,15\\
12&13&1\text{ at barrier }12\\
11&11&\text{a flat two-switch corridor}\\
10&12&2,25\text{ at barriers }10,11\\
9&12&1,9,53\text{ at barriers }9,10,11\\
8&12&1,2,8,58\text{ at barriers }8,9,10,11\\
7&11&1,5,38,330\text{ at barriers }7,8,9,10.
\end{array}
\]

Thus the triple potential alone is not a strict repair rank. The exact minimax-barrier component is essential even in this explicit physical trajectory.

### Proof

For each checkpoint, breadth-first search enumerates every legal two-permutation state whose potential is at most the candidate lower barrier. None of the listed lower components contains a state of smaller potential. The stored route stays within the displayed barrier and reaches the next checkpoint. QED.

## AC5nv -- explicit six-triple physical obstruction -- PROVED

The terminal frontier state has red permutation

\[
(19,15,26,18,23,17,8,2,25,13,9,4,20,28,1,12,7,24,29,5,3,30,27,11,14,6,21,16,22,10)
\]

and blue permutation

\[
(12,10,23,9,7,15,26,6,21,1,20,2,8,29,30,16,27,25,3,11,14,18,4,5,22,28,24,13,17,19).
\]

Its exact sublevel-component sizes are

\[
\begin{array}{c|c}
\text{barrier}&\text{component states}\\
\hline
6&1\\
7&9\\
8&33\\
9&860.
\end{array}
\]

None contains a state of potential below six. Consequently

\[
\boxed{\mathcal B(v_6)\ge10.}
\]

This is the current exact physical AC frontier for the selected `p=31` initial state.

### Proof

Enumerate the complete legal switch graph induced by each displayed sublevel. Direct potential evaluation gives the component sizes and confirms that every member has potential at least six. QED.

## AC5nw -- fail-closed status of the wider search -- PROVED

Bounded goal-directed and stochastic searches tested larger barriers through 24 without finding a lower state. These searches were not exhaustive and therefore supply no lower bound beyond AC5nv.

The accepted status is exactly:

1. a certified path from 75 to six;
2. exact checkpoint barriers through the seven-to-six step;
3. exact exclusion of a lower state through barrier nine at the final state;
4. no claim about barriers ten or larger.

A timeout, failed heuristic run, or unvisited state is not interpreted as a geometric obstruction.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_switch_frontier.cpp -o verify_p31
```

Replay the full path:

```text
./verify_p31
```

Check one exact checkpoint family per invocation:

```text
./verify_p31 13
./verify_p31 12
./verify_p31 10
./verify_p31 9
./verify_p31 8
./verify_p31 7
./verify_p31 6
```

The checkpoint modes recompute the component sizes rather than reading them from the data file.

## Remaining frontier

1. Find and verify a route from the six-triple state to a lower state, or exhaust the barrier-ten component.
2. Classify the six remaining triples by line, layer, channel, carry, denominator and owner fields.
3. Build a repair bank targeted at the returned six-triple core rather than using unrestricted switches.
4. Continue to zero and compare the resulting terminal configuration with the `p=19` certificate.
5. Extract a uniform minimax repair template from the `p=19` and `p=31` paths.

AC6 and the general no-three-in-line conjecture remain open.
