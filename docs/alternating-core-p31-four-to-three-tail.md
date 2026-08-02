# Exact p=31 four-to-three tail segment

## Status

This note keeps AC as the sole active research track and proves AC5od--AC5of. It continues the explicit `p=31`, `n=30` trajectory from the four-triple endpoint of AC5ob to a three-triple state.

It does not yet produce a zero-triple configuration or a uniform prime-minus-one theorem.

## AC5od -- exact barrier ten from four triples -- PROVED

Let `v_4` be the endpoint of AC5ob. Complete legal switch components at barriers `4,5,6,7,8,9` have sizes

\[
1,2,10,29,286,2033,
\]

and none contains a state of potential below four.

The 41-switch path stored in `data/ac-p31-tail-four-to-three.json` has maximum potential ten and reaches potential three. Therefore

\[
\boxed{\mathcal B(v_4,\{\Phi<4\})=10.}
\]

### Proof

The exact component enumerations give the lower bound. Replay of the stored legal switch word gives a matching upper path whose maximum potential is ten. QED.

## AC5oe -- explicit 41-switch physical repair -- PROVED

The stored potential sequence is

\[
\begin{aligned}
&4,7,10,8,10,10,8,8,8,10,9,10,10,9,9,9,9,8,10,9,10,\\
&7,8,8,7,10,10,9,9,8,8,10,9,10,8,10,8,9,10,9,8,3.
\end{aligned}
\]

Every switch preserves two disjoint permutation layers. The endpoint has red permutation

\[
(12,15,24,9,27,20,4,28,25,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,17,16)
\]

and blue permutation

\[
(17,10,21,22,7,15,8,23,28,13,9,4,20,26,30,12,27,24,29,5,14,1,2,11,18,6,3,16,25,19).
\]

Its exact potential is three.

### Proof

The verifier checks legality and cross-layer disjointness before every move, then recomputes the determinant potential of all 60 selected cells. The stored sequence and endpoint tables agree exactly. QED.

## AC5of -- durable manifest extension through three triples -- PROVED

The repository-backed explicit trajectory now contains

\[
75\longrightarrow6\longrightarrow5\longrightarrow4\longrightarrow3
\]

using

\[
154+26+32+41=253
\]

legal two-row switches after the alternating-star installation.

The three recovered tail barriers are all exact and equal to ten:

\[
\mathcal B(v_6)=\mathcal B(v_5)=\mathcal B(v_4)=10.
\]

## Deterministic audit

Compile and run:

```text
g++ -O3 -std=c++17 scripts/verify_ac_p31_tail_four_to_three.cpp -o verify_p31_43
./verify_p31_43
```

The verifier reuses the original exact switch-graph implementation, independently recomputes all six lower components and replays all 41 switches.

Expected ledger:

- lower-component sizes: `1,2,10,29,286,2033`;
- switches: `41`;
- maximum potential: `10`;
- terminal potential: `3`;
- deterministic recovery processed/discovered counts: `1,367,504 / 1,524,432`.

## Remaining frontier

1. Add a combined replay audit for the durable trajectory from 75 through three.
2. Begin the exact three-triple search toward two with durable checkpoints.
3. Continue through one and zero triples.
4. Compare the low-potential barriers with the complete `p=19` tail.
5. Extract reusable minimax repair templates from the two explicit prime-minus-one trajectories.

AC6 and the general no-three-in-line conjecture remain open.
